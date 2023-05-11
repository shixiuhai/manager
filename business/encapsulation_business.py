import pandas as pd
import datetime
class EnBu:
    def __init__(self) -> None:
        pass
     # 导入excel方法
    def import_excel(self,filePath,skiprows=1):
        df = pd.read_csv("excel_files"+"/"+filePath, skiprows=skiprows)
        # row 取数据
        for index, row in df.iterrows():   
            # 时间 row[0]
            # IN流量row[1]
            # OUT流量row[2]
            """调用sql_execute插入数据"""
            # 进口数据插入
            created_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 录入成绩（excel进行成绩录入）
    def import_score(self):
        pass
    
    # 分析成绩 按照月份分析 针对某个学生总分，针对某个学生单科成绩，针对某个班级单科平均分
    
    
    # 排名（设置排名维度，按照总分排名，按照单科成绩排名）
    
    # 增加某个学生或者老师的信息 完整字段插入
    
    # 查询某个学生或者老师信息 查询完整信息包括id (name,class_name)
    def select_user_information(self):
        pass
    
    # 修改某个学生或者老师的信息 (id) 需要查询
    def modify_user_information(self):
        pass
    
    # 删除某个老师或者某个学生的信息 (id) 需要查询
    def delete_user_informaition(self):
        pass