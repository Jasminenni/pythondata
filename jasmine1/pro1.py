
#导入python web应用框架  flask
from flask import Flask
from flask import render_template
from flask import  jsonify

# 创建flask应用对象
wxapp=Flask(__name__)

@wxapp.route("/")
def checkLogin():
    print("执行登录")
    #flask框架为用户提供直接返回包含json格式数据响应的方法,即jsonify方法
    return  jsonify({"flag":"10"})

# 用户在客户端发起的请求
@wxapp.route("/")
def defaultView():
    print("1111111111111111")
    return  render_template("index.html")

# 找到flask应用的入口
if __name__=="__main__":
    wxapp.run(debug=True,port=8086)


