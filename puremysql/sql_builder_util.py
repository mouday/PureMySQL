# -*- coding: utf-8 -*-

# @Date    : 2019-06-27
# @Author  : Peng Shiyu


from puremysql.sql_builder import SQLBuilder


class SQLBuilderUtil(object):
    @classmethod
    def get_key_str(cls, fields):
        if isinstance(fields, list):
            fields_str = ", ".join(["`{}`".format(field) for field in fields])
        else:
            fields_str = fields

        return fields_str

    @classmethod
    def get_value_str(cls, keys):
        return ", ".join(["%({})s".format(key) for key in keys])

    @classmethod
    def get_key_value_str(cls, keys):
        return ", ".join(["`{0}`=%({0})s".format(key) for key in keys])

    @classmethod
    def get_select_sql(cls, table, fields, where):
        fields_str = cls.get_key_str(fields)

        sql_builder = SQLBuilder()
        sql_builder.select(fields_str)
        sql_builder.from_(table)
        sql_builder.where(where)

        return sql_builder.build()

    @classmethod
    def get_insert_sql(cls, table, keys):
        keys_str = cls.get_key_str(keys)
        values_str = cls.get_value_str(keys)

        sql_builder = SQLBuilder()
        sql_builder.insert_into(table)
        sql_builder.parentheses(keys_str)
        sql_builder.values()
        sql_builder.parentheses(values_str)

        return sql_builder.build()

    @classmethod
    def get_delete_sql(cls, table, where):

        sql_builder = SQLBuilder()
        sql_builder.delete_from(table)
        sql_builder.where(where)

        return sql_builder.build()

    @classmethod
    def get_update_sql(cls, table, keys, where):

        key_value_str = cls.get_key_value_str(keys)
        sql_builder = SQLBuilder()
        sql_builder.update(table)
        sql_builder.set(key_value_str)
        sql_builder.where(where)

        return sql_builder.build()

    @classmethod
    def get_list_keys(cls, data):
        # 列表中字典key值校验
        keys = data[0].keys()
        for item in data:
            if item.keys() != keys:
                raise Exception("data key not equal!")
        return keys


if __name__ == '__main__':
    print(SQLBuilderUtil.get_insert_sql("student", ["name", "age"]))
