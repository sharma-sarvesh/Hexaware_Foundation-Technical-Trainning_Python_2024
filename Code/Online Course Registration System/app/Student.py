# class Student:
#     def __init__(self, student_id, student_name, student_email, phone_number=None): # phone no is not mandatory so if not given, defauklt valuer is None
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_email = student_email
#         self.phone_number = self.phone_number
#         self.courses = []           #list to store courses

#     def register_course(self, course):
#         if len(self.courses) < 5:
#             self.courses.append(course)
#             print(f"{self.student_name} successfully registered for {course.course_name}")
#         else:
#             print(f"{self.student_name} cannot register for more then 5 cources")
    
#     def deregister_cource(self, course_id):
#         new_course_list = []
#         for course in self.courses:
#             if course.course_id != course_id:
#                 new_course_list.append(course)
#         self.courses = new_course_list
#         print(f"{self.student_name} deregistered from course with course id: {course_id}")

#     def __str__(self):
#         print(f"Student[ID: {self.student_id}, Name: {self.student_name}, Email: {self.student_email}, PhoneNumber: {self.phone_number}]")

import pyodbc

class Student:
    def __init__(self, student_id, student_name, student_email, phone_number):
        self.student_id = student_id
        self.student_name = student_name
        self.student_email = student_email
        self.phone_number = phone_number

    @classmethod
    def get_all_students(cls, connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Students")
        rows = cursor.fetchall()
        students = []
        for row in rows:
            students.append(cls(row.StudentID, row.StudentName, row.StudentEmail, row.PhoneNumber))
        return students

    def register_new_student(self, connection):
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Students (StudentName, StudentEmail, PhoneNumber) VALUES (?, ?, ?)",
            (self.student_name, self.student_email, self.phone_number)
        )
        connection.commit()

    def __str__(self):
        return f"Student[ID: {self.student_id}, Name: {self.student_name}, Email: {self.student_email}, PhoneNumber: {self.phone_number}]"
    
