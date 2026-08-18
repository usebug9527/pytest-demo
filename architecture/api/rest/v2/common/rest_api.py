import logging
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from architecture.api.rest.v2.common.api_v2 import ApiV2
from architecture.api.rest.v2.utils.url_utils import UrlUtils

DEFAULT_TIMEOUT = (3, 10)
logger = logging.getLogger(__name__)

class RestApi(ApiV2):
    def __init__(self):
        logger.info(f"RestApi init...")
        super().__init__()
        self.session = requests.Session()
        # 配置连接池+自动重试，解决网络抖动超时
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504]
        )
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=10,
            pool_maxsize=100
        )
        # 统一默认请求头，避免登录后丢失json标识
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "rest-api-client/1.0"
        })
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def set_token(self, token:str):
        print(f"set_token: {token}; self.headers: {self.headers}")
        self.session.headers.update({
            'token': token
        }
        )

    def send(self, url: str, method: str, timeout=DEFAULT_TIMEOUT, **kwargs):
        # 修复循环覆盖body的bug，只支持单接口调用（当前业务场景）
        full_url = UrlUtils.join_path(self.base_url, url)
        print(full_url)
        try:
            rsp = self.session.request(
                method=method,
                url=full_url,
                json=self.parse_kwargs(**kwargs),
                timeout=timeout,
                # HTTPS环境放开注释关闭证书校验
                # verify=False
            )
            # print(rsp.text)
            rsp.raise_for_status()
            return rsp
        except requests.exceptions.ConnectTimeout:
            raise Exception(f"连接接口超时，url={full_url}")
        except requests.exceptions.ReadTimeout:
            raise Exception(f"读取接口响应超时，url={full_url}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"接口请求异常: {str(e)}") from e

    def parse_kwargs(self, **kwargs) -> dict:
        dic = {}
        for k,v in kwargs.items():
            dic[k] = v
        return dic


#
# if __name__ == '__main__':
#     rest = RestApi(account="admin", password="Aa123456")
#     resp = rest.send("/users", method="GET", body={"browseType": "inside"})
#     print(resp.text)
#     # session = requests.session()
#     # rsp0 = session.request(method="POST",url="http://127.0.0.1/zentao/api.php/v2/users/login", json={"account": "admin", "password": "Aa123456"})
#     # print(rsp0.text)
#     # rsp = session.get("http://127.0.0.1/zentao/api.php/v2/users", json={"browseType": "outside"})
#     # print(rsp.text)
#     pass
