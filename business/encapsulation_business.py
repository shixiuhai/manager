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
        # 创建一个操作mysql的对象
        self.enSql=EnSql('localhost','root','sxh.200008','manager')
    
    # 列出需要导入的文件名称
    def list_excel_fileNames(self,excelPath)->list:
        fileNamesList=[]
        for root,dirs,fileNames in os.walk(excelPath):
            count=1
            for fileName in fileNames:
                print("=====%s. %s =====\n"%(count,fileName))
                count+=1
                fileNamesList.append(fileName)
            return fileNamesList
    
    # 
    def import_excel(self,excelPath,skiprows=0):
        print("""
                ===============请选择你要导入的excel文件===============
                ===============1. 导入学生成绩=========================
                ===============2. 导入老师信息=========================
                  """)
        importExcelType=int(input("请输入数字: "))
        if  importExcelType==1:
            # 列出excel文件名称
            fileNameList=self.list_excel_fileNames(excelPath=excelPath)
            indexNumber=int(input("请输入文件标号: "))
            importExcelName=fileNameList[indexNumber-1]
            df = pd.read_excel(excelPath+"/"+importExcelName, skiprows=skiprows)
            print(df)
            # row 取数据
            # 按照行遍历
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
                # print(self.enSql.select_sql("select * from m_students")) 
                # 将每一行数据放入元组中
                insertData=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],created_time)
                print(insertData)
                self.enSql.insert_sql("replace into m_students \
                (name,sex,chinese_score,math_score,\
                english_score,physics_score,politics_score,\
                chemical_score,biological_score,geography_score,\
                class_name,remark,created_time) values ('%s','%s',\
                '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%insertData)
        
        if  importExcelType==2:
            fileNamesList=self.list_excel_fileNames(excelPath)
            # a/b/c / 3.excel a/b 3.excel a/b+"/" +3.excel
            indexNumber=int(input("请输入文件标号: "))
            df = pd.read_excel(excelPath+"/"+fileNamesList[indexNumber-1])
            print(df)
    
    # 维度班级维度或者个人维度
    # 分析成绩 按照月份分析 针对某个学生总分，针对某个学生单科成绩，针对某个班级单科平均分
    def analyzing_student_grades(self):
        print("""
                    ===============1. 按照学生维度分析=========================
                    ===============2. 按照班级维度分析=========================
            """)
        analyzingType=int(input("请输入的需要分析的成绩维度数字: "))
        if analyzingType==1:
            # SELECT name, AVG(chinese_score+math_score) from m_students where created_time BETWEEN '2023-01-13' and '2023-06-13' GROUP BY name;
            # SELECT class_name, AVG(chinese_score) from m_students where created_time BETWEEN '2023-01-13' and '2023-06-15 ' GROUP BY class_name;
            year=input("请输入年份: ") # 2023
            startMonth=input("请输入开始月份: ")# 1
            endMonth=input("请输入结束月份: ")# 2
            # 2023-01-01 # 时间段
            startTime=year+"-"+startMonth+"-01"
            endTime=year+"-"+endMonth+"-01"
            # print(startTime,endTime)
            print("""======
                1. chinese_score
                2. math_score
                3. english_score
                4. physics_score
                5. chemical_score
                6. biological_score
                7. geography_score
                8. politics_score
                =======""")
            courseList=["chinese_score","math_score","english_score","physics_score","chemical_score","biological_score","geography_score","politics_score"]
            inputCourseIndexList=input("请输入你需要分析的学科维度按照,号分割: ").split(",")
            courseNames=""
            for indexStr in inputCourseIndexList:
                print(indexStr)
                courseNames=courseNames+courseList[int(indexStr)-1]+"+"
            sql="SELECT name, AVG(%s) from m_students where created_time BETWEEN '%s' and '%s' GROUP BY name"%(courseNames[:-1:],startTime,endTime)
            results=self.enSql.select_sql(sql)
            self.process_print_information(results,{"成绩","平均分"})
            print(results)
        if analyzingType==2:
            pass
    # 维度班级维度或者个人维度
    # 排名（设置排名维度，按照总分排名，按照单科成绩排名）
    def student_grades_ranking(self):
        pass
    # 增加某个学生或者老师的信息 完整字段插入
    def insert_user_information(self):
        pass
    # 处理查询出的用户信息，希望他按照表格展示
    def process_print_information(self,results,titles):
        pass
    # 查询某个学生或者老师信息 查询完整信息包括id (name,class_name)
    def select_user_information(self):
        print("""
                ===============1. 查询学生信息=========================
                ===============2. 查询老师信息=========================
         """)
        selectType=int(input("请输入查询类别索引: "))
        if selectType==1:
            name=input("请输入学生姓名: ")
            className=input("请输入学生的班级: ")
            results=self.enSql.select_sql("select * from m_students where name='%s' and class_name='%s'"%(name,className))
            print(results)
        if selectType==2:
            name=input("请输入老师姓名: ")
            className=input("请输入老师的班级: ")
            reuslts=self.enSql.select_sql("select * from ")
            
    # 修改某个学生或者老师的信息 (id) 需要查询
    def modify_user_information(self):
        pass
        # 1. 维度学生或者老师
        # 2. 输入名字 查询 获取id
        # 3. 输入需要修改的字段 和 id
        # 4. 更据 id 进行update
        # self.enSql.update_sql("update m_students set %s='%s' where id='%s'"%("name","小张",123))
    
    # 删除某个老师或者某个学生的信息 (id) 需要查询
    def delete_user_informaition(self):
        pass

if __name__ == "__main__":
    enBu=EnBu()
    enBu.import_excel("../excel_files")