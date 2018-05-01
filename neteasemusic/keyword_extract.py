#coding:utf8
import MySQLdb
import thulac
import time
def extract():
    conn=MySQLdb.connect(
        port=3306,
        user='yyywhy',
        passwd='135156',
        host='localhost',
        db='MusicComments',
        charset='utf8'
    )
    thu1 = thulac.thulac(filt=True) 
    cur=conn.cursor()
    cur.execute("show tables like '%remarkings%'")
    val=cur.fetchall()
    tables=[]
    for i in val:
        tables.append(i[0])
    for table in tables:
        print time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
        split_points=[]
        sorted_dict=[]
        dict2=[]
        dict3=[]
        dict4=['歌','人','时候','爱心','感觉','声音','音乐','专辑','歌词','家']
        dict={}
        cur.execute("select content from %s " %table)
        val=cur.fetchall()
        for content in val:
            comment=content[0]
            comment=comment.replace(' ','')
            text = thu1.cut(comment, text=False)   
            for i in text:
                if i[1]!='n':
                    continue
                keyword=i[0]
                if keyword==' ':
                    continue
                if keyword in dict4:
                    continue
                if dict.get(keyword)!=None:
                    dict[keyword]+=1
                else :
                    dict[keyword]=1
        print time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
        t=dict.items()
        len_t=len(t)
        split_points.append(0)
        ss=0
        for i in xrange(0,99):
            ss+=len_t/100
            split_points.append(ss)
        split_points.append(len_t-1)
        for i in xrange(0,100):
            ss=split_points[i]
            ee=split_points[i+1]
            sorted_dict.append(sorted(dict.items()[ss:ee+1], key=lambda e:e[1], reverse=True))
        #sorted_dict=sorted(dict.items(), key=lambda e:e[1], reverse=True)
        
        for i in xrange(0,100):
            for j in xrange(0,10):
                dict2.append(sorted_dict[i][j])
        dict3=sorted(dict2, key=lambda e:e[1], reverse=True)
        name=table.replace('remarkings','')
        with open(name+'keyword.txt','a')as fp:
            for i in xrange(0,10):
                fp.write(dict3[i][0])
        print time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
if __name__=='__main__':
    extract()
        
    
                    
                
            
        
    
    