# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
import traceback 
from neteasemusic.items import NeteaseMusicItem
from operator import index

class BoardsongsSpiderSpider(scrapy.Spider):
    name = 'BoardSongs_Spider'
    allowed_domains = ['music.163.com']
    start_urls=[]
    names=[]
    conn=MySQLdb.connect(
                host='localhost',
                port=3306,
                user='yyywhy',
                passwd='135156',
                db='MusicComments',
                charset='utf8')
    cursor=conn.cursor()
    cursor.execute('select * from billboard')
    values=cursor.fetchall()
    values=list(values)      
    for i in values:
        url='http://music.163.com/discover/toplist?id=%s' %i[1]
        start_urls.append(url)
        names.append(i[2])
    #将billboard表中的榜单id转化为url，以供爬虫爬取
    #print(start_urls)
    #print(names)
    conn.commit()
    cursor.close()
    conn.close()
    def start_requests(self):
        #print "1"
        for j in xrange(0,len(self.start_urls)):
            #global index
            #index=i
            #print index
            #print self.index,self.names[self.index],self.start_urls[i] 
            yield scrapy.Request(url=self.start_urls[j],callback=self.parse)
    def parse(self, response):
        dex=self.start_urls.index(response.url)
        table_name=self.names[dex]
        #print(response.url)
        for t in response.xpath('//ul[@class="f-hide"]/li/a'):
            item=NeteaseMusicItem()
            tt=t.re('id=\d+')
            song_id=tt[0].replace('id=','')
            song_name=t.xpath('./text()').extract()
            song_name=song_name[0]
            #print(song_name)
            item['song_id']=song_id
            item['song_name']=song_name
            item['song_table']=table_name
            yield item
# print(index)
        pass
