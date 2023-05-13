import sys
# sys.path.append("operate_mysql")
# sys.path.append("business")
# sys.path.append("excel_files")
# print(sys.path)
from  business.encapsulation_business import EnBu
class MG:
    def __init__(self) -> None:
        self.enBu=EnBu()
    def print_start(self):
        print("----------------------------------start----------------------------------")
    def print_end(self):
        print("----------------------------------end----------------------------------")
    
    def main(self):
        while True:
            print("""
                    1. 导入sql
                    2. 分析成绩
                """)
            a=int(input("请输入你要做的事情: "))
            if a==1:
                self.enBu.import_excel("excel_files")
            elif a==2:
                self.enBu.analyzing_student_grades()


if __name__ == "__main__":
    mg=MG()
    mg.main()
    # enBu=EnBu()
    # enBu.import_excel(excelPath="excel_files")
    # enBu.select_user_information()
    # enBu.analyzing_student_grades()
  
        
        