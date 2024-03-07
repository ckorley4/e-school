#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource,Api
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
import os
# Local imports
from config import app
from models import db,Venue,Student,Instructor,Course,Enrollment

# Add your model imports



# Views go here!


@app.route('/students', methods=['GET'])
def index():
    student_list =[student.to_dict() for student in Student.query.all()]
    return make_response(student_list,200)

@app.route('/venues', methods=['GET'])
def venues():
    venue_list =[venue.to_dict() for venue in Venue.query.all()]
    return make_response(venue_list,200)

@app.route('/instructors', methods=['GET'])
def instructors():
    instructor_list =[instructor.to_dict() for instructor in Instructor.query.all()]
    return make_response(instructor_list,200)

@app.route('/courses', methods=['GET'])
def courses():
    course_list =[course.to_dict() for course in Course.query.all()]
    return make_response(course_list,200)

@app.route('/enrollments', methods=['GET'])
def enrollments():
    enrollment_list =[enrollment.to_dict() for enrollment in Enrollment.query.all()]
    return make_response(enrollment_list,200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

