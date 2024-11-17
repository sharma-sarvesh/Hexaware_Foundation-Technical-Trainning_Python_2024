# class Instructor:
#     def __init__(self, instructor_id, instructor_name):
#         self.insturctor_id = instructor_id
#         self.instructor_name = instructor_name
    
#     def __str__(self):
#         print(f"Instructor:[ID: {self.insturctor_id}, Name: {self.instructor_name}]")

import pyodbc

class Instructor:
    def __init__(self, instructor_id, instructor_name):
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name

    @classmethod
    def get_all_instructors(cls, connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Instructors")
        rows = cursor.fetchall()
        instructors = []
        for row in rows:
            instructors.append(cls(row.InstructorID, row.InstructorName))
        return instructors

    def __str__(self):
        return f"Instructor:[ID: {self.insturctor_id}, Name: {self.instructor_name}]"

