# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import json
from neteasemusic.items import NeteaseMusicItem

class BillBoardSpider(scrapy.Spider):
    name = 'BillBoard_Spider'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/discover/toplist']

    def parse(self, response):
        for i in re.findall('<p class="name">.*?</a>',response.body):
            #print(i)
            ii=re.findall('id=\d+',i)
            id=ii[0].replace('id=','')
            names=re.findall('>.*?<',i)
            name=names[1].replace('>','')
            name=name.replace('<','')
            item=NeteaseMusicItem()
            item['list_id']=id
            item['list_name']=name
            yield item
        