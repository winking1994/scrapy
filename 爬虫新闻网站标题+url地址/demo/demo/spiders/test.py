# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem
from scrapy.http import Request

class TestSpider(scrapy.Spider):
    #定义爬虫的名字和需要爬取的网址
    name = "test"
    allowed_domains = ["news.ldnews.cn"]
    start_urls = ['http://news.ldnews.cn/zhnews/domesticnews/1.shtml']

    def parse(self, response):
        for resp in response.css('.item'):
            #实例化item
            item = DemoItem()
            #把获取到的内容保存到item内
            item['title'] = resp.css('li a::attr(title)').extract()
            item['href'] = resp.css('li a::attr(href)').extract()      
            yield item
            
        #下面是多页面的爬取方法
        urls = response.css('.align-c a::attr(href)').extract()
        for url in urls:
            yield Request(url, callback=self.parse)


        categorys = response.css('.m-header-nav-list li a::attr(href)').extract()
        for ct in categorys:
            yield Request(ct, callback=self.parse)