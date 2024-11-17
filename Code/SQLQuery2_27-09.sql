USE demo
GO

CREATE TABLE test(
	testID int PRIMARY KEY,
	name VARCHAR(20)
)

CREATE TABLE test1(
	testID int PRIMARY KEY,
	name VARCHAR(20) not null
	)

INSERT INTO test (testID, name) VALUES (100, 'A');
INSERT INTO test1(testID, name) VALUES (200, 'Z');

SELECT * FROM test;
SELECT * FROM test1;

INSERT INTO test (testID, name) VALUES (101, 'B');
INSERT INTO test (testID) VALUES (110);        -- by default typs is null
INSERT INTO test (testID, name) VALUES ('D');  -- pRIMARY KEY CANNOT BE NULL
INSERT INTO test (testID, name) VALUES (104, 'E');

INSERT INTO test1 (testID, name) VALUES (201, 'S');
INSERT INTO test1 (testID, name) VALUES (202);  -- name is not null so error
INSERT INTO test1 (testID, name) VALUES ('y');  -- primary key cannot be null so error
INSERT INTO test1 (testID, name) VALUES (204, 'x');


insert into test1 (testID, name) VALUES (111, 'PQR');
insert into test1 VALUES (112, 'PQR');

ALTER TABLE demo set single_user with rollback immediate;
GO

SELECT * FROM test;

ALTER TABLE test
-- ADD age int not null;   -- ERROR coz already a NULL value is present
ADD age int not null default 16;

insert into test VALUES (009, 'ABC', 23);

Alter TABLE test
ADD mobile VARCHAR(10) UNIQUE;  -- ERROR coz age is default and UNIQUE is mentioned


SELECT * FROM test;

--ALTER TABLE test 
--ALTER COLUMN age CHECK(age between 14 and 20);

--alter table test add mobile varchar(10);
--update test set mobile = '9878964457' where testID = 1;
--update test set mobile = '9865745869' where testID= 2;
--update test set mobile = '9000124440' where testID = 3;
 
--alter table test add unique (mobile);




ALTER database demo set multi_user;

create table test2(
	id INT,
	marks INT CHECK (marks BETWEEN 0 and 100),
	rank INT UNIQUE,
	studID int,
	FOREIGN KEY (studID) REFERENCES test(testID),
	)

SELECT * FROM test2;




-- #############################
--DROP TABLE demo.dbo.stud;
--DROP TABLE demo.dbo.subject;
--DROP TABLE demo.dbo.marks;


CREATE TABLE stud(
	stud_id INT PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(50),
	);
 
CREATE TABLE subject (
	sub_id INT PRIMARY KEY IDENTITY(1,1),
	sub_name VARCHAR(50)
	);
 
CREATE TABLE marks(
	marks INT CHECK(marks between 0 and 100),
	stu_id INT,
	sub_id INT,
	FOREIGN KEY (stu_id) REFERENCES stud(stud_id),
	FOREIGN KEY (sub_id) REFERENCES subject(sub_id)
	);

INSERT INTO stud (name)
VALUES 
('John Doe'),
('Jane Smith'),
('Michael Johnson'),
('Emily Davis'),
('Chris Brown'),
('Linda Garcia'),
('James Wilson'),
('Sarah Miller'),
('Robert Taylor'),
('Lisa Anderson');

INSERT INTO subject (sub_name)
VALUES 
('Math'),
('Physics'),
('Chemistry'),
('Biology'),
('English'),
('History'),
('Geography'),
('Computer Science'),
('Economics'),
('Physical Education');


INSERT INTO marks (marks, stu_id, sub_id)
VALUES 
(ROUND(RAND() * 100, 0), 1, 1),
(ROUND(RAND() * 100, 0), 2, 2),
(ROUND(RAND() * 100, 0), 3, 3),
(ROUND(RAND() * 100, 0), 4, 4),
(ROUND(RAND() * 100, 0), 5, 5),
(ROUND(RAND() * 100, 0), 6, 6),
(ROUND(RAND() * 100, 0), 7, 7),
(ROUND(RAND() * 100, 0), 8, 8),
(ROUND(RAND() * 100, 0), 9, 9),
(ROUND(RAND() * 100, 0), 10, 10);

SELECT * FROM stud;
SELECT * FROM subject;
SELECT * FROM marks;

--DELETE FROM stud		-- ERROR coz reference is being used in another table
--WHERE stud_id = 3;     -- so we use "ON DELETE CASCADE" but it deletes entry from ALL THE TABLES

--DELETE FROM subject 
--WHERE sub_name = 'Biology';

--ALTER TABLE marks
--ADD CONSTRAINT fk_marks_stud
--FOREIGN KEY (stu_id) REFERENCES stud(id)
--ON DELETE CASCADE,

USE demo
GO

SELECT * FROM Student;
SELECT Name, Age from Student;
SELECT Name as Stud_Name, Age from Student;

SELECT Name, len(Name) as Length, age from Student;
SELECT UPPER(Name) as UName, LOWER(Name) as LName, age, Gender from Student; 

					-- Indexinf starts from 1
               -- Col_Name,Starting Index,len of characters
SELECT SUBSTRING(Name, 4,4) as Initial, Name, Age from Student;

	  --	Col-Name, Replace __ , Replace with __
SELECT REPLACE(Name, 'P','PQRS') as NewName, age from Student;

SELECT * FROM Student;
SELECT REPLACE(Age, 25, 1000) as NewAge, age from Student;

--#################################   DATE
SELECT * FROM Student;

ALTER TABLE Student
ADD joining_date date not null default GETDATE();

SELECT GETDATE() AS CurrentDateTime;

SELECT Name, joining_date, DATEADD( YEAR, 4, joining_date) AS GraduationDate FROM Student;

SELECT Name, joining_date, DATEADD( MONTH, 3, joining_date) AS m2g FROM Student;

SELECT Name, FORMAT(joining_date, 'dd-MMM-yyyy') AS FormattedDate FROM Student;

--#################################   DATE


SELECT * FROM test;
ALTER TABLE test
ADD email VARCHAR(50);

INSERT INTO test(testID, name, mobile, email) 
VALUES(21, 'Sahil', 9090876789, 'sahil@gmail.com');

SELECT @@IDENTITY as lidentity;
 
select top 1 * from test order by testID desc;

--################################# 

SELECT DB_NAME() as db;
SELECT USER_NAME() as userName;
SELECT SESSION_USER as sUser;
SELECT HOST_NAME as hName;
SELECT HOST_ID as hId;

SELECT @@VERSION as sqlversion;


 --################################# 
 

 CREATE TABLE emp(
	eId INT PRIMARY KEY,
	fName VARCHAR(50),
	lName VARCHAR(50),
	email VARCHAR(50),
	DOB DATE
	)

SELECT * FROM emp;

INSERT INTO emp (eId, fName, lName, email, DOB)
VALUES 
(1, 'John', 'Doe', 'johndoe@example.com', '1990-05-15'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '1988-07-22'),
(3, 'Michael', 'Johnson', 'michaelj@example.com', '1992-03-11'),
(4, 'Emily', 'Davis', 'emilyd@example.com', '1995-12-02'),
(5, 'Chris', 'Brown', 'chrisb@example.com', '1991-06-17'),
(6, 'Linda', 'Garcia', 'lindag@example.com', '1989-09-25'),
(7, 'James', 'Wilson', 'jamesw@example.com', '1993-11-30'),
(8, 'Sarah', 'Miller', 'sarahm@example.com', '1994-04-18'),
(9, 'Robert', 'Taylor', 'robertt@example.com', '1987-01-05'),
(10, 'Lisa', 'Anderson', 'lisaa@example.com', '1996-08-29'),
(11, 'David', 'Thomas', 'davidt@example.com', '1990-02-14'),
(12, 'Karen', 'Moore', 'karenm@example.com', '1992-10-07'),
(13, 'Mark', 'Jackson', 'markj@example.com', '1988-05-03'),
(14, 'Nancy', 'White', 'nancyw@example.com', '1991-11-20'),
(15, 'Paul', 'Harris', 'paulh@example.com', '1993-07-12'),
(16, 'Amy', 'Martin', 'amym@example.com', '1995-03-22'),
(17, 'Steven', 'Clark', 'stevenc@example.com', '1990-09-19'),
(18, 'Jessica', 'Rodriguez', 'jessicar@example.com', '1987-06-25'),
(19, 'George', 'Lewis', 'georgel@example.com', '1989-04-08'),
(20, 'Sophia', 'Walker', 'sophiaw@example.com', '1994-12-15');


SELECT * FROM emp;


SELECT eId, fName, lName, email, DOB,
    DATEDIFF(YEAR, DOB, GETDATE()) AS Age,
    CONCAT(LEFT(email, CHARINDEX('@', email) - 1), '@hexaware.com') AS company_mail
FROM emp;



 --################################################# GROUP BY


SELECT * FROM Student;
SELECT SUM(Marks) as Total FROM Student;
SELECT MAX(Marks)  as Topper FROM Student;
SELECT MIN(Marks) as Achiever FROM Student;
SELECT AVG(Marks)as Average FROM Student;
SELECT COUNT(Marks)as Total_Students FROM Student;

SELECT Name, AVG(Marks) as AvgMarks from Student
GROUP BY Name; 

SELECT Name, AVG(Marks) as AvgMarks, MAX(Marks) as Topper from Student
GROUP BY Name; 


SELECT Name, count(Marks) as subjects_appeared, MAX (Marks) as maxmarks, AVG(Marks) as avgmarks FROM student 
group by Name;

 
  --################################################# HAVING


SELECT Name, COUNT(Marks) as subjects_appeared, MAX(Marks) as maxmarks, AVG(Marks) as avgmarks FROM student 
GROUP BY Name 
HAVING AVG(marks) > 75;

  --################################################# Task

SELECT * FROM Student;

SELECT Id, Name, SUM(Marks) as Total_Marks, AVG(Marks) as Avg_Marks FROM Student
GROUP BY Id;


SELECT Name, 
	   AVG(Marks) as Avg_Marks, 
	   SUM(Marks) as Total_Marks,
	CASE 
		WHEN AVG(Marks) > 60 THEN 'Pass' 
		ELSE 'Fail' 
	END AS status
FROM Student 
GROUP BY Name;




  --################################################# JOINS

SELECT column_name(s) FROM table1 INNER JOIN table2 ON Condition;

SELECT * FROM stud;		--stud_id, name
SELECT * FROM subject;	-- sub_id, sub_name
SELECT * FROM marks;	-- marks, stud_id, sub_id


SELECT * 
FROM stud
INNER JOIN marks
ON marks = marks
ORDER BY stu_id;




