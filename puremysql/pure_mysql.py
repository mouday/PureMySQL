# -*- coding: utf-8 -*-

# @Date    : 2019-06-27
# @Author  : Peng Shiyu

import mysql.connector

from puremysql.logger import pure_mysql_logger


class PureMysql(object):
    def __init__(self, **db_config):
        # 返回字典对象
        self.connect = mysql.connector.connect(**db_config)
        self.cursor = self.connect.cursor(dictionary=True)

    def close(self):
        self.cursor.close()
        self.connect.close()

    def execute(self, sql, data=(), commit=False):
        pure_mysql_logger.info(self.cursor.statement)

        if isinstance(data, list):
            self.cursor.executemany(sql, data)
        else:
            self.cursor.execute(sql, data)

        if commit:
            self.connect.commit()

        pure_mysql_logger.info(self.cursor.statement)

        return self.cursor
