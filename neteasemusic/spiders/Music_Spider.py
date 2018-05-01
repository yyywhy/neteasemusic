# -*- coding: utf-8 -*-
#'http://music.163.com/api/v1/resource/comments/R_SO_4_543987400?limit=20&offset=0'
import scrapy
import re
import json
import MySQLdb
from neteasemusic.items import NeteaseMusicItem
class MusicSpider(scrapy.Spider):
    name = 'Music_Spider'
    allowed_domains = ['music.163.com']
    names=[]
    start_urls = []
    tables=[]
    tables2=[]
    comments=[]
    conn=MySQLdb.connect(host='localhost',
        port=3306,
        user='yyywhy',
        passwd='135156',
        db='musiccomments',
        charset='utf8')
    cur=conn.cursor()
    cur.execute('show tables')
    val=cur.fetchall()
    val=list(val)
    for i in val:
        if i[0]!='billboard' and i[0].find('remarkings')<0:
            tables.append(i[0])
    j=0
    for table in tables:
        cur.execute("select song_id,song_name from %s" %table)
        song_info=cur.fetchall()
        for i in xrange(0,len(song_info)):
            url=song_info[i][0]
            url='http://music.163.com/api/v1/resource/comments/R_SO_4_%s?limit=100&offset=0' %url
            start_urls.append(url)
            names.append(song_info[i][1])   
            tables2.append(table) 
            #print j,table
            j=j+1
    #print(len(tables))
    '''    for i in xrange(0,101):
        print start_urls[i],names[i],tables2[i]'''
    '''for i in xrange(0,100):
        print tables2[i]        '''

    def start_requests(self):
        for i in xrange(1000,1238):
            now={"comments":[{"commentId":-1}]}
            offset=0
            song_name=self.names[i]
            table_name=self.tables2[i]
            song_id=self.start_urls[i]
            url=self.start_urls[i]
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True,meta\
                                 ={'now':now,'offset':offset,'song_name':song_name,\
                                   'table_name':table_name,'song_id':song_id})
            #f1=Request(url=url,callback=self.parse,dont_filter=True)
    def parse(self,response):
        #print self.song_id,self.song_name,self.table_name
        url=response.url
        now=response.meta['now']
        offset=response.meta['offset']
        song_name=response.meta['song_name']
        table_name=response.meta['table_name']
        song_id=response.meta['song_id']
        js=json.loads(response.body)
        #j=self.start_urls.index(url)
        if len(js['comments'])==0 or offset>=2000:
            print 'a',offset
            return
        if now['comments'][0]['commentId'] == js['comments'][0]['commentId']:
            print 'b',offset
            return
        offset += 100
        aa = re.findall('offset=\d+', url)
        url = url.replace(aa[0], 'offset=')
        url = url + str(offset)
        now = js
        if js.has_key('hotComments'):
            for i in xrange(0, len(js['hotComments'])):
                item = NeteaseMusicItem()
                item['comments']=js['hotComments'][i]['content']
                item['song_name']=song_name
                item['song_id']=song_id
                item['song_table']=table_name
                item['song_table']=item['song_table'].replace('榜','Remarkings',1)
                yield item
        for i in xrange(0,len(js['comments'])):
            item=NeteaseMusicItem()
            item['comments']=js['comments'][i]['content']
            item['song_name']=song_name
            item['song_id']=song_id
            item['song_table']=table_name
            item['song_table']=item['song_table'].replace('榜','Remarkings',1)
            yield item  
        print "fengexian"
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=True,meta\
                                     ={'now':now,'offset':offset,'song_name':song_name,\
                                       'table_name':table_name,'song_id':song_id})

        

            
            
        