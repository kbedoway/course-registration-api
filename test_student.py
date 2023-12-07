from course import Course, courses
from student import Student, stdCourses
import pytest

courseA = Course("COSC", "111", 30, "John Doe", 
        "Programming I", "PH 503", "TH 9:00")
courseB = Course("COSC", "211", 30, "Jane Doe", 
        "Programming II", "PH 503", "TR 11:00")

@pytest.fixture
def studentA():
	studentA = Student("1", "First Last")
	return studentA

def test_addCourse(studentA):
	courses.append(courseA)
	courses.append(courseB)

	studentA.addCourse(courseB)
	assert studentA.stdCourses[0] == courseB
	assert not studentA.stdCourses[0] == courseA

	courses.pop()
	courses.pop()