-- Create the database
CREATE DATABASE CourierManagement_db;
GO

-- Use the newly created database
USE CourierManagement_db;
GO


-- Create the User_table
CREATE TABLE User_table (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Password VARCHAR(255),
    ContactNumber VARCHAR(20),
    Address TEXT
);
GO

-- Create the Courier table
CREATE TABLE Courier (
    CourierID INT PRIMARY KEY,
    SenderName INT,  -- References UserID
    SenderAddress TEXT,
    ReceiverName INT,  -- References UserID
    ReceiverAddress TEXT,
    Weight DECIMAL(5,2),
    Status VARCHAR(50),
    TrackingNumber VARCHAR(20) UNIQUE,
    DeliveryDate DATE,
    FOREIGN KEY (SenderName) REFERENCES User_table(UserID),
    FOREIGN KEY (ReceiverName) REFERENCES User_table(UserID)
);
GO

-- Create the CourierServices table
CREATE TABLE CourierServices (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(100),
    Cost DECIMAL(8,2)
);
GO

-- Create the Employee table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    ContactNumber VARCHAR(20),
    Role VARCHAR(50),
    Salary DECIMAL(10,2),
    CourierID INT,
    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID)
);
GO

-- Create the Location table
CREATE TABLE Location (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Address TEXT
);
GO

-- Create the Payment table
CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    CourierID INT,
    LocationID INT,
    Amount DECIMAL(10,2),
    PaymentDate DATE,
    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);
GO

-- Insert sample values into User_table
INSERT INTO User_table (UserID, Name, Email, Password, ContactNumber, Address) VALUES
(1, 'Alice Smith', 'alice@example.com', 'password123', '1234567890', '123 Elm St'),
(2, 'Bob Johnson', 'bob@example.com', 'password123', '0987654321', '456 Oak St'),
(3, 'Charlie Brown', 'charlie@example.com', 'password123', '2345678901', '789 Pine St'),
(4, 'Diana Prince', 'diana@example.com', 'password123', '3456789012', '101 Maple St'),
(5, 'Ethan Hunt', 'ethan@example.com', 'password123', '4567890123', '202 Birch St');
GO

-- Insert sample values into CourierServices
INSERT INTO CourierServices (ServiceID, ServiceName, Cost) VALUES
(1, 'Standard Delivery', 5.00),
(2, 'Express Delivery', 10.00),
(3, 'Same Day Delivery', 15.00);
GO

-- Insert sample values into Location
INSERT INTO Location (LocationID, LocationName, Address) VALUES
(1, 'Warehouse A', '303 Warehouse St'),
(2, 'Warehouse B', '404 Storage St'),
(3, 'Branch Office', '505 Business Rd');
GO

-- Insert sample values into Courier
INSERT INTO Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate) VALUES
(1, 1, '123 Elm St', 2, '456 Oak St', 2.5, 'Pending', 'TRACK12345', '2024-10-20'),
(2, 2, '456 Oak St', 3, '789 Pine St', 1.0, 'Delivered', 'TRACK54321', '2024-10-18'),
(3, 3, '789 Pine St', 4, '101 Maple St', 3.5, 'In Transit', 'TRACK67890', '2024-10-19'),
(4, 4, '101 Maple St', 5, '202 Birch St', 2.0, 'Pending', 'TRACK98765', '2024-10-21'),
(5, 5, '202 Birch St', 1, '303 Warehouse St', 4.0, 'Pending', 'TRACK45678', '2024-10-22');
GO

-- Insert sample values into Employee
INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary, CourierID) VALUES
(1, 'John Doe', 'john@example.com', '5678901234', 'Delivery Driver', 3000.00, 1),
(2, 'Jane Doe', 'jane@example.com', '6789012345', 'Delivery Driver', 3200.00, 2),
(3, 'Mark Smith', 'mark@example.com', '7890123456', 'Warehouse Staff', 2800.00, NULL); -- Mark is not assigned to a courier
GO

-- Insert sample values into Payment
INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES
(1, 1, 1, 5.00, '2024-10-15'),
(2, 2, 2, 10.00, '2024-10-16'),
(3, 3, 3, 15.00, '2024-10-17'),
(4, 4, 1, 5.00, '2024-10-18'),
(5, 5, 2, 10.00, '2024-10-19');
GO



SELECT * FROM User_table;
SELECT * FROM Courier;

SELECT * FROM Employee;
SELECT * FROM Location;
SELECT * FROM Courier;
SELECT * FROM CourierServices;
SELECT * FROM Payment;

DROP TABLE User_table;
DROP TABLE Employee;
DROP TABLE Location;
DROP TABLE Courier;
DROP TABLE CourierServices;
DROP TABLE Payment;


