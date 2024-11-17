create database demo;

CREATE TABLE demo.dbo.Student(
Id INT IDENTITY PRIMARY KEY,
Name VARCHAR(65) NOT NULL,
Gener VARCHAR(20),
Age INT,
Marks INT
)

Exec sp_help Student;
ALTER TABLE Student ADD Phone_No VARCHAR(20) NULL;
-- ALTER table Student ADD Phone_No VARCHAR(20) NULL;
ALTER TABLE STUDENT DROP COLUMN Phone_No;



-- ALTER TABLE Student Phone_No VARCHAR(20) NOT NULL;
USE demo;
SELECT * FROM Student;

ALTER TABLE Student
ALTER COLUMN Phone_No VARCHAR(20) NOT NULL;
SELECT name

FROM sys.key_constraints
WHERE type = 'PK' AND parent_object_id = OBJECT_ID('Student');

ALTER TABLE Student
DROP CONSTRAINT PK_Student;

ALTER TABLE Student

ADD CONSTRAINT PK_Student PRIMARY KEY (Phone_number);


-- DML 
-- C Create Insert
-- R Read Select
-- U Update Update
-- D Delete Delete

USE Demo;
GO

INSERT INTO Student (Name, Gener, Age, Marks, Phone_No) VALUES ('ABC', 'Male', 25, 75, '7248940124');
GO
-- Id will be aDDED automatically coz id incremenr is set to 1
INSERT INTO Student (Name, Gener, Age, Marks, Phone_No) VALUES ('XYZ', 'female', 21, 50, '123456789');

SELECT * FROM Student;

UPDATE Student set Phone_No = '101010101010'
WHERE id = 2
GO

SELECT * FROM Student;

DELETE FROM Student where id = 2;

SELECT * FROM Student;

INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('P', 'Male', 14, 45, '123');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Q', 'Female', 20, 77, '456');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('R', 'Male', 19, 90, '789');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('S', 'Female', 18, 68, '012');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Daniel', 'Male', 24, 98, '7521564946');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Andrew', 'Male', 22, 61, '8927722763');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Paul', 'Male', 19, 65, '6527883245');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Emily', 'Female', 29, 51, '8129861932');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Sarah', 'Female', 28, 75, '8826672642');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Donna', 'Female', 20, 71, '8328264150');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Nancy', 'Female', 20, 56, '6227703548');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Robert', 'Male', 31, 100, '6224604296');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Paul', 'Male', 18, 61, '8923992640');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Emily', 'Female', 25, 100, '6529646296');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('James', 'Male', 24, 69, '8129074670');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Emily', 'Female', 30, 100, '8827768723');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Andrew', 'Male', 26, 94, '9329381436');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Nancy', 'Female', 31, 90, '7822712451');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Mike', 'Male', 24, 74, '8823460324');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Linda', 'Female', 33, 75, '6224956439');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('James', 'Male', 29, 92, '9128921394');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Robert', 'Male', 25, 77, '7523194495');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('Jessica', 'Female', 27, 86, '8821536072');
INSERT INTO Student (Name, Gender, Age, Marks, Phone_number) VALUES ('David', 'Male', 23, 84, '7522318645');





UPDATE Student set Phone_No = '999999';     -- without where, all the id's gor updated
SELECT * FROM Student;


select Name, Marks from Student;    --Filter with column

SELECT * FROM Student;
select TOP 3 * FROM Student; --TOP is filter records (rows) order by ASC

SELECT * FROM Student
WHERE Marks > 50
order by Marks desc;


SELECT * FROM Student
WHERE Marks > 85 AND Gender = 'Male' AND Age < 50 
order by Marks desc; -- filter records with conditions

SELECT * FROM Student
WHERE Marks >= 35 AND Marks < 60
ORDER BY Marks asc;

SELECT top 3 * FROM Student
where Marks BETWEEN 35 AND 60
ORDER BY Marks desc;

SELECT Name, Phone_number from Student 
WHERE Name like '%s';           --wild card character

SELECT Name, Age from Student 
WHERE Age in (20,30,40);	-- AGE = 20 or AGE = 30 or AGE = 40


-- FETCH - number of records to display
 -- OFFSET - number of records to skip
 
 select * from Student
where Marks > 85
order by Marks desc
offset 5 rows

