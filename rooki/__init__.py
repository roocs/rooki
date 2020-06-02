# -*- coding: utf-8 -*-

"""Top-level package for rooki."""

__author__ = """Carsten Ehbrecht"""
__contact__ = "ehbrecht@dkrz.de"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__version__ = "0.1.0"

from birdy import WPSClient
from rooki import config
rooki = WPSClient(config.get_config_value('service', 'url'), verify=False)
