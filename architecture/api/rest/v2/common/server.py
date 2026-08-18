from architecture.api.rest.v2.utils.url_utils import UrlUtils
from architecture.api.rest.v2.utils.yaml_parser import YamlParser


class Server:
    def __init__(self):
        sv = YamlParser().get_test_bed()['zentao']['server']
        self.protocol = sv['protocol']
        self.host = sv['host']
        self.port = sv['port']
        self.base_url = sv['baseUrl']
        self.admin = {
            "account": sv['account']['username'],
            "password": sv['account']['password'],
        }

    def get_base_url(self):
        return UrlUtils.join_path(f"{self.protocol}://{self.host}:{self.port}", f"{self.base_url}")

    def get_account(self):
        return self.admin

    def get_protocol(self):
        return self.protocol

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port
