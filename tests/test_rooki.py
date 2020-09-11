#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rooki` package."""

__author__ = """Carsten Ehbrecht"""
__contact__ = 'ehbrecht@dkrz.de'
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


import pytest

from click.testing import CliRunner

# from rooki import rooki


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
