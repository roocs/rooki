#!/bin/bash

## Bash script to run against the production rook server at CEDA
#
# Checks WPS operations:
#  - GetCapabilities
#  - DescribeProcess
#  - Execute
#
# Checks various stages of workflow:
#  1. Accepts request
#  2. Polls status location URL
#  3. Downloads response document and extracts metalink URL
#  4. Downloads metalink document and extracts netcdf URL
#  5. Downloads netcdf file and checks it ncdumps okay
#
# Different scenarios are tested:
#  1. Standard subset request
#  2. Request exactly matches original files - so get from Data Node
#  3. Time request extends beyond data range - so get all from Data Node
#  4. No time request at all - so get all from Data Node

# Usage:
#
# $ test_rook_prod.sh [n1 [n2 ... n100]]
#
# Where:
#   n-values - represent tests to include (default: include all)
#

requests_to_include=$@

if [ "$requests_to_include" ]; then
   echo "[INFO] Will only run requests: $requests_to_include"
else
   echo "[INFO] All requests will be run."
fi

service_url="http://rook-wps1.ceda.ac.uk/wps"
prefix="${service_url}?service=WPS&version=1.0.0&request"

# Function to call a URL and write the contents to an output file
# If the call fails, then the script exits
function check_url {

    url=$1
    outfile=${2:-output.txt}

    echo "[INFO] Sending request: $url"
    wget -O $outfile "${url}"

    if [ $? -ne 0 ]; then
        echo "[ERROR] FAILED when calling: $url"
        exit
    fi

    echo "[INFO] SUCCESS: Wrote to: $outfile"
    echo ""
}

function run_request {

    url=$1
    requestid=$2
    skipdownload=$3

    if [ ! "$requestid" ]; then
        echo "[ERROR] Must provide request ID to run a test!"
        exit
    fi

    if [ "$requests_to_include" ] && [[ ! " ${requests_to_include} " =~ " ${requestid} " ]]; then
        echo "[WARN] Skipping request: $requestid"
        return
    fi 

    echo 
    echo "-------------------------"
    echo "[INFO] Running: request $requestid"
    echo "-------------------------"
    echo

    check_url $url ${requestid}.execute.txt

    echo "[INFO] Get status URL..."
    status_url=$(cat ${requestid}.execute.txt | grep statusLocation | cut -d\" -f20)
    status_file=${requestid}.status.txt

    while [ 1 ]; do
        sleep 5
        echo "[INFO] Polling job..."
        check_url $status_url $status_file

        if [ "$(grep ProcessSucceeded $status_file)" ]; then
        echo "[INFO] Job completed!"
        break
        fi
    done

    echo "[INFO] Execute response is..."
    cat $status_file
    echo ""

    echo "[INFO] Getting metalink content..."
    url=$(grep "input.meta4" $status_file | cut -d\" -f2)
    metalink_file=${requestid}.metalink.txt
    check_url $url $metalink_file

    echo "[INFO] Metalink response is..."
    cat $metalink_file

    if [ ! "$skipdownload" ]; then

        echo "[INFO] Downloading and checking netCDF file..."
        nc_url=$(grep "metaurl" $metalink_file | head -1 | cut -d\> -f2 | cut -d\< -f1)
        nc_file=${requestid}.netcdf.nc
        check_url $nc_url $nc_file

        ncdump -h $nc_file | head -15

        if [ $? -ne 0 ]; then
            echo "[ERROR] FAILED request $requestid when ncdumping: $nc_file"
            exit
        fi

    else
        echo "[INFO] Skipping netcdf download as requested."
    fi

    echo "[INFO] SUCCEEDED!"

}

echo "[INFO] Testing capabilities..."
url="${prefix}=getcapabilities"
check_url $url out.capabilities.txt

echo "[INFO] Testing describe process: subset..."
url="${prefix}=describeprocess&identifier=subset"
check_url $url out.describe.txt


datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619;time=2020-01-01/2020-12-30"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=1
run_request $url $requestid

datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619;time=2015-01-16T12:00:00/2100-12-16T12:00:00"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=2
run_request $url $requestid true

if [ ! "$(grep "data.mips.copernicus-climate.eu" ${requestid}.metalink.txt)" ]; then 
    echo "[ERROR] Request $requestid failed to identify original files on the Data Node."
    echo "        URL is: $url"
    exit
else
    echo "[INFO] Request $requestid: SUCCESS!"
fi

datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619;time=1900-01-01/2500-12-30"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=3
run_request $url $requestid true

if [ ! "$(grep "data.mips.copernicus-climate.eu" ${requestid}.metalink.txt)" ]; then 
    echo "[ERROR] Request $requestid failed to identify original files on the Data Node."
    echo "        URL is: $url"
    exit
else
    echo "[INFO] Request $requestid: SUCCESS!"
fi

datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=4
run_request $url $requestid true

if [ ! "$(grep "data.mips.copernicus-climate.eu" ${requestid}.metalink.txt)" ]; then 
    echo "[ERROR] Request $requestid failed to identify original files on the Data Node."
    echo "        URL is: $url"
    exit
else
    echo "[INFO] Request $requestid: SUCCESS!"
fi

time_area="time=2020-01-01/2020-12-30;area=10,10,40,40"
datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619;${time_area}"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=5
run_request $url $requestid 

time_area="time=2020-01-01/2020-12-30;area=-50,-50,-10,-10"
datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619;${time_area}"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=6
run_request $url $requestid

time_area="time=2020-01-01/2020-12-30;area=-50,-50,50,50"
datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619;${time_area}"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=7
run_request $url $requestid

time_area="time=2020-01-01/2020-12-30;area=-200,40,-50,80"
datainputs="collection=c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619;${time_area}"
url="${prefix}=Execute&identifier=subset&status=true&storeExecuteResponse=true&DataInputs=${datainputs}"
requestid=8
run_request $url $requestid


