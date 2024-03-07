from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.sql import func
from config import db

# Models go here!
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

class Dated(db.Model,SerializerMixin):
    created_at = db.Column(db.DateTime(timezone=True),server_default = func.now())
    updated_at = db.Column(db.DateTime(timezone=True),onupdate = func.now())

class Student(Dated,db.Model,SerializerMixin):
    __tablename__='students'

    id = db.Column(db.Integer,primary_key=True)
    program = db.Column(db.String)
    name = db.Column(db.String)
    photo = db.Column(db.LargeBinary)
    course = db.Column(db.String)

    def __repr__(self):
        return f'<Student {self.id}: {self.name}>'

class Enrollment(Dated,db.Model,SerializerMixin):
    id = db.Column(db.Integer,primary_key =True)
    student_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)

class Course(Dated,db.Model,SerializerMixin):
    id = db.Column(db.Integer,primary_key= True)
    description = db.Column(db.String)
    venue_id = db.Column(db.String)
    instructor_id = db.Column(db.Integer)

class Instructor(db.Model,SerializerMixin):
    id = db.Column(db.Integer)
    name = db.Column(db.String)
    department = db.Column(db.String)
    special = db.Column(db.String)

class Venue(db.Model,SerializerMixin):
    id = db.Column(db.Integer)
    location = db.Column(db.String)
    instructor = db.Column(db.String)

