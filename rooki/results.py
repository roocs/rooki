import tempfile
import requests
from bs4 import BeautifulSoup


class Result(object):
    def __init__(self, response, outdir=None, verify=False):
        self.response = response
        self.outdir = outdir or tempfile.mkdtemp()
        self.verify = verify
        # cache
        self._xml = None
        self._doc = None
        self._size = None
        self._num_files = None

    @property
    def ok(self):
        return self.response.isSucceded()

    @property
    def status(self):
        if self.ok:
            status = self.response.status
        else:
            status = '; '.join([error.text.strip() for error in self.response.errors])
        return status

    @property
    def url(self):
        return self.response.get()[0]

    @property
    def xml(self):
        if not self._xml:
            self._xml = requests.get(self.url, verify=self.verify).text
        return self._xml

    @property
    def doc(self):
        if not self._doc:
            self._doc = BeautifulSoup(self.xml, 'xml')
        return self._doc

    @property
    def size(self):
        if self._size is None:
            total_size = 0
            for size in self.doc.find_all('size'):
                total_size += int(size.text)
            self._size = f"{total_size} bytes"
        return self._size

    @property
    def num_files(self):
        if self._num_files is None:
            self._num_files = len(self.doc.find_all('file'))
        return self._num_files

    def download_urls(self):
        return [url.text for url in self.doc.find_all('metaurl')]

    def files(self):
        try:
            import metalink.download
            files = metalink.download.get(self.url, self.outdir, segmented=False)
        except Exception:
            files = []
        return files

    def datasets(self):
        try:
            import xarray as xr
            datasets = [xr.open_dataset(file) for file in self.files()]
        except Exception:
            datasets = []
        return datasets

    def __str__(self):
        if self.ok:
            msg = f"Metalink URL: {self.url}, size: {self.size}, num files: {self.num_files}"
        else:
            msg = self.status
        return msg

    def __repr__(self):
        return self.__str__()
