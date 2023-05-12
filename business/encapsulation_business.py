import pandas as pd
from enum import Enum
import datetime
import os
import sys
sys.path.append("..")
from  operate_mysql.encapsulation_mysql import EnSql
class Subject(Enum):
    chinese = 1
    math = 2
    english = 3
    physics = 4
    chemical = 5
    biological = 6
    geography = 7
    politics = 8

class EnBu:
    def __init__(self) -> None:
        self.enSql=EnSql('localhost','root','sxh.200008','manager')
    # 列出需要导入的文件名称
    def list_excel_fileNames(self,excelPath):
        fileNamesList=[]
        for root,dirs,fileNames in os.walk(excelPath):
            for fileName in fileNames:
                print("===== %s =====\n"%fileName)
    # 导入excel方法
    def import_excel(self,excelPath,skiprows=1):
        print("""
                ===============请选择你要导入的excel文件===============
                ===============1. 导入学生成绩=========================
                ===============2. 导入老师信息=========================
                  """)
        importExcelType=int(input("请输入数字: "))
        if  importExcelType==1:
            # 列出excel文件名称
            self.list_excel_fileNames(excelPath=excelPath)
            importExcelName=input("请输入excel文件名称: ")
            df = pd.read_excel(excelPath+"/"+importExcelName, skiprows=skiprows)
            print(df)
            # row 取数据
            for index, row in df.iterrows():   
                # 进口数据插入
                created_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # name row[0]
                # sex row[1]
                # chinese_score row[2]
                # math_score row[3]
                # english_score row[4]
                # physics_score row[5]
                # chemical_score row[6]
                # biological_score row[7]
                # geography_score row[8]
                # politics_score row[9]
                # class_name row[10]
                # remark row[11]
                # created_time row[12]
                """调用sql_execute插入数据"""
                print(self.enSql.select_sql("select * from m_students"))
                
                
        if  importExcelType==2:
            pass
        # time.sleep(10000)
        df = pd.read_csv("excel_files"+"/"+fileName, skiprows=skiprows)
        
    
    # 录入成绩（excel进行成绩录入）
    def import_student_grades(self):
        pass
    
    # 维度班级维度或者个人维度
    # 分析成绩 按照月份分析 针对某个学生总分，针对某个学生单科成绩，针对某个班级单科平均分
    def analyzing_student_grades(self):
        pass
    
    # 维度班级维度或者个人维度
    # 排名（设置排名维度，按照总分排名，按照单科成绩排名）
    def student_grades_ranking(self):
        pass
    
    # 增加某个学生或者老师的信息 完整字段插入
    def insert_user_information(self):
        pass
    
    # 查询某个学生或者老师信息 查询完整信息包括id (name,class_name)
    def select_user_information(self):
        pass
    
    # 修改某个学生或者老师的信息 (id) 需要查询
    def modify_user_information(self):
        pass
    
    # 删除某个老师或者某个学生的信息 (id) 需要查询
    def delete_user_informaition(self):
        pass

if __name__ == "__main__":
    enBu=EnBu()
    enBu.import_excel("../excel_files")