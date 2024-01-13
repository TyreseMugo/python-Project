import click
from Models.students import Student
from Models.enrollment import Enrollment
from Models.teachers import Teacher
from Models.room import Classroom
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Configure the database engine
DATABASE_URL = "sqlite:///class_management.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Class Management System CLI."""
    pass

@cli.command()
@click.option("--name", prompt="Student Name", help="Name of the student")
def enroll_student(name):
    """Enroll a new student."""
    session = Session()
    student = Student(name=name)
    session.add(student)
    session.commit()
    click.echo(f"Student {name} enrolled successfully.")

@cli.command()
def list_students():
    """List all students."""
    session = Session()
    students = session.query(Student).all()
    for student in students:
        click.echo(f"Student ID: {student.id}, Name: {student.name}")

@cli.command()
@click.option("--name", prompt="Teacher Name", help="Name of the teacher")
def hire_teacher(name):
    """Hire a new teacher."""
    session = Session()
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    click.echo(f"Teacher {name} hired successfully.")

@cli.command()
def list_teachers():
    """List all teachers."""
    session = Session()
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        click.echo(f"Teacher ID: {teacher.id}, Name: {teacher.name}")

@cli.command()
@click.option("--name", prompt="Classroom Name", help="Name of the classroom")
def create_classroom(name):
    """Create a new classroom."""
    session = Session()
    classroom = Classroom(name=name)
    session.add(classroom)
    session.commit()
    click.echo(f"Classroom {name} created successfully.")

@cli.command()
def list_classrooms():
    """List all classrooms."""
    session = Session()
    classrooms = session.query(Classroom).all()
    for classroom in classrooms:
        click.echo(f"Classroom ID: {classroom.id}, Name: {classroom.name}")

if __name__ == "__main__":
    cli()
