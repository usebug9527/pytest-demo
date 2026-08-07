from api.rest.v2.common.base.module_base import Base

class Token(Base):
    def __init__(self, account, password):
        super().__init__()
        self.__token__ = None
        self.__account__ = account
        self.__password__ = password
        self.__request_type__ = "POST"

    @staticmethod
    def get_token():
        return Token().__token__

