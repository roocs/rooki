import os
import tempfile

from birdy import WPSClient
from owslib.wps import ASYNC
from rooki import config
from rooki.results import Result


import logging


class Rooki(WPSClient):
    def __init__(
        self,
        url=None,
        mode=None,
        verify=None,
        output_dir=None,
        headers=None,
        lineage=True,
    ):
        self._url = url or os.environ.get(
            "ROOK_URL", config.get_config_value("service", "url")
        )
        self._mode = mode or os.environ.get(
            "ROOK_MODE", config.get_config_value("service", "mode")
        )
        if verify is None:
            self._verify = os.environ.get(
                "ROOK_SSL_VERIFY", config.get_config_value("service", "ssl_verify")
            )
        else:
            self._verify = verify
        self._output_dir = output_dir or os.environ.get(
            "ROOKI_OUTPUT_DIR", config.get_config_value("service", "output_dir")
        )
        progress = self.mode == ASYNC
        if "ACCESS_TOKEN" in os.environ:
            access_token = os.environ["ACCESS_TOKEN"]
            if headers is None:
                headers = {}
            headers["Authorization"] = f"Bearer {access_token}"
        super(Rooki, self).__init__(
            self._url,
            verify=self._verify,
            progress=progress,
            headers=headers,
            lineage=lineage,
        )
        self._notebook = False
        self.logger = logging.getLogger("rooki")
        self.logger.addHandler(logging.NullHandler())

    def cancel(self):
        # https://github.com/roocs/rook/issues/143
        self.logger.warn("cancel was called but is not available.")

    @property
    def url(self):
        return self._url

    @property
    def mode(self):
        return self._mode

    @property
    def verify(self):
        return self._verify

    @property
    def output_dir(self):
        if not self._output_dir:
            self._output_dir = tempfile.gettempdir()
        elif not os.path.isdir(self._output_dir):
            os.makedirs(self._output_dir)
        return self._output_dir

    def _execute(self, pid, **kwargs):
        try:
            resp = super(Rooki, self)._execute(pid, **kwargs)
        except Exception:
            raise RuntimeError("execution failed")
        return Result(resp, output_dir=self.output_dir)
