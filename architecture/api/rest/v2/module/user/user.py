import logging


from architecture.api.rest.v2.common.base.module_base import Base
from architecture.api.rest.v2.common.rest_api import RestApi
from typing import Optional, Any

DEFAULT_TIMEOUT = (3, 10)

LOG = logging.getLogger(__name__)

class User(Base):
    id: Optional[str] = None  # 用户编号
    company: Optional[str] = None  # 所属公司
    type: Optional[str] = None  # 用户类型
    dept: Optional[str] = None  # 部门
    account: Optional[str] = None  # 用户名
    role: Optional[str] = None  # 职位
    realname: Optional[str] = None  # 姓名
    superior: Optional[str] = None
    pinyin: Optional[str] = None
    nickname: Optional[str] = None  # 昵称
    commiter: Optional[str] = None  # 源代码帐号
    avatar: Optional[str] = None  # 用户头像
    birthday: Optional[str] = None  # 生日
    gender: Optional[str] = None  # 性别
    email: Optional[str] = None  # 邮箱
    skype: Optional[str] = None  # Skype
    qq: Optional[str] = None  # QQ
    mobile: Optional[str] = None  # 手机
    phone: Optional[str] = None  # 电话
    weixin: Optional[str] = None  # 微信
    dingding: Optional[str] = None  # 钉钉
    slack: Optional[str] = None  # Slack
    whatsapp: Optional[str] = None  # WhatsApp
    address: Optional[str] = None  # 通讯地址
    zipcode: Optional[str] = None  # 邮编
    nature: Optional[str] = None  # 性格特征
    analysis: Optional[str] = None  # 影响分析
    strategy: Optional[str] = None  # 应对策略
    join: Optional[str] = None  # 入职日期
    visits: Optional[str] = None  # 访问次数
    visions: Optional[str] = None  # 界面类型
    ip: Optional[str] = None  # 最后IP
    last: Optional[str] = None  # 最后登录
    fails: Optional[str] = None  # 失败次数
    locked: Optional[str] = None  # 锁住日期
    feedback: Optional[str] = None
    ranzhi: Optional[str] = None  # ZDOO帐号
    ldap: Optional[str] = None
    score: Optional[str] = None  # 积分
    scoreLevel: Optional[str] = None  # 积分等级
    resetToken: Optional[str] = None
    resetExpired: Optional[str] = None
    clientStatus: Optional[str] = None  # 登录状态
    clientLang: Optional[str] = None  # 客户端语言
    jira: Optional[str] = None
    deleted: Optional[str] = None  # (已删除)

    def __init__(self):
        super().__init__()
        # LOG.info(f"User init...")

    @staticmethod
    def create_user(r: RestApi,
                    account: str,
                    realname: str,
                    password: str,
                    timeout: Any = DEFAULT_TIMEOUT, ):
        """
        名称	类型	必填	描述
        account	string	是	登录名
        realname	string	是	姓名
        password	string	是	密码
        :return:
        {
            "status": "success",
            "id": 2
        }
        """
        rsp = r.send('/users', method="POST", timeout=timeout,
                     account=account,
                     realname=realname,
                     password=password,
                     )
        if rsp.json()['status'] == 'success':
            user = User()
            user.__setattr__('id', rsp.json()['id'])
            return user
        return rsp

    @staticmethod
    def get_user_list(r: RestApi,
                      browseType: str = '',
                      orderBy: str = '',
                      recPerPage: str = '',
                      pageID: str = '',
                      timeout: Any = DEFAULT_TIMEOUT):
        """
        名称	类型	必填	描述
        browseType	String	否	内部用户 inside | 内部用户 outside
        orderBy	String	否	排序(id_asc | realname_asc 姓名 | account_asc 用户名)，倒序使用id_desc, realname_desc, account_desc
        recPerPage	String	否	每页数量，不超过1000
        pageID	String	否	页码，从第1页开始
        :return:
        {
        "status": "success",
        "users": [{user},{user}]
        }
        """
        rsp = r.send('/users', method="GET", timeout=timeout,
                     browseType=browseType,
                     orderBy=orderBy,
                     recPerPage=recPerPage,
                     pageID=pageID,
                     )
        if rsp.json()['status'] == 'success':
            user_list = []
            for user in rsp.json()['users']:
                us = User()
                for k, v in user.items():
                    us.__setattr__(k, v)
                user_list.append(us)
            return user_list

        return rsp

    @staticmethod
    def edit_user_by_id(r: RestApi, userID: Any,
                        realname: str = '',
                        dept: str = '',
                        join: str = '',
                        group: str = '',
                        email: str = '',
                        visions: str = '',
                        mobile: str = '',
                        weixin: str = '',
                        password: str = '',
                        timeout: Any = DEFAULT_TIMEOUT):
        """
        名称	类型	必填	描述
        realname	string	否	真实姓名
        dept	int	否	部门
        join	date	否	入职日期
        group	array	否	权限分组
        email	string	否	邮箱
        visions	array	否	界面类型(研发综合界面 rnd | 运营管理界面 lite)
        mobile	string	否	手机
        weixin	string	否	微信
        password	string	否	密码
        :return:
        {
            "status": "success"
        }
        """
        try:
            rsp = r.send(f'/users/{int(userID)}', method="PUT", timeout=timeout,
                         realname=realname,
                         dept=dept,
                         join=join,
                         group=group,
                         email=email,
                         visions=visions,
                         mobile=mobile,
                         weixin=weixin,
                         password=password,
                         )
            if rsp.json()['status'] == 'success':
                us = User()
                for k, v in rsp.json()['user'].items():
                    us.__setattr__(k, v)
                return us
            return rsp
        except ValueError:
            return None

    @staticmethod
    def delete_users_by_id(r: RestApi, userID:Any, timeout: Any = DEFAULT_TIMEOUT):
        """
        :param userID:用户ID
        :return:
        {
            "status": "success"
        }
        """
        try:
            return r.send(f'/users/{int(userID)}', method="DELETE", timeout=timeout)
        except ValueError:
            return None

    @staticmethod
    def get_user_by_id(r: RestApi, userID:Any, timeout=DEFAULT_TIMEOUT):
        """
        名称	类型	必填	描述
        realname	string	否	真实姓名
        dept	int	否	部门
        join	date	否	入职日期
        group	array	否	权限分组
        email	string	否	邮箱
        visions	array	否	界面类型(研发综合界面 rnd | 运营管理界面 lite)
        mobile	string	否	手机
        weixin	string	否	微信
        password	string	否	密码
        :param userID: 用户ID
        :return:
        {
        "status": "success",
        "user": {user}
        }
        """
        try:
            rsp = r.send(f'/users/{int(userID)}', method="GET", timeout=timeout)
            if rsp.json()['status'] == 'success':
                us = User()
                for k, v in rsp.json()['user'].items():
                    us.__setattr__(k, v)
                return us
            return rsp
        except ValueError:
            return None

# if __name__ == '__main__':
#     rest = RestApi(account='admin', password='Aa123456')
#     print(rest.session.request(url='http://127.0.0.1/zentao/api.php/v2/users',method="GET").json())
#     # print(rest.send(url='/users', method="GET",body={}).json())
