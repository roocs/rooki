from birdy import WPSClient
from owslib.wps import ASYNC
from rooki import config
from rooki.results import Result


import logging


class Rooki(WPSClient):
    def __init__(self, url=None, mode=None, verify=None):
        self._url = url or config.get_config_value("service", "url")
        self._mode = mode or config.get_config_value("service", "mode")
        if verify is None:
            self._verify = config.get_config_value("service", "ssl_verify")
        else:
            self._verify = verify
        progress = self.mode == ASYNC
        super(Rooki, self).__init__(self._url, verify=self._verify, progress=progress)
        self._notebook = False
        self.logger = logging.getLogger("rooki")
        self.logger.addHandler(logging.NullHandler())

    @property
    def url(self):
        return self._url

    @property
    def mode(self):
        return self._mode

    @property
    def verify(self):
        return self._verify

    def _execute(self, pid, **kwargs):
        resp = super(Rooki, self)._execute(pid, **kwargs)
        return Result(resp)


rooki = Rooki()
