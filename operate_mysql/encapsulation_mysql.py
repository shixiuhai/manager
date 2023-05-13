import pymysql
import pandas as pd
import datetime
import sys
sys.path.append("..")
class EnSql:
    def __init__(self,mysqlHost,mysqlUser,mysqlPassword,mysqlDatabase) -> None:
        # 创建一个数据库对象
        self.db=pymysql.connect(host=mysqlHost,
                                user=mysqlUser,
                                password=mysqlPassword,
                                database=mysqlDatabase)
    
    # 增加数据
    def insert_sql(self,sql:str):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as error:
            print(error)
            # 发生错误时回滚
            self.db.rollback()
        cursor.close()    
    # 删除数据
    def delete_sql(self,sql:str):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.db.rollback()
        cursor.close()
    # 修改数据
    def update_sql(self,sql:str):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        cursor.close()
    # 查询数据
    def select_sql(self,sql:str,type:str="list")->list:
        cursor = self.db.cursor()
        if type=="list":
            cursor.execute(sql)
            result=cursor.fetchall()
            return list(result)
            
        elif type=="one":
            cursor.execute(sql)
            result=cursor.fetchone()
            return [result]
        cursor.close()
if __name__ == "__main__":
    ensql = EnSql("localhost","root","sxh.200008","manager")
    s=ensql.select_sql("select * from m_students",type="one")
    ensql.insert_sql("insert into m_students(id,name,sex)  values ('%s','%s','%s')"%(5,"哈哈",1))
        
        

 
# 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='sxh.200008',
#                      database='manager')
 
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("select * from m_students")
 
# # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# data = cursor.fetchall()
# for item in data:
#     print(item)
 
# # 关闭数据库连接
# db.close()
    
   