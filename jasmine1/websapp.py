#导入Python web应用框架，flask
from flask import Flask
from  flask import request
from dbface.dbface1 import *
from  flask import jsonify
from werkzeug.utils import secure_filename
import os
import  time

#创建flask应用对象
wxappliation=Flask(__name__)

@wxappliation.route("/face")
def queryFaceI():
    name=request.args.get("username")

    data = queryFaceImgPath(name)
    #print(data)
    userInfo={}
    userInfo["eface"] ="http://hv9ugr.natappfree.cc/static"+ data[8]
    userInfo["esex"]=data[4]
    userInfo["ephone"] = data[3]
    userInfo["eaddress"] = data[7]
    userInfo["emoney"] = data[5]
    userInfo["eimg"] ="http://hv9ugr.natappfree.cc/static"+data[10]
    userInfo["empctil"] = data[13]
    userInfo["eauthor"] = data[14]
    userInfo["empc"] = "http://hv9ugr.natappfree.cc/static"+data[11]
    userInfo["evideo"] ="http://hv9ugr.natappfree.cc/static"+ data[12]
    # userImgPath="http://24uaum.natappfree.cc/static"+userImgPath

    print(userInfo)

    return jsonify({"imgpath":userInfo})
    # print(name)


@wxappliation.route("/music")
def queryImgMucPath():
    authorName=request.args.get("mAuthor")
    authorMpath=queryMucPath(authorName)
    print(authorMpath)
    # print(authorMpath[2])
    titlePath="http://b8skdg.natappfree.cc/"+authorMpath[2]

    aorMpath="http://b8skdg.natappfree.cc/staic"+authorMpath[3]
    athMucPath="http://b8skdg.natappfree.cc/audio/"+authorMpath[4]
    # print(authorMpath)
    return jsonify({"titPath":titlePath,"ImgPath":aorMpath,"MucPath":athMucPath})

# @wxappliation.route("/login")
# def queryName():
#     name=request.args.get("username")
#     name=queryDBname(name)
#     print(name)


@wxappliation.route("/stuInfo")
def queryStuInfo():
    print("获取学生信息！")
    datas=queryDBemail()
    print(datas)
    stuInfo=[]
    for value in datas:
        # print(value)
        studata = {}
        studata["name"]=value[0]
        studata["phone"] = value[1]
        studata["email"] = value[2]
        studata["img"] = "http://b6j4az.natappfree.cc/static/user/"+value[3]
        stuInfo.append(studata)
    # print(stuInfo)
# queryStuInfo()

    return  jsonify({"stuData":stuInfo})


@wxappliation.route("/queryMail")
def  queryMail():
    print("接收发送邮件的参数！")

    mail=request.args.get("email")
    title=request.args.get("etitle")
    content=request.args.get("econtent")

    print(mail,title,content)
    sendEmail(mail,title,content)
    return jsonify({"flag":"发送成功"})



@wxappliation.route("/lunbo")
def queryImg():
    print("接收用户发起的请求！")

    navimg=[]
    navimg.append("http://b6j4az.natappfree.cc/static/user/aaa.jpg")
    navimg.append("http://b6j4az.natappfree.cc/static/user/bbb.jpg")
    navimg.append("http://b6j4az.natappfree.cc/static/user/ccc.jpg")
    print(navimg)

    codeValue=codeRandom(4)
    return jsonify({"navImg":navimg,"codeValue":codeValue})
# queryImg()

@wxappliation.route("/recode")
def queryCode():
    print("重置验证码")

    codeValue=codeRandom(4)
    return jsonify(codeValue)

@wxappliation.route("/namePwd")
def queryNamePwd():
    # print("接收客户端传送的姓名和密码！")
    name=request.args.get("name")
    pwd = request.args.get("pwd")
    # print(name,pwd)
    result=stuLogin(name,pwd)

    return  jsonify({"checklog":result})


@wxappliation.route("/uploadfiles",methods=["POST","GET"])
def imgOnload():
    # print("接收客户端发起的上传图片的路径！")
    if request.method=="POST":
        # 获取用户请求的参数
        loadImgPath=request.files["fileimg"]
        print(loadImgPath)

    #     获取文件上传名
        upFileName=loadImgPath.filename
        # print("获得上传的文件名：",upFileName)

    #     获取图片后缀名
        splitNames=os.path.splitext(upFileName)
        # print("获取到的图片的后缀名：",splitNames[1])

    #   文件名怎么正确命名 1.文件名不能一样 ymdhms_4位随机数.后缀名
    #     print("现在的时间", time.localtime(time.time()))

        timeName=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        # print(timeName)

        # 新的文件名
        newTimeName=timeName+splitNames[1]
        # print("新的文件名：",newTimeName)

        # 1.上传目录   2.插入数据库
        # 获取你所在服务器的目录

        basePath=os.path.dirname(__file__)
        # print("所在的目录：",basePath)

        saveFilePath=os.path.join(basePath,"static/userimg",secure_filename(newTimeName))
        # print('',saveFilePath)
        ImgPath=loadImgPath.save(saveFilePath)


        return jsonify({"ImgPath":newTimeName})

@wxappliation.route("/name")
def queryName():
    # print("接收客户端发起的姓名查询")

    name=request.args.get("sqlname")
    rename=StuName(name)

    return  jsonify({"resqlname":rename})

@wxappliation.route("/zhuce")
def queryZhuce():
    print("接收到客户端发起的请求，请求注册！")

    name=request.args.get("sqlname")
    pwd=request.args.get("sqlpwd")
    sex=request.args.get("sex")
    static = request.args.get("state")
    print(name,pwd,sex,static)

    adate=AddData(name,pwd,sex,static)

    # print("---->"+adate)
    return  jsonify(adate)




#找到flask的应用入口
if __name__=="__main__":
    wxappliation.run(debug=True,port=8086)


# img=request.args.get("image")img