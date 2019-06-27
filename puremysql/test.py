# -*- coding: utf-8 -*-

# @Date    : 2019-06-27
# @Author  : Peng Shiyu

from puremysql.pure_mysql import PureMysql
from puremysql.pure_table import PureTable

if __name__ == '__main__':
    db_config = {
        "database": "mydata",
        "user": "root",
        "password": "123456",
        "host": "127.0.0.1",
        "port": 3306,
    }

    pure_mysql = PureMysql(**db_config)
    student = PureTable(pure_mysql, "student")


    def test_insert():
        data = {
            "name": "Tom",
            "age": 25
        }

        count = student.insert(data)
        print(count)

        data = [
            {
                "name": "Tom",
                "age": 26,

            },
            {
                "name": "Jack",
                "age": 27,

            }
        ]
        count = student.insert(data)
        print(count)


    def test_delete():
        ret = student.delete("id=13")
        print(ret)

        ret = student.delete_by_id(12)
        print(ret)


    def test_update():
        data = {
            "name": "Tom"
        }
        # ret = student.update(data, "name='Tom'")
        # print(ret)

        ret = student.update_by_id(data, 1)
        print(ret)


    def test_select():
        ret = student.select(["name", "age"], "id=1")
        print(ret)

        ret = student.select("name, age", "id=1")
        print(ret)

        ret = student.select_one(["name", "age"], "id=1")
        print(ret)


    test_insert()
    test_delete()
    test_update()
    test_select()
