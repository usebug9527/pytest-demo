from architecture.api.rest.v2.common.api_rest import RestApi

class Base:
    def __init__(self):
        self.api_rest = RestApi()
