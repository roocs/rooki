#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rooki` package."""

import pytest

from .common import ROOK_URL


def test_rooki_settings(rooki):
    assert rooki.url == ROOK_URL
    assert rooki.mode == "async"
    assert rooki.verify is False
    assert rooki.output_dir == "/tmp/rooki"


@pytest.mark.online
def test_rooki_subset(rooki):
    resp = rooki.subset(
        collection="c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest",
        time="1860-01-01/1900-12-30",
    )
    assert resp.ok is True
    assert resp.num_files == 1
    assert len(resp.download_urls()) == 1
    assert resp.size > 1000000
    assert resp.size_in_mb > 1.0
    assert resp.size_in_gb > 0.0
    assert len(resp.download()) == 1
    assert len(resp.datasets()) == 1
    out_file = resp.download()[0]
    assert out_file.startswith("/tmp/rooki/metalink_")
    assert out_file.endswith("tas_day_EC-EARTH_historical_r1i1p1_18600101-19001229.nc")
