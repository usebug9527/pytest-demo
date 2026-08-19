import pymysql
from pymysql.cursors import DictCursor

from architecture.api.rest.v2.db.common.db_api import DB
from architecture.api.rest.v2.utils.yaml_parser import YamlParser


class Database(DB):
    def __init__(self):
        super().__init__()
        # db_config = YamlParser.parse_test_bed()['db']
        # self.db_config = db_config

    @staticmethod
    def query(sql, args):
        db_config = YamlParser.get_test_bed()['zentao']['db']
        # 建立连接
        conn = pymysql.connect(**db_config)
        # DictCursor：返回字典格式，否则返回元组
        cursor = conn.cursor(cursor=DictCursor)

        try:
            # 1. 查询
            cursor.execute(sql, args)  # 参数化，防止SQL注入，不要字符串拼接
            result_list = cursor.fetchall() # 获取全部

            print("查询结果：", result_list)
            return result_list
        except Exception as e:
            conn.rollback()  # 出错回滚
            print("异常：", e)
        finally:
            cursor.close()
            conn.close()
#
# if __name__ == '__main__':
#     db = Database()
#     db.query("select * from zt_user where id=%s or id=%s", (1, 2,))