# -*- coding: utf-8 -*-

# @Date    : 2019-06-27
# @Author  : Peng Shiyu


from functools import partial


class SQLBuilder(object):
    def __init__(self):
        self._sqls = []

    def __getattr__(self, item):
        return partial(self.append, item)

    def append(self, key, value=""):
        key = key.upper().strip("_").replace("_", " ")
        self._sqls.append("{} {}".format(key, value))
        return self

    def build(self):
        return " ".join(self._sqls)

    def parentheses(self, value):
        self._sqls.append("({})".format(value))
        return self

    def __str__(self):
        return self.build()


if __name__ == '__main__':
    sql_builder = SQLBuilder()
    sql = sql_builder.select("name, age").from_("student").where("id=1").order_by("id")
    print(sql)
    # SELECT name, age FROM student WHERE id=1 ORDER BY id
