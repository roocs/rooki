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
        collection="CMIP6.CMIP.IPSL.IPSL-CM6A-LR.historical.r1i1p1f1.Amon.rlds.gr.v20180803",
        time="1860-01-01/1900-12-30",
    )
    assert resp.ok is True
    assert resp.num_files == 1
    assert len(resp.download_urls()) == 1
    assert resp.size > 50000
    assert resp.size_in_mb > 0.0
    assert resp.size_in_gb > 0.0
    assert len(resp.download()) == 1
    assert len(resp.datasets()) == 1
    out_file = resp.download()[0]
    assert out_file.startswith("/tmp/rooki/metalink_")
    assert out_file.endswith(
        "rlds_Amon_IPSL-CM6A-LR_historical_r1i1p1f1_gr_18600116-19001216.nc"
    )
