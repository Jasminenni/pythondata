# 导入SQL模块
import  pymysql
import  yagmail
import  random

def  conDb():
    conn = pymysql.connect(host="127.0.0.1", port=3306, database="demo1", user="root", password="123", charset="utf8")
    return  conn


# 构造函数
def  queryFaceImgPath(*args):
    DB=conDb()
    objcur=DB.cursor()
    sql="SELECT * FROM t_emp WHERE e_name = %s"
    objcur.execute(sql,args)
    data = objcur.fetchone()
    datanull=("无","无","无","无","无","无","无","无","/user/null.png","无","/user/music1.jpg","/audio/a1.mp3","/video/a1.mp4","三生三世","万辰")
    if  data is None:
        return datanull
    else:
        return data
    # print(data)


# queryFaceImgPath("孙婕")

def queryMucPath(*args):
    #Connect() 方法来创建数据库的连接
    DB = conDb()
    objcu=DB.cursor()
    sqld="SELECT * FROM t_muc WHERE m_author = %s"
    objcu.execute(sqld,args)
    databas=objcu.fetchall()
    # print(databas[0])

    list=[]
    for value in databas:
        # print(value)
        for datas in value:
            list.append(datas)
    # print(list)
    return  list
# queryMucPath("万辰")

# 学生登录数据
def queryDBname(*args):
    DB = conDb()
    objcur=DB.cursor()
    sql="SELECT count(*) FROM t_phmail where p_name=%s"
    objcur.execute(sql,args)
    data=objcur.fetchone()
    # print(data[0])
    # return data[0]


def queryDBemail(*args):
    DB = conDb()
    objcur=DB.cursor()
    sql="SELECT p_name,p_phone,p_email,p_img FROM t_phmail"
    objcur.execute(sql,args)
    data=objcur.fetchall()
    # print(data)
    return data


# queryDBemail()

def sendEmail(mail,title,content):
    mailsend=yagmail.SMTP(user="2920786643@qq.com",password="vlwgvdlfuaeqdhdb",host="smtp.qq.com")
    mailsend.send(mail,title,content)
    print("发送邮件！")


def  codeRandom(codeLen):
    codeValue=[]

    # 利用随机函数生成随机数
    while (len(codeValue) < codeLen):
        code = random.randint(0, 9)

        # 判断生成的随机数是否有重复的
        if code not in codeValue:
            codeValue.append(code)
    print(codeValue)
    codeStr=""
    for item in codeValue:
        codeStr+=str(item)
    print(codeStr)

    return  codeStr


def  stuLogin(sname,spwd):
    resultMess=""
    DB = conDb()
    objcur=DB.cursor()
    sql="SELECT state FROM t_stus WHERE sname=%s AND spwd=%s"
    objcur.execute(sql,(sname,spwd))
    result=objcur.fetchone()

    print(result)
# stuLogin("袁信莉", "123456")
# stuLogin("Jenny","123456")
    if result is None:
        resultMess="None"
        # print("没有这个学生！")

    else:
        if result[0] == 1:
             # 继续查询数据库
            sql="SELECT   cname FROM  t_classes   WHERE cid =(SELECT  scid  FROM  t_stus  WHERE sname=%s)"
            objcur.execute(sql,(sname))
            resultdb=objcur.fetchone()
            # print(resultdb[0])
            resultMess="在学"
# stuLogin("Jone", "123456")
        else:
            if result[0]==2:
                resultMess="毕业"
            else:
                resultMess="休学"
    return  resultMess

def StuName(name):
    DB = conDb()
    objcur = DB.cursor()
    sql="SELECT COUNT(*) FROM t_Stus WHERE sname=%s"

    objcur.execute(sql,name)
    datas=objcur.fetchone()

    # print(datas[0])
    return datas[0]
# StuName("Jasmine")

def AddData(sname,spwd,ssex,state):
    DB = conDb()
    objcur = DB.cursor()
    sql="INSERT INTO t_stus (sname,spwd,ssex,state)VALUES(%s,%s,%s,%s) "
    result=objcur.execute(sql,(sname,spwd,ssex,state))
    DB.commit()
    # print(result)
    return result
