import json

import pytest

from rooki import operators as ops

WF_EXAMPLE = {
    "inputs": {
        "rlds": [
            "CMIP6.CMIP.IPSL.IPSL-CM6A-LR.historical.r1i1p1f1.Amon.rlds.gr.v20180803"
        ]
    },
    "steps": {
        "subset_rlds_1": {
            "run": "subset",
            "in": {"collection": "inputs/rlds", "time": "1860-01-01/1920-12-30"},
        },
        "subset_rlds_2": {
            "run": "subset",
            "in": {
                "collection": "subset_rlds_1/output",
                "time": "1880-01-01/1900-12-30",
            },
        },
    },
    "outputs": {"output": "subset_rlds_2/output"},
    "doc": "workflow",
}


@pytest.mark.online
#@pytest.mark.xfail(reason="online wps not always available")
@pytest.mark.skip(reason="needs to be fixed")
def test_workflow_subset_chain():
    wf = ops.Subset(
        ops.Subset(
            ops.Input(
                "rlds",
                [
                    "CMIP6.CMIP.IPSL.IPSL-CM6A-LR.historical.r1i1p1f1.Amon.rlds.gr.v20180803"
                ],
            ),
            time="1860-01-01/1920-12-30",
        ),
        time="1880-01-01/1900-12-30",
    )
    resp = wf.orchestrate()
    assert resp.ok is True
    assert len(resp.download_urls()) == 1
    assert len(resp.download()) == 1
    out_file = resp.download()[0]
    # assert out_file.startswith('/tmp/rooki/metalink_')
    assert out_file.endswith(
        "rlds_Amon_IPSL-CM6A-LR_historical_r1i1p1f1_gr_18800116-19001216.nc"
    )


def test_workflow_serialize():
    wf = ops.Subset(
        ops.Subset(
            ops.Input(
                "rlds",
                [
                    "CMIP6.CMIP.IPSL.IPSL-CM6A-LR.historical.r1i1p1f1.Amon.rlds.gr.v20180803"
                ],
            ),
            time="1860-01-01/1920-12-30",
        ),
        time="1880-01-01/1900-12-30",
    )
    assert json.loads(wf._serialise()) == WF_EXAMPLE


def test_workflow_compare_serialize():
    # wf tree
    wf_a = ops.Subset(
        ops.Subset(
            ops.Input(
                "rlds",
                [
                    "CMIP6.CMIP.IPSL.IPSL-CM6A-LR.historical.r1i1p1f1.Amon.rlds.gr.v20180803"
                ],
            ),
            time="1860-01-01/1920-12-30",
        ),
        time="1880-01-01/1900-12-30",
    )
    # wf simple
    wf_b = ops.Input(
        "rlds",
        ["CMIP6.CMIP.IPSL.IPSL-CM6A-LR.historical.r1i1p1f1.Amon.rlds.gr.v20180803"],
    )
    wf_b = ops.Subset(wf_b, time="1860-01-01/1920-12-30")
    wf_b = ops.Subset(wf_b, time="1880-01-01/1900-12-30")
    assert wf_a._serialise() == wf_b._serialise()
