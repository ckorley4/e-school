from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from config import db
from datetime import datetime

# Models go here!
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


# Models go here!
   

class Student(db.Model,SerializerMixin):
    __tablename__ = 'students'

    id = db.Column(db.Integer,primary_key=True)
    program = db.Column(db.String)
    name = db.Column(db.String)
    year_of_birth = db.Column(db.Integer)
    photo = db.Column(db.LargeBinary)
    course = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    enrollments = db.relationship('Enrollment',back_populates='student',cascade="all,delete")
    serialize_rules = ("-enrollments.student","-created_at","-updated_at",)
    
    @validates("year_of_birth")
    def validate_year(self, key, year_of_birth):
        if not len(str(year_of_birth)) == 4 or not isinstance(year_of_birth, int):
            raise ValueError("Year must be a four-digit integer")
        if year_of_birth > datetime.now().year:
            raise ValueError("Year cannot be in the future")
        if datetime.now().year - year_of_birth < 18:
            raise ValueError("Student should be greater than 18 years old")
        return year_of_birth

    def __repr__(self):
        return f'<Student {self.id}: {self.name}>'

class Enrollment(db.Model,SerializerMixin):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer,primary_key =True)
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer,db.ForeignKey('courses.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    student = db.relationship('Student',back_populates='enrollments')
    course =  db.relationship('Course',back_populates='enrollments')
    
    serialize_rules = ( "-student.enrollments","-course.enrollments" )

    def __repr__(self):
        return f'<Enrollment {self.id}>'

class Course(db.Model,SerializerMixin):
    __tablename__ = 'courses'

    id = db.Column(db.Integer,primary_key= True)
    description = db.Column(db.String)
    venue_id = db.Column(db.String,db.ForeignKey('venues.id'))
    instructor_id = db.Column(db.Integer,db.ForeignKey('instructors.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    #instructor = db.relationship('Instructor',back_populates='courses',cascade="all,delete")
    #venue = db.relationship('Instructor',back_populates='courses',cascade="all,delete")
    enrollments = db.relationship('Enrollment',back_populates='course',cascade="all,delete")
    serialize_rules = ("-enrollments.course","-created_at","-updated_at",)

    def __repr__(self):
        return f'<Course {self.id}  {self.description}>'

class Instructor(db.Model,SerializerMixin):
    __tablename__ = 'instructors'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    department = db.Column(db.String)
    specialty = db.Column(db.String)
    #courses=db.relationship(Course,back_populates='instructor')



    def __repr__(self):
        return f'<Instructor {self.id}  {self.name}>'

class Venue(db.Model,SerializerMixin):
    __tablename__ = 'venues'
    
    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.String)
    #courses=db.relationship(Course,back_populates='venue')

    def __repr__(self):
        return f'<Venue {self.id}  {self.location}>'

