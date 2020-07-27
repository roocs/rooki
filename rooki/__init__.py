# -*- coding: utf-8 -*-

"""Top-level package for rooki."""

from birdy import WPSClient
from rooki import config
rooki = WPSClient(config.get_config_value('service', 'url'), verify=False)
