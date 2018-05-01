#coding=utf8
import MySQLdb
import jieba
import jieba.posseg as pseg
import time
def extract():
    dict4=['歌','人','时候','爱心','感觉','声音','音乐','专辑','歌词','家']
    dict={}
    conn=MySQLdb.connect(
        port=3306,
        host='localhost',
        db='musiccomments',
        user='yyywhy',
        passwd='135156',
        charset='utf8'
    )
    cur=conn.cursor()
    cur.execute("show tables like '%remarkings%'")
    val=cur.fetchall()
    tables=[]
    for i in val:
        tables.append(i[0])
    for table in tables:
        #print table
        dict.clear()
        s=time.strftime("%y-%m-%d %H%M%S", time.localtime())
        cur.execute("select content from %s" %table)
        val=cur.fetchall()
        for content in val:
            comment=content[0]
            comment=comment.replace(' ','')
            words=pseg.cut(comment)
            for i,v in words:
                if i in dict4:
                    continue
                if v!='n' and v!='ns':
                    continue
                if dict.get(i)!=None:
                    dict[i]+=1
                else:
                    dict[i]=0
        sorted_dict=sorted(dict.items(), key=lambda e:e[1], reverse=True)
        #s='jieba_result/'+s+table+'.txt'
        #s=table+'.txt'
        s='总表'
        with open(s,'a') as fp:
            fp.write(table+':'+'\n')
            for i in xrange(0,10):
                 fp.write(sorted_dict[i][0]+' ')
            fp.write('\n')
if __name__=='__main__':
    ex=extract()
        