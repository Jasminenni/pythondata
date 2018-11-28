import  pymysql as pmc

def queryEmpEexCount(*args):
    conn=pmc.connect(host="127.0.0.1",port=3306,database="demo1",user="root",password="123",charset="utf8")
    objcur=conn.cursor()
    sql="select count(*),e_sex from t_emp group by e_sex"
    objcur.execute(sql,args)
    data=objcur.fetchall()
    print(data)
    return data

