from fastapi import FastAPI
from course import Course, courses

class Student:
    def __init__(self, EID, , registered_courses, name):
        self.EID = EID
        self.registered_courses = registered_courses
        self.name = name
        self.stdCourses = []

    def addCourse(self, course):
        if course in courses:
            self.stdCourses.append(course)

stdCourses = []
stds = {}