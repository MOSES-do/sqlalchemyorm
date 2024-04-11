from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///manytomany/database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

#This enables us to use class as the blueprint for our table
Base = declarative_base()

#Association table
# student_course_link = Table('student_course', Base.metadata,
#     Column('student_id', Integer, ForeignKey('students.id')),
#     Column('course_id', Integer, ForeignKey('courses.id'))
# )
#in a case of many to many relatonship where we have two classses
#where one class can have limitless number of instances and the other
#has a limit on instances that can be created 
#we relate the tables/classes such that each instance of the limitless class can have
#a list containing attribute values of the limited class, whenver an instance of the limitless class is created via a relationship in its own table, although will not be directly accessible when the table is viewed only upon query
#But in a case where both classes can have limitless instances, then all relationship is defined in the associative table

class StudentCourse(Base):
    __tablename__ = 'student_course'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    course_id = Column('course_id', Integer, ForeignKey('courses.id'))


#independent class
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name =  Column(String)
    #retuns a list: when creating a student object -> bill = Student(name='Bill', courses=[math, physics])
    courses = relationship("Course", secondary='student_course', back_populates="students")

#dependent class  
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary='student_course', back_populates="courses")

math = Course(title='Mathematics')
physics = Course(title='Physics')
bill = Student(name='Bill', courses=[math, physics])
rob = Student(name='Rob', courses=[math])

Base.metadata.create_all(engine)

# session.add_all([math, physics, bill, rob])
session.commit()

#print courses of a student
student = session.query(Student).filter_by(name='Bill').first()
courses = [course.title for course in student.courses]
print(f"{student.name}'s Courses: {', '.join(courses)}")

#print students enrolled to a particular course
cs = session.query(Course).filter_by(title='Physics').first()
students = [student.name for student in cs.students]
print(f"Student's {len(students)}\n")
print(f"Student's {students}\n")
