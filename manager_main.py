import sys
sys.path.append("operate_mysql")
sys.path.append("business")
sys.path.append("excel_files")
from  business.encapsulation_business import EnBu
class MG:
    def __init__(self) -> None:
        self.enBu=EnBu()
    # @property
    def print_start(self):
        print("----------------------------------start----------------------------------")
    def print_end(self):
        print("----------------------------------end----------------------------------")
        
    
        
        