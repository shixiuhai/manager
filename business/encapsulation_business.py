import pandas as pd
from enum import Enum
import datetime
import time
import os
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
        pass
    # 列出需要导入的文件名称
    def list_excel_fileNames(self):
        for root,dirs,fileNames in os.walk("excel_files"):
            for fileName in fileNames:
                print("=====%s=====\n"%fileName)
    # 导入excel方法
    def import_excel(self,skiprows=1):
        print("""
                ===============请选择你要导入的excel文件===============
                ===============1. 导入学生成绩=========================
                ===============2. 导入老师信息=========================
                  """)
        importExcelType=int(input("请输入数字: "))
        if  importExcelType==1:
            # 列出excel文件名称
            self.list_excel_fileNames()
            importExcelName=input("请输入excel文件名称: ")
            df = pd.read_csv("excel_files"+"/"+importExcelName, skiprows=skiprows)
        if  importExcelType==2:
            pass
        # time.sleep(10000)
        df = pd.read_csv("excel_files"+"/"+fileName, skiprows=skiprows)
        # row 取数据
        for index, row in df.iterrows():   
            # 时间 row[0]
            # IN流量 row[1]
            # OUT流量 row[2]
            """调用sql_execute插入数据"""
            # 进口数据插入
            created_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
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
    enBu.import_excel("ab")