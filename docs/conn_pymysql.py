from typing import Any, Union, Tuple

import pymysql




# Ref: https://juejin.cn/post/6893107055248375815

class Database(object):
    """
    pymysql 数据库操作类。
    """

    def __init__(self, host, user, password, db, port=3306, charset="utf8"):
        """
        初始化数据库类
        :param host: 链接地扯
        :param user: 用户名
        :param password: 密码
        :param db: 数据库名
        :param port: 端口
        :param charset: 字符集
        """
        try:
            self.connect = pymysql.connect(host=host, port=port, user=user,
                                           passwd=password,
                                           db=db, charset=charset)
            self.cursor = self.connect.cursor()
            print("初始化")
        except pymysql.err as res:
            print("链接出错了", str(res))

    def insert_all(self, insert_sql: str, data: dict) -> int:
        """
        功能 : 添加多条数据
        :param insert_sql: sql语句.如: insert into test1(name,age) values(%s,%s)
        :param data: {('小陈', 20), ('小东', 19)}
        :return: 返回影响行数.如添加了两条数据就返回 2 .
        """
        try:
            self.cursor.executemany(insert_sql, data)
            count = self.cursor.rowcount
            self.connect.commit()
            return count
        except Exception as e:
            self.connect.rollback()
            print("添加多条数据出错:{}".format(e))

    def insert(self, insert_sql: str, data: tuple) -> int:
        """
        功能 : 添加单条数据
        :type data: object ('小陈', 20)
        :param insert_sql: sql语句. 如 : insert into test1(name,age) values(%s,%s)
        :return: 返回添加成功的 ID .
        """
        try:
            self.cursor.execute(insert_sql, data)
            insert_id = self.connect.insert_id()
            self.connect.commit()
            return insert_id
        except Exception as e:
            self.connect.rollback()
            print("添加单条数据出错:{}".format(e))

    def select(self, select_sql: str, data=None) -> tuple:
        """
        功能：查询数据
        :param select_sql: 查询的 sql 语句。 如： select * from test1
        :param data: 默认为 None ,当 sql = 'select * from test1 where id=%s'，那么 data 就类似于 data = 2
        :return: 当 data 为 None 时：((1, '小东', 19), (2, '小陈', 20)) . 当 data 为不 None 时： ((1, '小东', 19),)
        """
        try:

            self.cursor.execute(select_sql, data)
            result_all: Union[Tuple, Any] = self.cursor.fetchall()
            return result_all
        except Exception as e:
            self.connect.rollback()
            print("查询数据出错:{}".format(e))

    def delete(self, delete_sql: str, data) -> int:
        """
        功能： 删除数据
        :param delete_sql: DELETE FROM test1 WHERE age = %s
        :param data: 如： 11
        :return: 返回删除的影响行数
        """
        try:
            self.cursor.execute(delete_sql, data)
            # 删除的影响行数
            row_count = self.cursor.rowcount
            # 提交事务
            self.connect.connect()
            return row_count
        except Exception as e:
            self.connect.rollback()
            print("删除数据出错:{}".format(e))

    def update(self, update_sql, data):
        try:
            self.cursor.execute(update_sql, data)
            # 更新的影响行数
            row_count = self.cursor.rowcount
            # 提交事务
            self.connect.connect()
            return row_count
        except Exception as e:
            self.connect.rollback()
            print("更新数据出错:{}".format(e))

    def __del__(self):
        """
        关闭数据库链接
        """
        self.connect.close()
        self.cursor.close()
        print("关闭数据库")
