import logging

from rest.v2.module.user.user import User

LOG = logging.getLogger(__name__)

class TestGetUserList:

    def test_get_user_list(self, rest):
        user_list = User.get_user_list(rest)
        LOG.info(f"user_list:{user_list}")
        for user in user_list:
            LOG.info(f"user:{user.id}")
        print("test_create_account")