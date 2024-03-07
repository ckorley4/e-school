#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db,Student,Venue,Course,Instructor,Enrollment

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        print("Deleting data...")
        Student.query.delete()
        #Course.query.delete()
        #Instructor.query.delete()
        Venue.query.delete()
        print("Creating Stundents")
        s1 = Student(program="Computer Science",year_of_birth=1984,name="Thomas",course=2)
        s2 = Student(program="Music",year_of_birth=1986,name="Nii Korley",course=1)
        s3 = Student(program="software Engineering",year_of_birth=1986,name="Bernard Korley",course=3)
        s4 = Student(program="Computer Science",year_of_birth=1993,name="Atu Skrilla",course=4)
        s5 = Student(program="Computer Science",year_of_birth=1993,name="Shatta Wale",course=5)
        s6 = Student(program="Data Science",year_of_birth=1984,name="Ama Corq",course=1)
        s7 = Student(program="Computer Science",year_of_birth=1984,name="Sarah Sarah",course=2)
        s8 = Student(program="Mathematics",year_of_birth=1991,name="Daria Neza",course=3)
        s9 = Student(program="Computer Science",year_of_birth=1987,name="Charle Nii Armah",course=4)
        s10 = Student(program="Mathematics",year_of_birth=1984,name="Odoole",course=5)
        s11 = Student(program="Data Science",year_of_birth=1994,name="Tinny Akquaye",course=1)
        s12 = Student(program="Computer Science",year_of_birth=1990,name="Shoto Emma",course=2)
        s13 = Student(program="Data Science",year_of_birth=1986,name="Scarf Row",course=3)
        s14 = Student(program="Mathematics",year_of_birth=1984,name="Klotia",course=4)
        s15 = Student(program="Computer Science",year_of_birth=1980,name="Philip",course=5)

        students=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]
        db.session.add_all(students)
        db.session.commit()

        print("Creating Courses")
        c1 = Course(description="Front End",instructor_id=1,venue_id=2)
        c2 = Course(description="Back End",instructor_id=2,venue_id=1)
        c3 = Course(description="AI",instructor_id=3,venue_id=3)
        c4 = Course(description="AI",instructor_id=4,venue_id=4)
        c5 = Course(description="Algo",instructor_id=1,venue_id=5)
        c6 = Course(description="SQL",instructor_id=2,venue_id=4)
        c7 = Course(description="Blogging",instructor_id=2,venue_id=5)
        c8 = Course(description="Validation",instructor_id=1,venue_id=4)
        c9 = Course(description="Routing",instructor_id=3,venue_id=5)
        
        courses = [c1,c2,c3,c4,c5,c6,c7,c9]
        db.session.add_all(courses)
        db.session.commit()

        print("Creating Enrollments")
        e1 = Enrollment(student_id=1,course_id=2)
        e2 = Enrollment(student_id=2,course_id=1)
        e3 = Enrollment(student_id=2,course_id=1)
        e4 = Enrollment(student_id=14,course_id=4)
        e5 = Enrollment(student_id=12,course_id=1)
        e6 = Enrollment(student_id=11,course_id=5)
        e7 = Enrollment(student_id=2,course_id=3)
        e8 = Enrollment(student_id=3,course_id=3)
        e9 = Enrollment(student_id=3,course_id=1)
        e10 = Enrollment(student_id=9,course_id=4)
        e11 = Enrollment(student_id=2,course_id=3)
        e12 = Enrollment(student_id=14,course_id=5)
        e13 = Enrollment(student_id=1,course_id=1)
        e14 = Enrollment(student_id=1,course_id=1)
        e15 = Enrollment(student_id=2,course_id=5)
        e16 = Enrollment(student_id=5,course_id=1)
        e17 = Enrollment(student_id=3,course_id=5)
        e18 = Enrollment(student_id=9,course_id=1)
        e19 = Enrollment(student_id=2,course_id=1)
        e20 = Enrollment(student_id=14,course_id=1)
        e21 = Enrollment(student_id=8,course_id=1)
        e22 = Enrollment(student_id=11,course_id=1)
        e23 = Enrollment(student_id=8,course_id=5)
        e24 = Enrollment(student_id=3,course_id=2)
        e25 = Enrollment(student_id=3,course_id=2)
        e26 = Enrollment(student_id=9,course_id=5)
        e27 = Enrollment(student_id=2,course_id=1)
        e28 = Enrollment(student_id=15,course_id=1)
        e29 = Enrollment(student_id=12,course_id=5)
        e30 = Enrollment(student_id=5,course_id=1)
        e31 = Enrollment(student_id=2,course_id=5)
        e32 = Enrollment(student_id=7,course_id=1)
        e33 = Enrollment(student_id=3,course_id=5)
        e34 = Enrollment(student_id=9,course_id=2)
        enrollments = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e33,e31,e32,e34]
        db.session.add_all(enrollments)
        db.session.commit()


        print("Creating Venues")
        v1 = Venue(location="Ga Mashie")
        v2 = Venue(location="Awoshie")
        v3 = Venue(location="Bukom")
        v4 = Venue(location="Ashongman")
        v5 = Venue(location="Kaneshie")
        venues = [v1, v2, v3,v4,v5]
        db.session.add_all(venues)
        db.session.commit()


        print("Creating Instructors")
        i1=Instructor(name="Lantz",specialty="back end",department="Computer Science")
        i2=Instructor(name="Bleshia",specialty="dance",department="Fine Art")
        i3=Instructor(name="Anima",specialty="Data",department="Computer Science")
        i4=Instructor(name="Akweley",specialty="Java",department="Computer Science")
        instructors= [i1, i2, i3,i4]
        db.session.add_all(instructors)
        db.session.commit()
