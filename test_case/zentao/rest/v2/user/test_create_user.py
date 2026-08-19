from rest.v2.common.rest_api import RestApi
from rest.v2.module.user.user import User
import logging

LOG = logging.getLogger(__name__)


class TestCreateUser:

    def test_create_account(self, rest, case_data):
        user = User.create_user(rest, case_data['account'], case_data['realname'], case_data['password'], )
        if isinstance(user, User):
            LOG.info(f"user id:{user.id}")
            assert user.id
        else:
            LOG.error(f"rsp:{user}")


    # def test_edit_account(self, request):
    #     print("test_edit_account")
    #     print(f"request scope: {request.scope}")
    #     print(f"request node: {request.node}")
    #     print(f"request node.name: {request.node.name}")
    #     print(f"request node.module.__file__: {request.node.module.__file__}")
    #     print(f"request node.cls: {request.node.cls}")
