class Result(object):
    def __init__(self, response):
        self.response = response

    def reference(self):
        return self.response.get()[0]

    def download_urls(self):
        return []

    def datasets(self):
        return self.response.get(asobj=True)[0]
