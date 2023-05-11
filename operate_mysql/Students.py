# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MStudent(Base):
    __tablename__ = 'm_students'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255, 'utf8mb4_bin'), comment='学生姓名')
    sex = Column(Integer, comment='学生性别 1 男，2女')
    chinese_score = Column(String(255, 'utf8mb4_bin'), comment='语文成绩')
    math_score = Column(String(255, 'utf8mb4_bin'), comment='数学成绩')
    english_score = Column(String(255, 'utf8mb4_bin'), comment='英语成绩')
    physics_score = Column(String(255, 'utf8mb4_bin'), comment='物理成绩')
    biological_score = Column(String(255, 'utf8mb4_bin'), comment='生物成绩')
    class_name = Column(String(255, 'utf8mb4_bin'), comment='班级名称')
    remark = Column(String(255, 'utf8mb4_bin'), comment='同名备注区分')
    created_time = Column(DateTime, comment='成绩录入时间')
