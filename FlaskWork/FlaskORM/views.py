from main import app
from flask import render_template
import datetime
from models import Curriculum


class Calendar():
    """
    当前类实现日历功能
    ⒈以列表嵌套列表的形式返回日历
    ⒉按照日历格式打印日历
        周日 周一 周二 周三 周四 周五 周六
        如果一号是周日，那么第一行显示 ''*0 + 1-7号
        如果一号是周一，那么第一行显示 ''*1 + 1-6号
        如果一号是周二，那么第一行显示 ''*2 + 1-5号
        如果一号是周三，那么第一行显示 ''*3 + 1-4号
        如果一号是周四，那么第一行显示 ''*4 + 1-3号
        如果一号是周五，那么第一行显示 ''*5 + 1-2号
        如果一号是周六，那么第一行显示 ''*6 + 1号
        输入年份和月份，得到某年某月一号是周几
        []填充7个元素 索引0对应周一（日历中0-6代表周一到周日）
        返回列表
        day_range 1-30
    """
    def __init__(self, year, month='now'):
        self.result = []
        # 月份分类
        big_month = [1, 3, 5, 7, 8, 10, 12]
        small_month = [4, 6, 9, 11]
        # 获取当前月份
        now = datetime.datetime.now()
        if month == 'now':
            month = now.month
            first_date = datetime.datetime(now.year, month, 1, 0, 0)
        else:
            assert int(month) in range(1, 13)
            first_date = datetime.datetime(int(year), int(month), 1, 0, 0)
        # 判断获取指定月份天数
        if month in big_month:
            day_range = range(1, 32)
        elif month in small_month:
            day_range = range(1, 31)
        elif month == 2:
            if year % 400 == 0:
                day_range = range(1, 30)
            else:
                day_range = range(1, 29)
        self.daye_range = list(day_range)
        # 判断获取指定月的一号是周几。在python中0-6代表周一到周天
        first_week = first_date.weekday()
        # 获取日历的第一行数据
        line01 = []
        # 如果first_week=6，说明是周日。日历表又是【周日到周一】，所以前七天都是空白或是上个月的日期
        # 而range是含头不含尾的，所以+1。
        for week in range(first_week + 1):
            line01.append('')
        for w in range(6 - first_week):
            line01.append(
                str(self.daye_range.pop())
            )
        self.result.append(line01)
        # 如果总天数列表中还有值，就接着循环
        while self.daye_range:
            line = []
            for i in range(7):
                if len(line) < 7 and self.daye_range:
                    line.append(
                        str(self.daye_range.pop(0))
                    )
                else:
                    line.append('')
            self.result.append(line)

    def return_month(self):
        """
        以嵌套列表的形式返回日历
        """
        return self.result

    def print_month(self):
        """
        按照日历格式打印日历
        """
        print('星期日 星期一 星期二 星期三 星期四 星期五 星期六')
        # 遍历行数
        for line in self.result:
            # 遍历每行中有值的列
            for day in line:
                # 按照6个字节的长度居中展示
                day = day.center(6)
                print(day, end=' ')
            print()


@app.route('/')
def index():
    name = 'Jack'
    return render_template('index.html', **locals())


import functools
def loginValid(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        email = request.cookies.get('email')
        id = request.cookies.get('id')
        if id and email:
            user = User.query.get(int(id))
            if user.u_email == email:
                return func(*args, **kwargs)
            else:
                return redirect('/login/')
        return redirect('/login/')
    return inner


@app.route('/logout/')
def logout():
    response = redirect('/login/')
    response.delete_cookie('id')
    response.delete_cookie('email')
    return response


import hashlib
def setPassword(password):
    result = hashlib.md5(password.encode()).hexdigest()
    return result


from flask import request
from flask import redirect
from models import User
@app.route('/register/', methods=['GET', 'POST'])
def register():
    result = {
        'code': 200,
        'data': ''
    }
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            password = request.form.get('password')
            password_to = request.form.get('password_to')
            print('email>>>{}\npassword>>>{}\npassword_to>>>{}'.format(email, password, password_to))
            if password == password_to:
                print('第一次校验')
                db_email = User.query.filter_by(u_email=email).first()
                print('db_email>>>{}'.format(db_email))
                if not db_email:
                    print('第二次校验')
                    user = User()
                    user.u_email = email
                    print('user.u_email>>>{}'.format(user.u_email))
                    user.u_password = setPassword(password)
                    print('user.u_password>>>{}'.format(user.u_password))
                    user.u_name = request.form.get('username')
                    print('user.u_name>>>{}'.format(user.u_name))
                    user.u_phone_number = request.form.get('phonenumber')
                    print('user.u_phone_number>>>{}'.format(user.u_phone_number))
                    user.u_address = request.form.get('address')
                    print('user.u_address>>>{}'.format(user.u_address))
                    user.save()
                    print(user.id)
                    return redirect('/login/')
                else:
                    result['code'] = 404
                    result['data'] = '邮箱已被注册'
            else:
                result['code'] = 404
                result['data'] = '两次密码不一致'
        else:
            result['code'] = 404
            result['data'] = '邮箱不能为空'

    return render_template('register.html', **locals())


from flask import session
@app.route('/login/', methods=['GET', 'POST'])
def login():
    result = {
        'code': 200,
        'data': ''
    }
    if request.method == 'POST':
        email = request.form.get('email')
        password = setPassword(request.form.get('password'))
        print('email>>>{}\npassword>>>{}'.format(email, password))
        if email and password:
            db_email = User.query.filter_by(u_email=email).first()
            print('db_email>>>{}'.format(db_email))
            if db_email:
                db_password = db_email.u_password
                print('db_password>>>{}'.format(db_password))
                if password == db_password:
                    response = redirect('/index/')
                    response.set_cookie('email', db_email.u_email)
                    response.set_cookie('id', str(db_email.id))
                    session.permanent = True
                    session['email'] = db_email.u_email
                    session['id'] = str(db_email.id)
                    return response
                else:
                    result['code'] = 404
                    result['data'] = '密码错误'
            else:
                result['code'] = 404
                result['data'] = '邮箱不存在'


    return render_template('login.html', **locals())


@app.route('/index/')
@loginValid
def ex_index():
    # c = Curriculum()
    # c.c_id = '0001'
    # c.c_name = 'python基础'
    # c.c_time = datetime.datetime.now()
    # c.save()
    curr_list = Curriculum.query.all()
    return render_template('ex_index.html', **locals())


@app.route('/userinfo/', methods=['GET', 'POST'])
@loginValid
def userinfo():
    user_id = request.cookies.get('id')
    print('user_id>>>{}'.format(user_id))
    user = User.query.get(user_id)
    print('user>>>{}'.format(user))
    if request.method == 'POST':
        u_name = request.form.get('u_name')
        u_phone_number = request.form.get('u_phone_number')
        u_address = request.form.get('u_address')
        u_gender = request.form.get('u_gender')
        u_age = request.form.get('u_age')
        u_identity = request.form.get('u_identity')
        u_subject = request.form.get('u_subject')
        u_phases = request.form.get('u_phases')
        user.u_name = u_name
        user.u_phone_number = u_phone_number
        user.u_address = u_address
        user.u_gender = u_gender
        user.u_age = u_age
        user.u_identity = u_identity
        user.u_subject = u_subject
        user.u_phases = u_phases
        user.save()
    return render_template('userinfo.html', **locals())


@app.route('/ca/', methods=['GET', 'POST'])
@loginValid
def course_arrangement():
    year_list = [x for x in range(2020, 1948, -1)]
    month_list = [x for x in range(12, 0, -1)]
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if request.method == 'POST':
        year = request.form.get('year')
        month = request.form.get('month')
    calendar = Calendar(int(year), int(month))
    return render_template('course_arrangement.html', **locals())


from models import Leave
@app.route('/rl/', methods=['GET', 'POST'])
@loginValid
def request_leave():
    type_list = ['事假', '病假', '婚假', '年假', '产假', '缺勤', '调休', '加班', '出差']
    data_list = [x for x in range(365)]
    if request.method == 'POST':
        user = request.cookies.get('id')
        print('user>>>{}'.format(user))
        request_name = request.form.get('request_name')
        print('request_name>>>{}'.format(request_name))
        request_type = request.form.get('request_type')
        print('request_type>>>{}'.format(request_type))
        request_start_time = request.form.get('request_start_time')
        print('request_start_time>>>{}'.format(request_start_time))
        request_end_time = request.form.get('request_end_time')
        print('request_end_time>>>{}'.format(request_end_time))
        request_data = request.form.get('request_data')
        request_description = request.form.get('request_description')
        print('request_description>>>{}'.format(request_description))
        request_phone = request.form.get('request_phone')
        print('request_phone>>>{}'.format(request_phone))
        leave = Leave()
        leave.request_id = user
        print('leave.request_id>>>{}'.format(leave.request_id))
        leave.request_name = request_name
        print('leave.request_name>>>{}'.format(leave.request_name))
        leave.request_type = request_type
        print('leave.request_type>>>{}'.format(leave.request_type))
        leave.request_start_time = request_start_time
        print('leave.request_start_time>>>{}'.format(leave.request_start_time))
        leave.request_end_time = request_end_time
        print('leave.request_end_time>>>{}'.format(leave.request_end_time))
        leave.request_data = request_data
        print('leave.request_data>>>{}'.format(leave.request_data))
        leave.request_description = request_description
        print('leave.request_description>>>{}'.format(leave.request_description))
        leave.request_phone = request_phone
        print('request_phone>>>{}'.format(leave.request_phone))
        leave.request_status = 0
        leave.save()
        print('保存成功')
    return render_template('request_leave.html', **locals())


from paginator import Pager
@app.route("/ll/<int:page>/")
@loginValid
def leave_list(page):
    leaves = Leave.query.all()
    pager = Pager(leaves, 2)
    page_data = pager.page_date(page)
    return render_template("leave_list.html", **locals())
