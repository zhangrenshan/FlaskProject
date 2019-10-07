import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()


# 实例化app
app = Flask(__name__)


# # 配置参数
# # abspath 绝对路径
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
# # app.config返回字典对象，里面用来存放当前app实例的配置
# """
# #配置数据连接的参数
# # MySQL——》 mysql://username:password@hostname[:port]/database
# # Sqlite(windows)——》 sqlite:///d:/python/python.sqlite
# # Sqlite(linux)——》 sqlite:////python/python.sqlite
# # Pgsql——》 postgresql://username:password@hostname/database
# """
#
# # BASE_DIR是路径   ORM.sqlite数据库名称
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR, "ORM.sqlite")    # 数据库地址 sqlite
# # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:111111@localhost/demo3"                  # 数据库地址 mysql
#
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True      # 请求结束后自动提交数据库修改
#
# # 如果设置成 True (默认情况)，Flask-SQLAlchemy将会追踪对象的修改并且发送信号。这需要额外的内存，如果不必要的可以禁用它。
# app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] = True     # flask1版本之后，添加的选项，目的是跟踪修改


# 第一种，直接写配置文件
app.config.from_pyfile('settings.py')
app.config.from_object("settings.Config")                 # 来源于类对象


s = os.urandom(24)
app.secret_key = s


# 关联sqlalchemy和flask应用
models = SQLAlchemy(app)