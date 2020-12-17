from rooki import operators as ops


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


def test_workflow_serialize_json():
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
