# class Enrollment:
#     def __init__(self, enrollment_id, student, course, enrollment_date, status):
#         self.enrollment_id = enrollment_id
#         self.student = student  # instance of the class Student
#         self.course = course  # instance of the class Course class
#         self.enrollment_date = enrollment_date
#         self.status = status

#     def __str__(self):
#         return f"Enrollment[ID: {self.enrollment_id}, Student: {self.student.student_name}, Course: {self.course.course_name}, Date: {self.enrollment_date}, Status: {self.status}]"

import pyodbc

class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, enrollment_date, status):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date
        self.status = status

    def enroll_student(self, connection):
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Enrollments (StudentID, CourseID, Status) VALUES (?, ?, 'Registered')",
            (self.student_id, self.course_id)
        )
        connection.commit()

    @staticmethod
    def get_students_with_courses(connection):
        try:
            cursor = connection.cursor()
            query = """
                SELECT s.StudentName, c.CourseName, e.Status
                FROM Enrollments e
                JOIN Students s ON e.StudentID = s.StudentID
                JOIN Courses c ON e.CourseID = c.CourseID
                WHERE e.Status = 'Registered';
            """
            cursor.execute(query)
            results = cursor.fetchall()
            
            if results:
                print("Students Enrolled in Courses:")
                enrollments = []
                for row in results:
                    student_name, course_name, status = row
                    enrollments.append(f"Student: {student_name}, Course: {course_name}, Status: {status}")
                return enrollments
            else:
                print("No students are enrolled in any courses.")
                return []
        
        except Exception as e:
            print(f"Error fetching enrollments: {e}")
            return []

    def __str__(self):
        return f"Enrollment[ID: {self.enrollment_id}, Student: {self.student.student_name}, Course: {self.course.course_name}, Date: {self.enrollment_date}, Status: {self.status}]"
