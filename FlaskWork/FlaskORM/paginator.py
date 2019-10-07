""""
编写分页器
"""

from models import Curriculum


class Pager():
    """
    flask 分页通过sqlalchemy查询进行分页
    offset 偏移，开始查询的位置
    limit 单页条数
    分页器需要具备的功能：
        页码
        分页数据
        是否第一页
        是否最后一页
    """
    def __init__(self, data, page_size):
        """

        :param data: 总数据
        :param page_size: 每页多少条数据
        """
        self.data = data
        self.page_size = page_size
        self.is_start = False   # 是否首页
        self.is_end = False     # 是否最后一页
        self.page_count = len(data)
        self.next_page = 0  # 下一页
        self.previous_page = 0  # 上一页
        self.page_number = self.page_count/page_size
        # 如果能被整除
        if self.page_number == int(self.page_number):
            self.page_number = int(self.page_number)
        else:
            # 如果不能被整除，页码+1
            self.page_number = int(self.page_number) + 1
        # 页码范围
        self.page_range = range(1, self.page_number+1)

    def page_date(self, page):
        """

        :param page: 页码
            假设
                page_size = 10
                第一页     偏移offset从0开始    limit(10)
        :return:  返回分页数据
        """
        self.next_page = int(page) + 1
        self.previous_page = int(page) - 1
        if page <= self.page_range[-1]:
            page_start = (page - 1) * self.page_size
            page_end = page * self.page_size
            data = self.data[page_start: page_end]
            if page == 1:
                self.is_start = True
            else:
                self.is_start = False
            if page == self.page_range[-1]:
                self.is_end = True
            else:
                self.is_end = False
        else:
            data = ['没有数据']
        return data

if __name__ == '__main__':
    while True:
        page = int(input('页码>>>'))

        data = Curriculum.query.all()
        page_size = 3
        pager = Pager(data, page_size)
        print('当前页码是：{}'.format(page))
        print('共{}条数据'.format(pager.page_count))
        print('总页数：{}'.format(pager.page_number))
        print('页码范围：{}'.format(list(pager.page_range)))
        page_data = pager.page_date(page)
        print('页码数据：{}'.format(page_data))
        print('是否首页：{}'.format(pager.is_start))
        print('是否尾页：{}'.format(pager.is_end))




"""
往数据库快速添加数据

import datetime
from models import Leave
leave_name_list = ['玲玲', '玲依', '依玲', '依依', '妖玲', '玲妖', '妖妖', 'Rose', 'Jack', 'Tom', 'Jim']
leave_type_list = ['事假', '病假', '出差', '调休', '婚假', '产假', '年假', '缺勤', '事假', '病假', '出差']
leave_description_list = ['事假', '病假', '出差', '调休', '婚假', '产假', '年假', '缺勤', '事假', '病假', '出差']
leave_phone_list = ['123', '456', '789', '123', '456', '789', '123', '456', '789', '123', '456']

for a, b, c, d, e, f, g, index in enumerate(leave_name_list, leave_type_list, leave_description_list, leave_phone_list, 1)
"""