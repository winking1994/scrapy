# -*- coding: utf-8 -*-
import scrapy
from hell.items import HellItem
from scrapy.http import Request	

class YiclubSpider(scrapy.Spider):
    name = 'yiclub'
    allowed_domains = ['yiyiclub.com']
    start_urls = ['http://www.yiyiclub.com/meitui/list_3_1.html']

    def parse(self, response):
        pics = response.xpath('//div[@class= " mt50 pic-list1 clearfix"]/ul/li')
        for pic in pics:
            item = HellItem()
            name = pic.xpath('./a/img/@alt').extract()[0]
            address = pic.xpath('./a/img/@data-original').extract()[0]
            item['name'] = name
            item['address'] = address
            yield item

            for i in range(1,18):
                url = 'http://www.yiyiclub.com/meitui/list_3_1' + str(i) + '.html'
                yield Request(url, callback=self.parse)