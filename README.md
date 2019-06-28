# PureMySQL
![PyPI](https://img.shields.io/pypi/v/PureMySQL.svg)

一个MySQL简单操作方式

```
pip install PureMySQL
```

- https://github.com/mouday/PureMySQL
- https://pypi.org/project/PureMySQL/

代码示例
```python

from puremysql import PureMysql

db_config = {
    "database": "mydata",
    "user": "root",
    "password": "123456",
    "host": "127.0.0.1",
    "port": 3306,
}

pure_mysql = PureMysql(**db_config)
student = PureTable(pure_mysql, "student")


# 插入数据
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


# 删除数据
def test_delete():
    ret = student.delete("id=13")
    print(ret)

    ret = student.delete_by_id(12)
    print(ret)


# 更新数据
def test_update():
    data = {
        "name": "Tom"
    }
    # ret = student.update(data, "name='Tom'")
    # print(ret)

    ret = student.update_by_id(data, 1)
    print(ret)


# 查询数据
def test_select():
    ret = student.select(["name", "age"], "id=1")
    print(ret)

    ret = student.select("name, age", "id=1")
    print(ret)

    ret = student.select_one(["name", "age"], "id=1")
    print(ret)

```