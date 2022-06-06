from model.mydb import MyDatabase


db = MyDatabase()


def select_one():
    sql = "select * from details"
    return db.select(sql)


if __name__ == '__main__':
    res = select_one()
    print(res)