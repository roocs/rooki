from birdy import WPSClient
from owslib.wps import ASYNC
from rooki import config
from rooki.results import Result


import logging


class Rooki(WPSClient):
    def __init__(self, url=None, mode=None, verify=True):
        mode = mode or ASYNC
        url = url or config.get_config_value('service', 'url')
        progress = mode == ASYNC
        super(Rooki, self).__init__(url, verify=verify, progress=progress)
        self.logger.setLevel(logging.ERROR)
        self._notebook = False

    def _execute(self, pid, **kwargs):
        resp = super(Rooki, self)._execute(pid, **kwargs)
        return Result(resp)


rooki = Rooki(verify=False)
