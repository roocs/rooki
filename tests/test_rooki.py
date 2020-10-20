#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rooki` package."""

from .common import ROOK_URL


def test_rooki_settings(rooki):
    assert rooki.url == ROOK_URL
    assert rooki.mode == 'async'
    assert rooki.verify is False


def test_rooki_subset(rooki):
    resp = rooki.subset(
        collection='c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest',
        time='1860-01-01/1900-12-30')
    assert resp.ok is True
    assert resp.num_files == 1
    assert len(resp.download_urls()) == 1
    assert resp.size > 1000000
    assert resp.size_in_mb > 1.0
    assert resp.size_in_gb > 0.0
    assert len(resp.download()) == 1
    assert len(resp.datasets()) == 1
