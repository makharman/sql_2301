from sqlalchemy import Table,Column, String, Integer, MetaData, ForeignKey

metadata= MetaData()

students_table= Table(
    'students',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('city', String),
    Column('birth_data', Integer),
)

courses_table = Table(
    'courses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('course_name', String),
    Column('student_id', Integer, ForeignKey('students.id')) 
)


courses_students_table = Table(
    'courses_students',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('student_id', Integer, ForeignKey('students.id'))
)