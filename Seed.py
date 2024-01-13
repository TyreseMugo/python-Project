import random
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Models.students import Student
from Models.teachers import Teacher
from    Models.room import Classroom

DATABASE_URL = "sqlite:///class_management.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def seed_students():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    with Session() as session:
        for name in names:
            student = Student(name=name)
            session.add(student)
        session.commit()

def seed_teachers():
    names = ["Mr. Smith", "Mrs. Johnson", "Dr. Brown"]
    with Session() as session:
        for name in names:
            teacher = Teacher(name=name)
            session.add(teacher)
        session.commit()

def seed_classrooms():
    locations = ["Room A", "Room B", "Room C"]
    with Session() as session:
        for location in locations:
            classroom = Classroom(name=location)
            session.add(classroom)
        session.commit()

def seed_enrollments():
    with Session() as session:
        students = session.query(Student).all()
        teachers = session.query(Teacher).all()
        classrooms = session.query(Classroom).all()

        for student in students:
            teacher = random.choice(teachers)
            classroom = random.choice(classrooms)
            enrollment_date = datetime.now() - timedelta(days=random.randint(1, 30))

            enrollment = enrollment(student_id=student.student_id, class_id=classroom.class_id, enrollment_date=enrollment_date)
            session.add(enrollment)

        session.commit()

if __name__ == "__main__":
    seed_students()
    seed_teachers()
    seed_classrooms()
    seed_enrollments()
    print("Seed data added successfully.")
