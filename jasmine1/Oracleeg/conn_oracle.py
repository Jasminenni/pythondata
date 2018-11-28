import cx_Oracle as orc

# 连接数据库

def selectAll():
    conn=orc.connect("student/student@127.0.0.1/XE")
    print(conn)

    sql="select * from t_stus"
    curobj=conn.cursor()

    curobj.execute(sql)
    data=curobj.fetchall();
    print(data)

def selectCount():
    conn=orc.connect("student/student@127.0.0.1/XE")
    # print (conn)

    sql="select count(*) from t_stus"
    curobj=conn.cursor()
    curobj.execute(sql)
    data=curobj.fetchone()
    print(data)   #[(4),]
    print("%s"%(data))  #[(4),]
    print("{0}".format(data))       #  4 #打印出来直接是值，不是元祖
# selectCount()

def selectNamePwd(name,pwd):
    conn=orc.connect("student/student@127.0.0.1/XE")
    sql="select count(*) from t_stus where tname=:name and trim(tpwd)=:pwd"
    curcor=conn.cursor()
    params={"name":name,"pwd":pwd}
    curcor.execute(sql,params)
    data=curcor.fetchone()
    print("%s"%(data))

selectNamePwd("Mary","666666")

# 从数据库中查询几行几列
def queryPage(pageNum):
    conn=orc.connect("student/student@127.0.0.1/XE")
    cursor1=conn.cursor()
    sql="select  *  from (select  rownum  rm,  e.*    from   t_stus  " \
        "e  where rownum<=:endnum) temp  where  temp.rm>:startnum"
    prams={"endnum":pageNum*2,"startnum":(pageNum-1)*2}

    cursor1.execute(sql,prams)
    data=cursor1.fetchall()
    print(data)

    for value in data:
        print("{0}".format(value))
queryPage(1)
