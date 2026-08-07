import requests


class Api:

    def __init__(self):
        self.headers = {}
        self.session = requests.Session()

    def post(self, url, **kwargs):
        return self.session.post(url)