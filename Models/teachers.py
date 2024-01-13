
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from .db import Base

# Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    

    def display_info(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        
