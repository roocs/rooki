# -*- coding: utf-8 -*-

"""Top-level package for rooki."""

from birdy import WPSClient
from rooki import config


import logging

__all__ = [
    'rooki',
    'output',
    'open_dataset',
]

rooki = WPSClient(config.get_config_value('service', 'url'), verify=False, progress=True)
rooki.logger.setLevel(logging.ERROR)
rooki._notebook = False


def output(response):
    return response.get()[0]


def open_dataset(response):
    return response.get(asobj=True)[0]
