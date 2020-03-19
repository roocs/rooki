# -*- coding: utf-8 -*-

"""Top-level package for rooki."""

__author__ = """Carsten Ehbrecht"""
__contact__ = "ehbrecht@dkrz.de"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__version__ = "0.1.0"

from birdy import WPSClient
url = 'https://bovec.dkrz.de/ows/proxy/roocs'
# url = 'http://localhost:5000/wps'
rooki = WPSClient(url, verify=False)
