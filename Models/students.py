
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from .db import Base

# Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        
