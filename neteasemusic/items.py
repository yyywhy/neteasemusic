# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NeteaseMusicItem(scrapy.Item):
    list_id=scrapy.Field()
    list_name=scrapy.Field()
    song_id=scrapy.Field()
    song_name=scrapy.Field()
    song_table=scrapy.Field()
    comments=scrapy.Field()
    
