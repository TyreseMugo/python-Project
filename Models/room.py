from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class Classroom(Base):
    __tablename__ = 'classes'

    class_id = Column(Integer, primary_key=True)
    location = Column(String)
    status = Column(String)

    # Use a string for the relationship
    enrollments = relationship('Enrollment', back_populates='enrolled_class')

    def display_info(self):
        print(f"Class ID: {self.class_id}")
        print(f"Location: {self.location}")
        print(f"Status: {self.status}")
