from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Enrollment(Base):
    __tablename__ = 'enrollments'

    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    class_id = Column(Integer, ForeignKey('classes.class_id'))
    enrollment_date = Column(Date)

    student = relationship('Student', back_populates='enrollments')
    enrolled_class = relationship('Classroom', back_populates='enrollments')

    def display_info(self):
        print(f"Enrollment ID: {self.enrollment_id}")
        print(f"Student ID: {self.student_id}")
        print(f"Class ID: {self.class_id}")
        print(f"Enrollment Date: {self.enrollment_date}")
