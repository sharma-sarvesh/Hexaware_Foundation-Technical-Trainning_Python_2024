CREATE DATABASE HospitalManagement_DB;

USE HospitalManagement_DB;
GO

-- 1. Table: Patient
CREATE TABLE Patient (
    patientId INT PRIMARY KEY IDENTITY(1,1),
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F')) NOT NULL,
    contactNumber VARCHAR(10) NOT NULL,
    address NVARCHAR(255) NOT NULL
);
GO

-- 2. Table: Doctor
CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY IDENTITY(1,1),
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    contactNumber VARCHAR(10) NOT NULL
);
GO

-- 3. Table: Appointment
CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY IDENTITY(1,1),
    patientId INT NOT NULL,
    doctorId INT NOT NULL,
    appointmentDate DATETIME NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (patientId) REFERENCES Patient(patientId) ON DELETE CASCADE,
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId) ON DELETE CASCADE
);
GO

SELECT * FROM Patient;
SELECT * FROM Doctor;
SELECT * FROM Appointment;


INSERT INTO Patient (firstName, lastName, dateOfBirth, gender, contactNumber, address) VALUES
('John', 'Doe', '1985-05-15', 'M', '555-1234', '123 Elm St, Springfield'),
('Jane', 'Smith', '1990-08-22', 'F', '555-5678', '456 Oak St, Springfield'),
('Emily', 'Johnson', '1982-12-05', 'F', '555-8765', '789 Pine St, Springfield'),
('Michael', 'Brown', '1975-03-30', 'M', '555-4321', '321 Maple St, Springfield'),
('Sarah', 'Davis', '1995-11-11', 'F', '555-1111', '654 Cedar St, Springfield');


INSERT INTO Doctor (firstName, lastName, specialization, contactNumber) VALUES
('Dr. Alice', 'Williams', 'Cardiology', '555-9999'),
('Dr. Bob', 'Martinez', 'Pediatrics', '555-2222'),
('Dr. Carol', 'Garcia', 'Neurology', '555-3333'),
('Dr. David', 'Hernandez', 'Orthopedics', '555-4444'),
('Dr. Eva', 'Lopez', 'General Medicine', '555-5555');


INSERT INTO Appointment (patientId, doctorId, appointmentDate, description) VALUES
(2, 1, '2024-10-20', 'Routine check-up'),
(3, 2, '2024-10-21', 'Flu vaccination'),
(4, 3, '2024-10-22', 'Neurological evaluation'),
(5, 4, '2024-10-23', 'Knee pain assessment'),
(6, 5, '2024-10-24', 'General health consultation');
SELECT * FROM Patient;
SELECT * FROM Doctor;
SELECT * FROM Appointment;