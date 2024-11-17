import logging
from DBConnection import DBConnection
from Student import Student
from Course import Course
from Enrollment import Enrollment

# Configure logging
logging.basicConfig(
    filename='logfile.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def display_menu():
    print("\nWhat would you like to do?")
    print("1. Display All Students")
    print("2. New Student Registration")
    print("3. Display Course List")
    print("4. Enroll in Course")
    print("5. Display Enrollments (Students and their Courses)")
    print("6. Exit")
    
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return None
    return choice

def main():
    db = DBConnection()
    db.connect()
    logging.info("Database connection established.")
    
    print("\n***** Online Course Registration System *****")
    
    while True:
        choice = display_menu()
        
        if choice == 1:
            # Display all students
            students = Student.get_all_students(db.get_connection())
            for student in students:
                print(student)
            logging.info("Displayed all students.")

        elif choice == 2:
            # New student registration
            student_name = input("Enter student name: ")
            student_email = input("Enter student email: ")
            phone_number = input("Enter phone number: ")
            new_student = Student(student_id=None, student_name=student_name, student_email=student_email, phone_number=phone_number)
            new_student.register_new_student(db.get_connection())
            logging.info(f"Registered new student: {student_name}")

        elif choice == 3:
            # Display course list
            courses = Course.get_all_courses(db.get_connection())
            for course in courses:
                print(course)
            logging.info("Displayed all courses.")

        elif choice == 4:
            # Enroll in course
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            enrollment = Enrollment(enrollment_id=None, student_id=student_id, course_id=course_id, enrollment_date=None, status='Registered')
            enrollment.enroll_student(db.get_connection())
            logging.info(f"Enrolled student ID {student_id} in course ID {course_id}.")

        elif choice == 5:
            # Display Enrollments (Students and their Courses)
            enrollments = Enrollment.get_students_with_courses(db.get_connection())
            for enrollment in enrollments:
                print(enrollment)
            logging.info("Displayed students and their enrolled courses.")

        elif choice == 6:
            print("Exiting...")
            db.close()
            logging.info("Database connection closed.")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
