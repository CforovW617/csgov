import scrapy
from scrapy.selector import Selector
from scrapy import Request
from csgov.items import DeptItem
from csgov.items import LeaderInfoItem

class LeaderInfoSpider(scrapy.Spider):
    name = "leader_info"
    allowed_domains = ["www.changsha.gov.cn"]
    start_urls = ["http://www.changsha.gov.cn/szf"]

    def parse(self, response, **kwargs):
        sel = Selector(response)
        head = "http://www.changsha.gov.cn/szf"
        urls = sel.xpath('//*[@id="szf"]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[*]/a/@href').extract()
        names = sel.xpath('//*[@id="szf"]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[*]/a/text()').extract()
        for url, name in zip(urls, names):
            item = DeptItem()
            item['url'] = head+url[1:]
            item['name'] = name
            yield item