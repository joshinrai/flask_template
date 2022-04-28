from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class UserBean(Base):
    __tablename__ = 'tb_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    truename = Column(String(255))
    email = Column(String(255))
    role = Column(String(255))