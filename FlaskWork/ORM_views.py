import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


# 实例化app
app = Flask(__name__)

# 配置参数
# abspath 绝对路径
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# app.config返回字典对象，里面用来存放当前app实例的配置
"""
#配置数据连接的参数
# MySQL——》 mysql://username:password@hostname[:port]/database
# Sqlite(windows)——》 sqlite:///d:/python/python.sqlite
# Sqlite(linux)——》 sqlite:////python/python.sqlite
# Pgsql——》 postgresql://username:password@hostname/database
"""

# BASE_DIR是路径   ORM.sqlite数据库名称
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR, "ORM.sqlite")    # 数据库地址 sqllite
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:111111@localhost/demo3"                  # 数据库地址 mysql

app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True      # 请求结束后自动提交数据库修改

# 如果设置成 True (默认情况)，Flask-SQLAlchemy将会追踪对象的修改并且发送信号。这需要额外的内存，如果不必要的可以禁用它。
app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] = True     # flask1版本之后，添加的选项，目的是跟踪修改


# 关联sqlalchemy和flask应用
models = SQLAlchemy(app)


# 定义表
class Curriculum(models.Model):
    __tablename__ = "curriculum"
    id = models.Column(models.Integer, primary_key=True)
    c_id = models.Column(models.String(32))
    c_name = models.Column(models.String(32))
    c_time = models.Column(models.Date)


# 创建表（同步）
# models.create_all()


import datetime
# 创建操作数据库的会话
session = models.session()

# 单个数据添加
# c = Curriculum(c_id='0001', c_name='python基础', c_time=datetime.datetime.now())
# session.add(c)
# session.commit()

# 多个数据添加
# c1 = Curriculum(c_id="0002", c_name="html", c_time=datetime.datetime.now())
# c2 = Curriculum(c_id="0003", c_name="mysql", c_time=datetime.datetime.now())
# c3 = Curriculum(c_id="0004", c_name="linux", c_time=datetime.datetime.now())
# session.add_all(
#     [c1, c2, c3]
# )
# session.commit()

# 查询所有（查询数据不需要commit提交）
# all_c = Curriculum.query.all()
# for c in all_c:
#     print(c.id, c.c_name)

# 条件查询
# all_c = Curriculum.query.filter_by(c_id="0002")     # 返回列表对象
# for c in all_c:
#     print(c.id, c.c_name)

# 查询一条
# c = Curriculum.query.get(1)    # 返回列表对象（get后面的参数是id）
# print(c)
# print(c.id, c.c_name)

# c = Curriculum.query.first()   # 返回第一条数据
# print(c.id, c.c_name)

# 排序
# all_c = Curriculum.query.order_by("id")
# all_c = Curriculum.query.order_by(models.desc("id")) # 倒序（desc）
# for c in all_c:
#     print(c.id, c.c_name)

# all_c = Curriculum.query.offset(2).limit(2).all() #倒序
#     # offset 偏移，在这里指的时候查询的起始位置
#     # limit 具体查询的数量
# # select * from curriculum limit 0,2 #从0号索引开始，查询两条
# for c in all_c:
#     print(c.id, c.c_name)

# 删除数据
# c = Curriculum.query.get(4)
# print(c)
# session.delete(c)
# session.commit()

# 修改数据
# c = Curriculum.query.get(3)
# c.c_name = "MySQL"
# session.add(c)
# session.commit()

# 注意：增删改都需要先查询数据
