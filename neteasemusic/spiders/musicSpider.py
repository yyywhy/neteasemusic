# -*- coding: utf-8 -*-
import scrapy


class MusicspiderSpider(scrapy.Spider):
    name = 'musicSpider'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        pass
