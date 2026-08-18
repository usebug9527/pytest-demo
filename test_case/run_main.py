import logging
import os

import pytest
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(f"path = {os.path.abspath(__file__)}")
# print(f"path = {os.path.dirname(os.path.abspath(__file__))}")
# LOG = logging.getLogger(__name__)
print(os.getcwd())

if __name__ == '__main__':
    # os.chdir(ROOT_DIR)
    # print(f"ROOT_DIR: {ROOT_DIR}")
    pytest.main()
    # os.system('allure generate allure-results -o allure-report --clean')
    # os.system('allure open allure-report')
