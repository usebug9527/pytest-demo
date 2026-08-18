from architecture.api.rest.v2.common.base.module_base import Base
from rest.v2.common.rest_api import RestApi


class Token(Base):
    def __init__(self, token:str = ""):
        super().__init__()
        self.token = token

    @staticmethod
    def get_token(r: RestApi, account: str, password: str):
        rsp = r.send(url="/users/login", method="POST",account=account, password=password)
        if rsp.json()['status'] == 'success':
            return Token(
                token = rsp.json()['token']
            )
        return rsp