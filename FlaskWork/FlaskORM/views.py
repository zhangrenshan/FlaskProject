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


@app.route('/register/')
def register():
    return render_template('register.html', **locals())


@app.route('/login/')
def login():
    return render_template('login.html', **locals())


@app.route('/index/')
def ex_index():
    # c = Curriculum()
    # c.c_id = '0001'
    # c.c_name = 'python基础'
    # c.c_time = datetime.datetime.now()
    # c.save()
    curr_list = Curriculum.query.all()
    return render_template('ex_index.html', **locals())


@app.route('/userinfo/', methods=['GET', 'POST'])
def userinfo():
    year_list = [x for x in range(2020, 1948, -1)]
    month_list = [x for x in range(12, 0, -1)]
    # year = request.form.get('year')
    # month = request.form.get('month')
    # calendar = Calendar(int(year), int(month))
    calendar = Calendar(2019, 9)
    return render_template('userinfo.html', **locals())
