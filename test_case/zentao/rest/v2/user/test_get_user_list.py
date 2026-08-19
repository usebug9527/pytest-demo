import logging

import allure

from rest.v2.module.user.user import User

LOG = logging.getLogger(__name__)

class TestGetUserList:

    @allure.epic('zentao')
    @allure.feature('User')
    @allure.story('get')
    @allure.title('get user')
    @allure.description('获取用户列表')
    def test_get_user_list(self, rest):
        user_list = User.get_user_list(rest)
        LOG.info(f"user_list:{[u.id for u in user_list]}")
        print("test_create_account")