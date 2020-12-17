import pytest

from rooki import operators as ops


@pytest.mark.online
def test_workflow_subset_chain():
    wf = ops.Subset(
        ops.Subset(
            ops.Input(
                'tas', ['c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest']
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
    assert out_file.startswith('/tmp/rooki/metalink_')
    assert out_file.endswith('tas_day_EC-EARTH_historical_r1i1p1_18800101-19001229.nc')


def test_workflow_serialize():
    wf = ops.Subset(
        ops.Subset(
            ops.Input(
                'tas', ['c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest']
            ),
            time="1860-01-01/1920-12-30",
        ),
        time="1880-01-01/1900-12-30",
    )
    assert wf._serialise() == '{"inputs": {"tas": ["c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest"]}, "steps": {"subset_tas_1": {"run": "subset", "in": {"collection": "inputs/tas", "time": "1860-01-01/1920-12-30"}}, "subset_tas_2": {"run": "subset", "in": {"collection": "subset_tas_1/output", "time": "1880-01-01/1900-12-30"}}}, "outputs": {"output": "subset_tas_2/output"}, "doc": "workflow"}'  # noqa


def test_workflow_compare_serialize():
    # wf tree
    wf_a = ops.Subset(
        ops.Subset(
            ops.Input(
                'tas', ['c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest']
            ),
            time="1860-01-01/1920-12-30",
        ),
        time="1880-01-01/1900-12-30",
    )
    # wf simple
    wf_b = ops.Input('tas', ['c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest'])
    wf_b = ops.Subset(wf_b, time='1860-01-01/1920-12-30')
    wf_b = ops.Subset(wf_b, time='1880-01-01/1900-12-30')
    assert wf_a._serialise() == wf_b._serialise()
