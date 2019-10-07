from main import models


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


class User(BaseModel):
    __tablename__ = 'user'
    u_email = models.Column(models.String(32), unique=True)
    u_password = models.Column(models.String(32))
    u_name = models.Column(models.String(32))
    u_phone_number = models.Column(models.String(11), nullable=True)
    u_address = models.Column(models.String(1024), nullable=True)
    u_gender = models.Column(models.String(32), nullable=True)
    u_age = models.Column(models.Integer, nullable=True)
    u_identity = models.Column(models.String(32), default='学生') # 身份
    u_subject = models.Column(models.String(32), nullable=True)
    u_phases = models.Column(models.String(32), nullable=True)


class Leave(BaseModel):
    __tablename__ = 'leave'
    request_id = models.Column(models.Integer)              # 请假人id
    request_name = models.Column(models.String(32))         # 请假人姓名
    request_type = models.Column(models.String(32))         # 假期类型
    request_start_time = models.Column(models.String(32))   # 起始时间
    request_end_time = models.Column(models.String(32))     # 结束时间
    request_data = models.Column(models.String(32))         # 请求天数
    request_description = models.Column(models.TEXT)        # 请假事由
    request_phone = models.Column(models.String(11))        # 联系方式
    request_status = models.Column(models.String(32))
