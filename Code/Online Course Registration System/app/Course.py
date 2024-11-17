# class Course:
#     def __init__(self,course_id, course_name, instructor): #instructor is instance(object-relation b/w class n obj) of the class Instructor 
#         self.course_id = course_id
#         self.course_name = course_name
#         self.instructor = instructor

#     def __str__(self):
#         print(f"Course[ID: {self.course_id}, Name: {self.course_name}, Instructort: {self.instructor}]")

import pyodbc

class Course:
    def __init__(self, course_id, course_name, instructor_id):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor_id = instructor_id

    @classmethod
    def get_all_courses(cls, connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Courses")
        rows = cursor.fetchall()
        courses = []
        for row in rows:
            courses.append(cls(row.CourseID, row.CourseName, row.InstructorID))
        return courses

    def __str__(self):
        return f"Course[ID: {self.course_id}, Name: {self.course_name}, Instructor: {self.instructor_id}]"
