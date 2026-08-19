# from rest.v2.common.rest_api import RestApi
# import logging
# LOG = logging.getLogger(__name__)


class TestToken:
    pass

    # def test_get_token_1(self, case_params):
    #     self.api = RestApi(account=case_params['account'], password=case_params['password'])
    #     LOG.info(f"token: {self.api.session.headers.get('token', '')}")
    #     assert self.api.session.headers.get('token', '')
    #     headers = self.api.session.headers
    #     LOG.info(f"headers: {headers}")
    #     self.api = RestApi()
    #     rsp = self.api.send(url='users/login', method="POST", account=case_params['account'],password=case_params['password'])
    #     LOG.info(f"rsp: {rsp}")
    #     print("test_get_token")