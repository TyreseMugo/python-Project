## Class Management System
This is a simple command-line interface (CLI) based Class Management System implemented in Python using SQLAlchemy. The system allows you to manage students, teachers, classrooms, and enrollments.

## Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/TyreseMugo/python-Project.git
cd class-management-system
Install Dependencies:

 bash
Copy code
pip install -r requirements.txt
Database Setup:

The system uses SQLite as the default database. If you want to use a different database, update the DATABASE_URL variable in the code accordingly.

Create the database tables by running:

bash
Copy code
python create_tables.py
Seed Data:
To populate the database with sample data, run:

bash
Copy code
python seed_data.py
Usage
CLI Commands
Enroll Student:

bash
Copy code
python main.py enroll_student --name "Student Name"
List Students:

bash
Copy code
python main.py list_students
Hire Teacher:

bash
Copy code
python main.py hire_teacher --name "Teacher Name"
List Teachers:

bash
Copy code
python main.py list_teachers
Create Classroom:

bash
Copy code
python main.py create_classroom --name "Classroom Name"
List Classrooms:

bash
Copy code
python main.py list_classrooms
Customization
Models:

The models for students, teachers, classrooms, and enrollments are defined in separate files under the Models directory. You can customize these models based on your requirements.
Seed Data:

The seed_data.py script provides a way to populate the database with sample data. You can customize the names, locations, and other data used for seeding.
## Contributing
If you find issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project uses SQLAlchemy for database interactions.
Click is used for building the command-line interface.