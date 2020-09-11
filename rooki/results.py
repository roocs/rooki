import requests


class Result(object):
    def __init__(self, response):
        self.response = response

    @property
    def url(self):
        return self.response.get()[0]

    @property
    def xml(self):
        xml = requests.get(self.url).text
        return xml

    def download_urls(self):
        return []

    def datasets(self):
        return self.response.get(asobj=True)[0]
