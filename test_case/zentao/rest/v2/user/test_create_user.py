import allure
import pytest
from pytest_html import fixtures

from rest.v2.common.rest_api import RestApi
from rest.v2.db.common.database import Database
from rest.v2.module.user.user import User
import logging

LOG = logging.getLogger(__name__)


class TestCreateUser:
    @pytest.fixture(scope='function', autouse=True)
    def fixture(self,rest, case_data):
        LOG.info(f'case_data: {case_data}')
        res = Database().query("select id from zt_user where account=%s or realname=%s",
                               (case_data['account'], case_data['realname']))
        LOG.info(f"res:{res[0]}")
        rsp = User.delete_users_by_id(rest,res[0]['id'])
        LOG.info(f"rsp:{rsp}")
        assert rsp['status'] == 'success' or "User does not exist" in rsp['message']
        yield
        LOG.info("yield")


    @allure.epic('zentao')
    @allure.feature('User')
    @allure.story('create')
    @allure.title('create user')
    @allure.description('正常创建用户')
    def test_create_account(self, rest, case_data):
        user = User.create_user(rest, case_data['account'], case_data['realname'], case_data['password'], )
        if isinstance(user, User):
            LOG.info(f"user id:{user.id}")
            assert user.id
        else:
            LOG.error(f"rsp:{user}")
            assert user and False
    # def test_edit_account(self, request):
    #     print("test_edit_account")
    #     print(f"request scope: {request.scope}")
    #     print(f"request node: {request.node}")
    #     print(f"request node.name: {request.node.name}")
    #     print(f"request node.module.__file__: {request.node.module.__file__}")
    #     print(f"request node.cls: {request.node.cls}")
