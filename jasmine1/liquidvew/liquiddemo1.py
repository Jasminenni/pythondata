# 导入sql模块
import  pymysql as pm

def queryEmpSalary(*args):
    conn=pm.connect(host="127.0.0.1",port=3306,database="demo1",user="root",password="123",charset="utf8")
    print(conn)
    objcu=conn.cursor()
    sql="SELECT FORMAT( e_salary/(SELECT SUM(e_salary+IFNULL(e_money,0) ) " \
        "FROM t_emp),2) FROM t_emp WHERE e_name=%s "
    objcu.execute(sql,args)
    datas = objcu.fetchone()
    print(datas)
    if datas is None:
        return None
    else:
        # 这个方法返回计算的值
        return datas[0]
# data=queryEmpSalary("陈大炮")
# print(data)
