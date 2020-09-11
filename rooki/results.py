import tempfile
import requests
from bs4 import BeautifulSoup


class Result(object):
    def __init__(self, response, outdir=None, verify=False):
        self.response = response
        self.outdir = outdir or tempfile.mkdtemp()
        self.verify = verify

    @property
    def url(self):
        return self.response.get()[0]

    @property
    def xml(self):
        return requests.get(self.url, verify=self.verify).text

    @property
    def doc(self):
        return BeautifulSoup(self.xml)

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
