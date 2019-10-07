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


class BaseModel(models.Model):
    __abstract__ = True     # 声明当前类是抽象类，被继承调用不被创建
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db = models.session()
        db.add(self)
        db.commit()

    def delete(self):
        db = models.session()
        db.delete(self)
        db.commit()


# 定义表
class Curriculum(BaseModel):
    __tablename__ = "curriculum"
    id = models.Column(models.Integer, primary_key=True)
    c_id = models.Column(models.String(32))
    c_name = models.Column(models.String(32))
    c_time = models.Column(models.Date)


c = Curriculum.query.get(3)
print(c.c_name)
c.delete()
