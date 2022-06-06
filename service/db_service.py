import pymysql


# 数据库服务

def get_conn():
    # 建立连接
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="covid", charset="utf8")
    # c创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    """

    :param sql:
    :param args:
    :return:
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def test():
    sql = "select * from details"
    res = query(sql)
    return res[0]


def get_center_top_data():
    # sql = "select sum(confirm)," \
    #       "(select suspect from history order by ds desc limit 1)," \
    #       "sum(heal),sum(dead) from details " \
    #       "where update_time=(select update_time from details order by update_time desc limit 1) "
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal),sum(dead) from details "
    res = query(sql)
    return res[0]


def get_center_bottom_data():
    # sql = "select province,sum(confirm) from details " \
    #       "where update_time=(select update_time from details " \
    #       "order by update_time desc limit 1) " \
    #       "group by province"
    sql = "select province,sum(confirm) from details " \
          "group by province"
    res = query(sql)
    return res


def get_left_top_data():
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res


def get_left_bottom_data():
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res


def get_right_top_data():
    sql = 'select city,confirm from ' \
          '(select city,confirm from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆") ' \
          'union all ' \
          'select province as city,sum(confirm) as confirm from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆") group by province) as a ' \
          'order by confirm desc limit 5'
    res = query(sql)
    return res


def get_right_bottom_data():
    sql = "select content from hotsearch order by id desc limit 20"
    res = query(sql)
    return res


if __name__ == "__main__":
    print(get_right_bottom_data())
    # print(test())
