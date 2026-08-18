from rest.v2.common.rest_api import RestApi
from rest.v2.module.user.user import User
import logging

LOG = logging.getLogger(__name__)


class TestUser:

    def test_create_account(self, init_token, case_params):
        api = init_token
        user_list = User.get_user_list(api)
        LOG.info(f"user_list:{user_list}")
        for user in user_list:
            LOG.info(f"user:{user.id}")
        print("test_create_account")

    # def test_edit_account(self, request):
    #     print("test_edit_account")
    #     print(f"request scope: {request.scope}")
    #     print(f"request node: {request.node}")
    #     print(f"request node.name: {request.node.name}")
    #     print(f"request node.module.__file__: {request.node.module.__file__}")
    #     print(f"request node.cls: {request.node.cls}")
