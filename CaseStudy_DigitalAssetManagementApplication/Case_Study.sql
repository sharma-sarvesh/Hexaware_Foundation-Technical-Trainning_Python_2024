-- Database creation
CREATE DATABASE AssetManagement_db;
USE AssetManagement_db;
GO
	
-- 1.  Employees Table
CREATE TABLE Employees(
	EmployeeID INT PRIMARY KEY IDENTITY(1,1),
	Name VARCHAR(255) NOT NULL,
	Department VARCHAR(255) NOT NULL,
	Email VARCHAR(30) NOT NULL UNIQUE,
	Password VARCHAR(255) NOT NULL
	);

INSERT INTO Employees (Name, Department, Email, Password)
VALUES
('Alice Johnson', 'IT', 'alice.johnson@example.com', 'Password123!'),
('Bob Smith', 'Finance', 'bob.smith@example.com', 'SecurePass456'),
('Charlie Brown', 'HR', 'charlie.brown@example.com', 'HRPass789'),
('Diana Prince', 'Engineering', 'diana.prince@example.com', 'WonderWoman2021'),
('Ethan Hunt', 'Operations', 'ethan.hunt@example.com', 'MissionImpossible1');


-- 2. Assets Table
CREATE TABLE Assets(
	AssetID INT PRIMARY KEY IDENTITY(1,1),
	Name VARCHAR(255) NOT NULL,
	Type VARCHAR(255) NOT NULL,
	SerialNumber VARCHAR(255) UNIQUE NOT NULL,
	PurchaseDate DATE NOT NULL,
	Location VARCHAR(255) NOT NULL,
	Status VARCHAR(255) NOT NULL,
	OwnerID INT,
	FOREIGN KEY (OwnerID) REFERENCES Employees(EmployeeID)
	);

INSERT INTO Assets (Name, Type, SerialNumber, PurchaseDate, Location, Status, OwnerID)
VALUES
('Dell Laptop', 'Electronics', 'DL123456', '2022-05-01', 'Office A', 'In Use', 1),
('HP Printer', 'Electronics', 'HP987654', '2020-01-15', 'Office B', 'Available', 2),
('Office Chair', 'Furniture', 'CH567890', '2019-11-20', 'Office A', 'Under Maintenance', 3),
('Air Conditioner', 'Appliances', 'AC123789', '2021-07-22', 'Office C', 'In Use', 4),
('Projector', 'Electronics', 'PJ456123', '2023-03-10', 'Conference Room', 'Reserved', 5);


-- 3. maintenance_records table
CREATE TABLE Maintenance_Records(
	MaintenanceID INT PRIMARY KEY IDENTITY(1,1),
	MaintenanceDate DATE NOT NULL,
	Description VARCHAR(40) NOT NULL,
	Cost DECIMAL(10,2) NOT NULL,
	AssetID INT,
	FOREIGN KEY (AssetID) REFERENCES Assets(AssetID)
	);

INSERT INTO Maintenance_Records (MaintenanceDate, Description, Cost, AssetID)
VALUES
('2023-01-10', 'General Maintenance', 150.00, 1),
('2022-12-05', 'Ink Cartridge Replacement', 45.00, 2),
('2023-05-18', 'Leg Repair', 80.00, 3),
('2023-02-15', 'Filter Cleaning', 60.00, 4),
('2024-04-01', 'Lens Cleaning', 25.00, 5);


-- 4. asset_allocations table
CREATE TABLE Asset_Allocations(
	AllocationID INT PRIMARY KEY IDENTITY(1,1),
	AllocationDate DATE NOT NULL,
	ReturnDate DATE NULL,
	AssetID INT,
	EmployeeID INT,
	FOREIGN KEY(AssetID) REFERENCES Assets(AssetID),
	FOREIGN KEY(EmployeeID) REFERENCES Employees(EmployeeID)
	);

INSERT INTO Asset_Allocations (AllocationDate, ReturnDate, AssetID, EmployeeID)
VALUES
('2023-04-05', NULL, 1, 1), -- Asset currently allocated
('2022-10-12', '2022-11-15', 2, 2), -- Asset returned
('2023-03-01', NULL, 4, 4), -- Asset allocated but not yet returned
('2022-11-20', '2023-02-10', 3, 3), -- Asset returned
('2024-01-05', NULL, 5, 5); -- Asset reserved but not yet allocated


--5. reservations table
CREATE TABLE Reservations(
	ReservationID INT PRIMARY KEY IDENTITY(1,1),
	ReservationDate date NOT NULL,
	StartDate DATE NOT NULl,
	EndDate DATE NOT NULL,
	Status VARCHAR(50) NOT NULL,
	AssetID INT,
	EmployeeID INT,
	FOREIGN KEY(AssetID) REFERENCES Assets(AssetID),
	FOREIGN KEY(EmployeeID) REFERENCES Employees(EmployeeID)
	);

INSERT INTO Reservations (ReservationDate, StartDate, EndDate, Status, AssetID, EmployeeID)
VALUES
('2024-01-01', '2024-01-05', '2024-01-10', 'Confirmed', 5, 1),
('2023-03-01', '2023-03-05', '2023-03-15', 'Cancelled', 3, 2),
('2023-12-20', '2024-01-01', '2024-01-05', 'Pending', 1, 3),
('2022-08-15', '2022-08-20', '2022-08-25', 'Completed', 2, 4),
('2024-02-01', '2024-02-05', '2024-02-10', 'Confirmed', 4, 5);


SELECT * FROM Employees;
SELECT * FROM Assets;
SELECT * FROM Asset_Allocations;
SELECT * FROM Reservations;
SELECT * FROM Maintenance_Records;


USE AssetManagement_db;


ALTER TABLE Asset_Allocations
DROP CONSTRAINT FK__Asset_All__Asset__534D60F1;

ALTER TABLE Asset_Allocations
ADD CONSTRAINT FK__Asset_All__Asset__534D60F1
FOREIGN KEY (AssetID) REFERENCES Assets(AssetID) ON DELETE CASCADE;


ALTER TABLE Maintenance_Records
DROP CONSTRAINT FK__Maintenan__Asset__5070F446;

ALTER TABLE Maintenance_Records
ADD CONSTRAINT FK__Maintenan__Asset__5070F446
FOREIGN KEY (AssetID) REFERENCES Assets(AssetID) ON DELETE CASCADE;



--INSERT INTO Assets (Name, Type, SerialNumber, PurchaseDate, Location, Status, OwnerID)
--INSERT INTO Reservations (ReservationDate, StartDate, EndDate, Status, AssetID, EmployeeID)
--INSERT INTO Asset_Allocations (AllocationDate, ReturnDate, AssetID, EmployeeID)


SELECT * FROM Assets;
SELECT * FROM Asset_Allocations;
SELECT * FROM Reservations;


SELECT  A.AssetID, A.Name AS AssetName, A.Type, A.SerialNumber, A.PurchaseDate, A.Location, A.Status AS AssetStatus, 
		R.ReservationDate, R.StartDate, R.EndDate, R.Status AS ReservationStatus
FROM Reservations R 
JOIN Assets A ON R.AssetID = A.AssetID
LEFT JOIN Asset_Allocations AA ON R.AssetID = AA.AssetID
WHERE AA.AllocationID IS NULL AND R.Status IN ('Confirmed', 'Pending')
ORDER BY R.StartDate ASC;
