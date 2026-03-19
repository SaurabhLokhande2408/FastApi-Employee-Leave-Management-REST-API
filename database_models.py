from sqlalchemy import Column,Integer,String,Float
from database import engine,SessionLocal
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()#parent class for all tables



#database models used for db

class Leave_request(Base):
    __tablename__ = "leave_requests"
    id = Column(Integer, primary_key=True, index=True)  
    name=Column(String,nullable=False)
    department=Column(String,nullable=False)
    reason=Column(String,nullable=False)
    total_leaves=Column(Integer,nullable=False)

