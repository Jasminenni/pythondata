# 导入Liquid模块
# from pyecharts import Liquid
# from liquidvew.liquiddemo1 import *
from pyecharts import Pie
from  liquidvew.pie1 import *


# name=input("请输入员工姓名：")
# data=queryEmpSalary(name)
# print("--------",data)
# if data  is  None:
#     print("用户名不存在")
# else:
#     lidatas = []
#     lidatas.append(data)
#     print(lidatas)
#
#  # 创建水球图对象0
#     liObj = Liquid("员工工资百分比图")
#
#     # liObj放入数据
#     liObj.add("人工工资占比", lidatas)
#
#     # 渲染到一个html页面
#     liObj.render(name + ".html")

datas=queryEmpEexCount()

peos=[]
adres=[]

for item in datas:
   adres.append(item[0])
   peos.append(item[1])
print(peos,adres)

piesex=Pie("hj")

piesex.add("hj",peos,adres)
piesex.render("a.html")


