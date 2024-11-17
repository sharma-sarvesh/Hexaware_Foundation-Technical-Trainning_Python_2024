#* Online Course Registration System
# Problem Statement:Develop an Online Course Registration System where:
'''
# Students can register for multiple courses, and each course has a unique Course ID, Course Name, and Instructor.
# Store student and course information in MSSQL tables.
# Allow students to register for courses, update their course list, or deregister from courses.
# Create a transaction log in a text file to keep track of all registration changes (add, update, delete).
# Use exception handling for scenarios like over-enrollment (more than 5 courses per student) or registering for a non-existent course.
# Handle OOP concepts to model relationships between Students, Courses, and Instructors.
'''
#* Tasks:
'''
# Create MSSQL tables to handle course registration and student data.
# Implement CRUD operations for course registration.
# Log registration details in a text file.
# Handle exceptions for over-enrollment and invalid course selection.
'''
#* Hints:
'''
# Create tables for Students, Courses, and Enrollments.
# Use file handling to log every course registration or modification.
# Apply try-except-else-finally blocks to handle errors during the registration process.
# Implement custom exceptions for exceeding course limits or invalid course selection.
'''
#* General Considerations :
# Focus on clean code practices, including appropriate naming conventions, modularity, and code reusability.
# Ensure proper use of exception handling and logging to manage unexpected scenarios.
# Solutions should handle edge cases such as invalid inputs, database connection issues, and logical errors in business rules.

