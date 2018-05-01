# -*- coding: utf-8 -*-
import time
import neteasemusic.items
import MySQLdb
import re
class neteasemusicpipeline(object):
    def process_item(self, item, spider):
        if spider.name=='BillBoard_Spider':
            print(1)
            #print(spider.start_urls)
            id=item['list_id'].encode('utf8')
            name=item['list_name'].encode('utf8')
            name=name.replace(' ','')
            conn=MySQLdb.connect(
                host='localhost',
                port=3306,
                user='yyywhy',
                passwd='135156',
                db='MusicComments',
                charset='utf8')
            cur=conn.cursor()
            cur.execute("insert ignore into billboard(list_id,list_name) values(%s,%s)",(id,name))
            cur.execute("create table if not exists %s(id int primary key auto_increment,song_id varchar(50) unique key,song_name varchar(50))" %name)
            conn.commit()
            cur.close()
            conn.close()
            return item
        if spider.name=='BoardSongs_Spider':
            id=item['song_id'].encode('utf8')
            name=item['song_name'].encode('utf8')
            table_name=item['song_table'].encode('utf8')
            #print(table_name)
            conn=MySQLdb.connect(
                host='localhost',
                port=3306,
                user='yyywhy',
                passwd='135156',
                db='MusicComments',
                charset='utf8')
            cur=conn.cursor()
            #print(type(table_name))
            #print(type('云音乐飙升榜'))
            #table_name='云音乐飙升榜'.encode('utf8')
            #sql=('create table if not exists %s (song_id,song_name) values(%s,%s)') %('ffff',id,name)
            cur.execute("insert   ignore %s    values  (null,'%s','%s') " %(table_name,id,name) )
            conn.commit()
            cur.close()
            conn.close()
            return item
        if spider.name=='Music_Spider':
            comments=item['comments'].encode('utf8')
            tab=item['song_table'].encode('utf8')
            song_id=item['song_id'].encode('utf8')
            song_name=item['song_name'].encode('utf8')
            #print comments,tab,song_id,song_name
            conn=MySQLdb.connect(
                host='localhost',
                port=3306,
                user='yyywhy',
                passwd='135156',
                db='MusicComments',
                charset='utf8')
            cur=conn.cursor()
            #print("1111111111")
            tab=tab.replace(' ','')
            cur.execute("create table if not exists %s(id int primary key auto_increment,\
                        song_id varchar(50),song_name varchar(50),content varchar(1000) unique key)" %tab)
            #print("bbbbbbbbbbbb")
            cur.execute("insert ignore into %s values (null,'%s','%s','%s')" %(tab,song_id,song_name,comments))
            conn.commit()
            cur.close()
            conn.close()
            
             
