CREATE DATABASE sample;
USE sample;

CREATE TABLE Student(
	StudentId INT PRIMARY KEY IDENTITY(1,1), --Auto Increment(Start, Increase with)
	Name VARCHAR(255) NOT NULL,
	Gender CHAR(1) CHECK(Gender IN('M', 'F')), --REstricted to M OR F
	Age INT CHECK(Age BETWEEN 5 and 100)	--Restricted between 5 and 100
	);

INSERT INTO Student(Name, Gender, Age) VALUES 
	('Arnav', 'M' , 16),
	('Neha', 'F' , 21),
	('Manav', 'M' , 20),
	('Ishika', 'F' , 22),
	('Sahil', 'M' , 20);


CREATE TABLE Subject(
	SubjectId INT PRIMARY KEY IDENTITY(1,1),
	SubjectName VARCHAR(255) NOT NULL
	);

INSERT INTO Subject (SubjectName) VALUES
	('Mathematics'),
	('Physics'),
	('Chemistry'),
	('Biology');


CREATE TABLE Enrollment(
	EnrollementId INT PRIMARY KEY IDENTITY(1,1),
	StudentId INT,
	SubjectId INT,
	FOREIGN KEY (StudentId) REFERENCES Student(StudentId) ON DELETE CASCADE, --Deletes entry for enrollement as well if student deleted
	FOREIGN KEY (SubjectId) REFERENCES Subject(SubjectId) ON DELETE CASCADE
	);

INSERT INTO Enrollment (StudentId, SubjectId) VALUES
	(11, 1),
	(12, 2),
	(13, 3),
	(14, 4),
	(15, 3);

SELECT * FROM Student;
SELECT * FROM Subject;
SELECT * FROM Enrollment;

UPDATE Student
SET Age = 23
WHERE Name = 'Neha';

CREATE TABLE Marks(
	StudentId INT,
	SubjectId INT,
	Marks INT CHECK(Marks BETWEEN 0 and 100)
	FOREIGN KEY (StudentId) REFERENCES Student(StudentID),
	FOREIGN KEY (SubjectId) REFERENCES Subject(SubjectId)
	);

INSERT INTO Marks (StudentId, SUbjectId, Marks) VALUES
	(11, 1, 90),
	(11, 2, 88),
	(12, 2, 60),
	(12, 3, 47),
	(13, 3, 30),
	(13, 4, 75);


SELECT * FROM Student;
SELECT * FROM Subject;
SELECT * FROM Enrollment;
SELECT * FROM Marks;

ALTER TABLE Student
ADD Email VARCHAR(255);

UPDATE Student
SET Email = 'Arnav16@gmail.com'
WHERE Name = 'Arnav';


-- Exercise 12: Remove a Foreign Key Constraint
ALTER Table Marks
DROP CONSTRAINT 'CK__Marks__Marks__5629CD9C';
    -- OR 
SELECT CONSTRAINT_NAME 
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'Marks' AND COLUMN_NAME = 'Subject_id';


-- Exercise 13: Add a Check Constraint
ALTER TABLE Marks 
ADD CONSTRAINT ck_marks CHECK (MARKS BETWEEN 0 AND 100);

-- Exercise 14: Add On Delete Cascade to a Foreign Key

-- Drop the existing foreign key constraint
ALTER TABLE Marks
DROP CONSTRAINT FK_Marks_Student;

-- Add a new foreign key constraint with ON DELETE CASCADE
ALTER TABLE Marks
ADD CONSTRAINT FK_Marks_Student
FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE;


-- Bonus Exercise: Create a Self-Referencing Table
-- Create a table Employees with a manager_id that references another  employee_id in the same table.
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id) ON DELETE SET NULL -- Set to NULL if the manager is deleted
);



INSERT INTO Student( Name, Gender, Age, Email) VALUES ('Ron', 'M', 30, 'ron@gmail.com');

SELECT * FROM Student;
SELECT * FROM Subject;
SELECT * FROM Enrollment;
SELECT * FROM Marks;

--Task 15: Write a query to retrieve students' names and their respective subject names
SELECT s.Name as StudentName, sub.SubjectName
FROM Student s
INNER JOIN Enrollment e on e.StudentId = s.StudentId 
INNER JOIN Subject sub ON sub.SubjectId = e.SubjectID;

-- Task 16: Write a query to retrieve all students, even those who have not enrolled in any subjects
SELECT stu.Name as StudentName, stu.StudentId, sub.SubjectName
FROM Student stu
LEFT Join Enrollment e on e.StudentId = stu.StudentId
LEFT JOIN Subject sub ON sub.SubjectID = e.SubjectID;

--Task 17: Retrieve all subjects                 WRONG
SELECT sub.SubjectId, sub.SubjectName
FROM Subject sub
RIGHT JOIN Enrollment e ON e.SubjectId = sub.SubjectId
RIGHT JOIN Student stu ON stu.StudentId = e.StudentId;

select su.subject_name, st.student_name
from students st
right join enrollments e on st.student_id = e.student_id
right join subjects su on e.subject_id=su.subject_id;

--Task 18: Retrieve all students and subjects
SELECT stu.Name as StudentName, sub.SubjectName
FROM Student stu
FULL OUTER JOIN Enrollment e ON stu.StudentId = e.StudentId
FULL OUTER JOIN Subject sub ON e.SubjectId = sub.SubjectID;

--Task 19: Show all students and all subjects, generating every possible combination.
SELECT stu.Name as StudentName, sub.SubjectName
FROM Student stu
CROSS JOIN Subject sub;

--Task 20: Retrieve each student's name and the total marks they scored across all subjects.
SELECT s.Name as StudentName, SUM(m.Marks) as TotalMarks
FROM Student s
LEFT JOIN Marks m on s.StudentId = m.StudentId
GROUP BY s.Name;

--Task 21: Write a query to list employees and their respective managers' names.
--SELECT 
--    e.employee_name,
--    m.employee_name
--FROM 
--    Employees e
--SELF JOIN 
--    Employees m ON e.manager_id = m.employee_id;

--Task 22: Write a query to list students and their marks for each subject using an equi join.
SELECT stu.Name, sub.SubjectName, m.Marks
FROM Student stu, Subject sub, Marks m
WHERE stu.StudentId = m.StudentId AND sub.SubjectId = m.SubjectId;

--Task 23: Write a query to find subjects with an average mark greater than 70.
SELECT sub.SubjectName, AVG(m.Marks) AS AverageMarks
FROM Marks m
JOIN Subject sub ON m.SubjectId = sub.SubjectId
GROUP BY sub.SubjectName
HAVING AVG(m.Marks) > 70;

--Bonus Task: Write a query to display students who are enrolled in more than two subjects.
SELECT stu.Name AS StudentName, COUNT(e.SubjectId) AS NumberOfSubjects
FROM Student stu
INNER JOIN Enrollment e ON stu.StudentId = e.StudentId
GROUP BY stu.Name
HAVING COUNT(e.SubjectId) > 2 ;


SELECT * FROM Student;
SELECT * FROM Subject;
SELECT * FROM Enrollment;
SELECT * FROM Marks;

SELECT stu.Name as Name, sub.SUbjectName, m.Marks, 
	   RANK() OVER (PARTITION BY sub.SubjectId ORDER BY m.Marks DESC) AS Rank
FROM Student stu
INNER JOIN Enrollment e ON stu.StudentId = e.StudentId
INNER JOIN Subject sub ON e.SubjectId = sub.SubjectId
INNER JOIN Marks m ON e.StudentId = m.StudentId AND e.SubjectId = m.SubjectId;


SELECT Name FROM Student 
WHERE StudentId IN (SELECT StudentID FROM Enrollment);




SELECT name 
FROM Students s
JOIN Marks m ON s.student_id = m.student_id
WHERE m.marks > ANY (SELECT AVG(marks) FROM Marks WHERE subject_id = (SELECT subject_id FROM Subjects WHERE subject_name = 'Physics'));



