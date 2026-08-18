import logging
from datetime import datetime

import pytest
from pathlib import Path

from architecture.api.rest.v2.utils.yaml_parser import YamlParser
from rest.v2.common.rest_api import RestApi
from rest.v2.common.server import Server
from rest.v2.module.token.token import Token

# 定义yaml用例配置文件路径，与conftest.py同级目录
TEST_SET_CONFIG = Path(__file__).parent / "test_set.yml"

print(f"TEST_SET_CONFIG: {TEST_SET_CONFIG}")
def pytest_configure(config):
    """pytest启动的时候执行，初始化日志"""
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)

    # Windows文件名禁止冒号，时分秒用下划线
    time_str = datetime.now().strftime("%Y‑%m‑%d_%H_%M_%S")
    log_file = log_dir / f"{time_str}.log"

    # 日志格式
    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s:%(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y‑%m‑%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf‑8")
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(fmt)
    console_handler.setLevel(logging.INFO)

    root_logger = logging.getLogger()
    # 防止重复添加handler，多次执行pytest重复打印日志
    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)
    root_logger.setLevel(logging.DEBUG)

def load_set_config():
    """
    解析yaml配置文件，构建【测试文件名标识+测试函数名】与接口入参的映射字典
    返回格式：{(文件标识, 测试函数名): 请求参数字典}
    示例：{("token", "test_get_token"): {"account": "admin", "password": "Aa123456"}}
    """
    # 打开yaml文件，utf-8编码避免中文乱码
    data = YamlParser().parse(TEST_SET_CONFIG)
    # 获取yaml顶层testcase节点下所有文件分组（token、user）
    testcase = data.get("testcase", {})

    return testcase


# 程序启动时一次性加载所有用例配置，全局复用，无需重复读取文件
CASE_CONFIG_MAP = load_set_config()
print(f"CASE_CONFIG_MAP: {CASE_CONFIG_MAP}")

@pytest.fixture(scope='session' ,autouse=True)
def init_token():
    r = RestApi()
    sv = Server()
    t = Token().get_token(r, sv.get_account().get("account"), sv.get_account().get("password"))
    r.set_token(token=t.token)
    return r
    # yield
    # r.session.close()
    # print(f" yield init_token: {r.session.headers}")




@pytest.fixture(autouse=True)
def case_params(request):
    """
    自动执行fixture（所有用例运行前都会触发）
    1. 以当前测试文件名称作为匹配标识，匹配yaml对应分组，注入参数
    2. 未在yaml配置中的用例直接跳过执行
    :param request: pytest内置对象，可获取当前执行用例的模块、函数信息
    :return: 当前用例对应的接口请求参数字典
    """
    # 获取当前测试文件完整路径
    file_path = Path(request.module.__file__)
    module_name = file_path.parent.name
    # 获取纯文件名（带后缀，如 test_get_token_1.py）
    file_full_name = file_path.name
    # 去除后缀 .py
    file_name_no_suffix = file_full_name.replace(".py", "")
    print(f"file_name_no_suffix: {file_name_no_suffix}")
    # 文件名为 test_xxx.py → 提取xxx作为文件标识：test_get_token_1.py → token
    if file_name_no_suffix.startswith("test_"):
        file_tag = file_name_no_suffix.replace("test_", "")
    else:
        file_tag = file_name_no_suffix
    case_data = None
    # 判断当前用例是否在yaml配置清单内，不在则跳过
    if module_name not in CASE_CONFIG_MAP.keys() or file_tag not in [case['caseName'] for case in CASE_CONFIG_MAP[module_name]]:
        print(f"module_name: {module_name},CASE_CONFIG_MAP.keys():{CASE_CONFIG_MAP.keys()} file_tag: {file_tag},CASE_CONFIG_MAP[module_name]:{CASE_CONFIG_MAP[module_name]}")
        pytest.skip(f"跳过用例：文件标识{file_tag} ，该用例未配置在test_set.yml")
    for case in CASE_CONFIG_MAP.get(module_name, ""):
        if case.get('caseName', None) == file_tag:
            case_data = case.get('caseData', None)
            break
    return case_data
