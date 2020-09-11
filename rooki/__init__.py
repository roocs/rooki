# -*- coding: utf-8 -*-

"""Top-level package for rooki."""

from birdy import WPSClient
from owslib.wps import ASYNC, SYNC
from rooki import config
from rooki.results import Result


import logging

__all__ = [
    'rooki',
    'Result',
]


class Rooki(object):
    def __init__(self, url=None, mode=None, verify=True):
        mode = mode or ASYNC
        url = url or config.get_config_value('service', 'url')
        progress = mode == ASYNC
        self.client = WPSClient(url, verify=verify, progress=progress)
        self.client.logger.setLevel(logging.ERROR)
        self.client._notebook = False


rooki = Rooki(verify=False).client
