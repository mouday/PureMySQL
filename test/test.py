# -*- coding: utf-8 -*-

# @Date    : 2019-06-27
# @Author  : Peng Shiyu

from __future__ import unicode_literals, print_function
from puremysql.pure_mysql import PureMysql

import unittest


class PureTest(unittest.TestCase):
    student = None
    pure_mysql = None

    @classmethod
    def setUpClass(cls):
        db_config = {
            "database": "mydata",
            "user": "root",
            "password": "123456",
            "host": "127.0.0.1",
            "port": 3306,
        }

        # cls.pure_mysql = PureMysql(**db_config)

        # 或者
        url = "mysql://root:123456@127.0.0.1:3306/mydata"
        cls.pure_mysql = PureMysql(db_url=url)

        cls.student = cls.pure_mysql.table("student")

        drop_table = "drop table if exists student"

        create_table = """
        CREATE TABLE `student` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(10) DEFAULT NULL,
        `age` int(11) DEFAULT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8
        """

        cls.pure_mysql.execute(drop_table, commit=True)
        cls.pure_mysql.execute(create_table, commit=True)

    @classmethod
    def tearDownClass(cls):
        cls.pure_mysql.close()

    def test_insert(self):
        data = {
            "name": "Tom",
            "age": 25
        }

        count = self.student.insert(data)
        self.assertEqual(count, 1)

    def test_insert_many(self):
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
        count = self.student.insert(data)
        self.assertEqual(count, 2)

    def test_delete(self):
        data = [
            {
                "name": "DELETE",
                "age": 26,
            },
            {
                "name": "DELETE",
                "age": 27,
            }
        ]

        self.student.insert(data)
        count = self.student.delete("name='DELETE'")
        self.assertEqual(count, 2)

    def test_delete_by_id(self):
        data = {
            "name": "DELETE",
            "age": 26,
            "id": 2006,
        }

        self.student.insert(data)

        count = self.student.delete_by_id(2006)
        self.assertEqual(count, 1)

    def test_update(self):
        data = {
            "name": "UPDATE",
            "age": 26
        }

        self.student.insert(data)

        data = {
            "name": "NEW_UPDATE",
            "age": 23
        }

        count = self.student.update(data, "name='UPDATE'")
        self.assertEqual(count, 1)

    def test_update_by_id(self):
        data = {
            "name": "UPDATE",
            "age": 26,
            "id": 3007,
        }

        self.student.insert(data)

        data = {
            "name": "ID_UPDATE",
            "age": 23
        }

        count = self.student.update_by_id(data, 3007)
        self.assertEqual(count, 1)

    def test_select(self):
        ret = self.student.select(["name", "age"], "id=1")
        print(ret)
        self.assertIsInstance(ret, list)

        ret = self.student.select("name, age", "id=1")
        print(ret)
        self.assertIsInstance(ret, list)

        ret = self.student.select_one(["name", "age"], "id=1")
        print(ret)
        self.assertIsInstance(ret, dict)

        ret = self.student.select_by_id("name, age", 2007)
        print(ret)
        self.assertIsInstance(ret, dict)


if __name__ == '__main__':
    unittest.main()
