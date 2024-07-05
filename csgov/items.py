# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class CsgovItem(scrapy.Item):
    pass

class DeptItem(scrapy.Item):
    url = Field() # 链接
    name = Field()  # 部门名

class LeaderInfoItem(scrapy.Item):
    index = Field()  # 索引号
    org = Field()  # 所属机构
    dep = Field()  # 公开责任部门
    pub = Field()  # 公开范围
    exp = Field()  # 公开方式
    name = Field()  # 姓名
    duty = Field()  # 职务
    work = Field()  # 工作职责
    intro = Field()  # 个人简介
    resume = Field()  # 工作简历