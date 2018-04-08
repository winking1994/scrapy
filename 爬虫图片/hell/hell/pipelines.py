# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests

class HellPipeline(object):
    def process_item(self, item, spider):
        #return item
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
                


                r = requests.get(url=item['address'], headers=headers, timeout=4)
                with open(r'/Users/xiaoyu/scrapy/hell/tp/' + item['name'] + '.jpg', 'wb') as f:
                        f.write(r.content)
