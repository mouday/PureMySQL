# -*- coding: utf-8 -*-

# @Date    : 2019-07-09
# @Author  : Peng Shiyu

from puremysql import PureMysql

url = "mysql://root:123456@127.0.0.1:3306/demo"
pure_mysql = PureMysql(db_url=url)
student = pure_mysql.table("todo_list")

for row in student.select_page(2, 3, ["content"]):
    print(row)

print(student.count())
