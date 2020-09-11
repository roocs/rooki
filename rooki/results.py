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
        total_size = 0
        for size in self.doc.find_all('size'):
            total_size += int(size.text)
        return f"{total_size} bytes"

    @property
    def num_files(self):
        return len(self.doc.find_all('file'))

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
        return f"Metalink URL: {self.url}"

    def __repr__(self):
        return self.__str__()
