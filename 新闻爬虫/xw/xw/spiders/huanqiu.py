# -*- coding: utf-8 -*-
import scrapy
from xw.items import XwItem
from scrapy.http import Request

class HuanqiuSpider(scrapy.Spider):
    name = 'huanqiu'
    allowed_domains = ['hope.huanqiu.com']
    start_urls = ['http://hope.huanqiu.com/domesticnews/2.html']

    def parse(self, response):
        xw = response.xpath('//div[@class="pad20"]/div/ul/li')
        

        for hq in xw:
        	item = XwItem()
        	item['name'] = hq.xpath('./a/@title').extract()[0]
        	item['connection'] = hq.xpath('./a/@href').extract()[0]
        	item['time'] = hq.xpath('./em').extract()[0]

        	yield item


        for x in range(1,10):
        	url = 'http://hope.huanqiu.com/domesticnews/2' + str(x) + '.html'
        	yield Request(url, callback=self.parse)
        			