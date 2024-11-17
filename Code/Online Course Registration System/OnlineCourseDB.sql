-- Online Course Registration System

CREATE DATABASE OnlineCourse_db;
USE OnlineCourse_db;
GO

CREATE TABLE Students(
	StudentID INT PRIMARY KEY IDENTITY(1,1),
	StudentName VARCHAR(255) NOT NULL,
	StudentEmail VARCHAR(50) UNIQUE,
	PhoneNumber VARCHAR(20)
	);

INSERT INTO Students (StudentName, StudentEmail, PhoneNumber) VALUES 
	('Alice Johnson', 'alice.johnson@example.com', '123-456-7890'),
	('Bob Smith', 'bob.smith@example.com', NULL),
	('Charlie Brown', 'charlie.brown@example.com', '345-678-9012'),
	('Diana Prince', 'diana.prince@example.com', NULL),
	('Ethan Hunt', 'ethan.hunt@example.com', '567-890-1234');


CREATE TABLE Instructors(
	InstructorID INT PRIMARY KEY IDENTITY(1,1),
	InstructorName VARCHAR(50) NOT NULL
	);

INSERT INTO Instructors (InstructorName) VALUES 
	('Dr. John Doe'),
	('Prof. Jane Smith'),
	('Ms. Emily Davis'),
	('Mr. William Brown'),
	('Dr. Susan Green');


CREATE TABLE Courses(
	CourseID INT PRIMARY KEY IDENTITY(1,1),
	CourseName VARCHAR(50) NOT NULL,
	InstructorID INT,
	FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
	);

INSERT INTO Courses (CourseName, InstructorID) VALUES 
	('Python Programming', 1),
	('Data Science Basics', 2),
	('Web Development', 3),
	('Machine Learning', 2),
	('Database Management', 5);


CREATE TABLE Enrollments(
	EnrollmentID INT PRIMARY KEY IDENTITY(1,1),
	StudentID INT,
	CourseID INT,
	EnrollmentDate DATETIME DEFAULT GETDATE(),
	Status VARCHAR(20) CHECK (Status IN ('Registered', 'Deregistered', 'Not Enrolled')) NOT NULL,
	FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
	FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
	);

INSERT INTO Enrollments (StudentID, CourseID, Status) VALUES 
(1, 1, 'Registered'),
(1, 2, 'Registered'),
(2, 2, 'Registered'),
(3, 3, 'Registered'),
(4, 1, 'Registered');



SELECT * FROM Students;
SELECT * FROM Instructors;
SELECT * FROM Courses;
SELECT * FROM Enrollments;
