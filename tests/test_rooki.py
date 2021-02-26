#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rooki` package."""

import pytest
import requests

from .common import ROOK_URL


def test_rooki_settings(rooki):
    assert rooki.url == ROOK_URL
    assert rooki.mode == "async"
    assert rooki.verify is False
    assert rooki.output_dir == "/tmp/rooki"


@pytest.mark.online
def test_rooki_subset(rooki):
    resp = rooki.subset(
        collection="c3s-cmip6.ScenarioMIP.INM.INM-CM5-0.ssp245.r1i1p1f1.Amon.rlds.gr1.v20190619",
        time="2020-01-01/2020-12-31",
    )
    assert resp.ok is True
    assert resp.num_files == 1
    assert len(resp.download_urls()) == 1
    assert resp.size > 0.0
    assert resp.size_in_mb > 0.0
    assert resp.size_in_gb > 0.0
    assert len(resp.download()) == 1
    assert len(resp.datasets()) == 1
    out_file = resp.download()[0]
    assert out_file.startswith("/tmp/rooki/metalink_")
    assert out_file.endswith(
        "rlds_Amon_INM-CM5-0_ssp245_r1i1p1f1_gr1_20200116-20201216.nc"
    )


def test_rooki_errors_connection():
    from rooki.client import Rooki

    with pytest.raises(requests.exceptions.ConnectionError):
        Rooki(url="http://not.available")


@pytest.mark.online
def test_rooki_errors_not_avail_op(rooki):
    with pytest.raises(AttributeError):
        rooki.not_availble_operator()


@pytest.mark.online
@pytest.mark.xfail(reason="XFAIL at service provider site, otherwise XPASS")
def test_rooki_errors_access_denied():
    from rooki.client import Rooki

    rooki = Rooki(url="http://compute.mips.copernicus-climate.eu/wps")
    with pytest.raises(RuntimeError):
        rooki.subset(
            collection="c3s-cmip6.CMIP.IPSL.IPSL-CM6A-LR.historical.r1i1p1f1.Amon.rlds.gr.v20180803",
        )
