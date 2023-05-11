from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Students import MStudent
# sqlacodegen --tables m_students --outfile Students.py mysql+pymysql://root:sxh.200008@127.0.0.1:3306/manager?charset=utf8


engine = create_engine('mysql+pymysql://root:sxh.200008@localhost:3306/manager')
# 把当前的引擎绑定给这个会话
Session = sessionmaker(bind=engine)
# 实例化
session = Session()


# all = session.query(MStudent.name,MStudent.sex).filter(MStudent.name=="张三").all()
all = session.query(MStudent).all()
print(all)
for item in all:
    print(item.name,item.sex)