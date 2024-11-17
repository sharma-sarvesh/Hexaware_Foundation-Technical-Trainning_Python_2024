-- **************Task 1: Database Design **************

CREATE DATABASE task_db;
USE task_db;

 -- [User], valid identifier rather than a reserved keyword
-- CREATE TABLE task_db.dbo.[User] (

CREATE TABLE task_db.dbo.User_table(
	UserID INT PRIMARY KEY,
	Name VARCHAR(255) NOT NULL,
	Email VARCHAR(255) UNIQUE,
	Password VARCHAR(255),
	ContactNumber VARCHAR(20),
	ADDRESS TEXT
	);

INSERT INTO User_table (UserID, Name, Email, Password, ContactNumber, Address)
VALUES
    (1, 'Alice Johnson', 'alice.johnson@example.com', 'password123', '1234567890', '123 Main Street'),
    (2, 'Bob Smith', 'bob.smith@example.com', 'password456', '2345678901', '456 Elm Street'),
    (3, 'Charlie Brown', 'charlie.brown@example.com', 'password789', '3456789012', '789 Oak Street'),
    (4, 'David Lee', 'david.lee@example.com', 'password012', '4567890123', '1234 Maple Street'),
    (5, 'Emily Taylor', 'emily.taylor@example.com', 'password345', '5678901234', '567 Pine Street'),
    (6, 'Frank Wilson', 'frank.wilson@example.com', 'password678', '6789012345', '890 Cedar Street'),
    (7, 'Grace Williams', 'grace.williams@example.com', 'password901', '7890123456', '1234 Birch Street'),
    (8, 'Henry Baker', 'henry.baker@example.com', 'password234', '8901234567', '567 Oak Street'),
    (9, 'Isabella Clark', 'isabella.clark@example.com', 'password567', '9012345678', '890 Elm Street'),
    (10, 'Jack Davis', 'jack.davis@example.com', 'password890', '1234567890', '123 Pine Street'),
    (11, 'Kate Evans', 'kate.evans@example.com', 'password123', '2345678901', '456 Cedar Street'),
    (12, 'Liam Fox', 'liam.fox@example.com', 'password456', '3456789012', '789 Birch Street'),
    (13, 'Mia Green', 'mia.green@example.com', 'password789', '4567890123', '1234 Maple Street'),
    (14, 'Noah Hill', 'noah.hill@example.com', 'password012', '5678901234', '567 Pine Street'),
    (15, 'Olivia Jones', 'olivia.jones@example.com', 'password345', '6789012345', '890 Cedar Street'),
    (16, 'Paul King', 'paul.king@example.com', 'password678', '7890123456', '1234 Birch Street'),
    (17, 'Quinn Lee', 'quinn.lee@example.com', 'password901', '8901234567', '567 Oak Street'),
    (18, 'Riley Martin', 'riley.martin@example.com', 'password234', '9012345678', '890 Elm Street'),
    (19, 'Sarah Nelson', 'sarah.nelson@example.com', 'password567', '1234567890', '123 Pine Street'),
    (20, 'Thomas Owens', 'thomas.owens@example.com', 'password890', '2345678901', '456 Cedar Street');


-- Courier Table
CREATE TABLE Courier(
	CourierID INT PRIMARY KEY,
	SenderName VARCHAR(255),
	SenderAddress TEXT,
	ReceiverName VARCHAR(255),
	ReceiverAddress TEXT,
	Weight DECIMAL(5,2),
	Status VARCHAR(50),
	TrackingNumber VARCHAR(20) UNIQUE,
	DeliveryDate Date
	);

INSERT INTO Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate)
VALUES
    (1, 'Alice Johnson', '123 Main Street', 'Bob Smith', '456 Elm Street', 2.50, 'Pending', 'C001', '2023-10-15'),
    (2, 'Charlie Brown', '789 Oak Street', 'David Lee', '1234 Maple Street', 3.25, 'Out for Delivery', 'C002', '2023-10-17'),
    (3, 'Emily Taylor', '567 Pine Street', 'Frank Wilson', '890 Cedar Street', 1.75, 'Delivered', 'C003', '2023-10-16'),
    (4, 'Grace Williams', '1234 Birch Street', 'Henry Baker', '567 Oak Street', 4.00, 'Pending', 'C004', '2023-10-20'),
    (5, 'Isabella Clark', '890 Elm Street', 'Jack Davis', '123 Pine Street', 2.25, 'Out for Delivery', 'C005', '2023-10-18'),
    (6, 'Kate Evans', '456 Cedar Street', 'Liam Fox', '789 Birch Street', 3.50, 'Delivered', 'C006', '2023-10-19'),
    (7, 'Mia Green', '1234 Maple Street', 'Noah Hill', '567 Pine Street', 1.00, 'Pending', 'C007', '2023-10-22'),
    (8, 'Olivia Jones', '890 Cedar Street', 'Paul King', '1234 Birch Street', 2.75, 'Out for Delivery', 'C008', '2023-10-21'),
    (9, 'Quinn Lee', '567 Oak Street', 'Riley Martin', '890 Elm Street', 3.00, 'Delivered', 'C009', '2023-10-23'),
    (10, 'Sarah Nelson', '123 Pine Street', 'Thomas Owens', '456 Cedar Street', 1.50, 'Pending', 'C010', '2023-10-25'),
    (11, 'Alice Johnson', '123 Main Street', 'Bob Smith', '456 Elm Street', 2.50, 'Delivered', 'C011', '2023-10-24'),
    (12, 'Charlie Brown', '789 Oak Street', 'David Lee', '1234 Maple Street', 3.25, 'Pending', 'C012', '2023-10-27'),
    (13, 'Emily Taylor', '567 Pine Street', 'Frank Wilson', '890 Cedar Street', 1.75, 'Out for Delivery', 'C013', '2023-10-26'),
    (14, 'Grace Williams', '1234 Birch Street', 'Henry Baker', '567 Oak Street', 4.00, 'Delivered', 'C014', '2023-10-28'),
    (15, 'Isabella Clark', '890 Elm Street', 'Jack Davis', '123 Pine Street', 2.25, 'Pending', 'C015', '2023-10-30'),
    (16, 'Kate Evans', '456 Cedar Street', 'Liam Fox', '789 Birch Street', 3.50, 'Out for Delivery', 'C016', '2023-10-31'),
    (17, 'Mia Green', '1234 Maple Street', 'Noah Hill', '567 Pine Street', 1.00, 'Delivered', 'C017', '2023-11-01'),
    (18, 'Olivia Jones', '890 Cedar Street', 'Paul King', '1234 Birch Street', 2.75, 'Pending', 'C018', '2023-11-02'),
    (19, 'Quinn Lee', '567 Oak Street', 'Riley Martin', '890 Elm Street', 3.00, 'Out for Delivery', 'C019', '2023-11-03'),
    (20, 'Sarah Nelson', '123 Pine Street', 'Thomas Owens', '456 Cedar Street', 1.50, 'Delivered', 'C020', '2023-11-04');


-- CourierServices Table
CREATE TABLE CourierServices(
	ServiceID INT PRIMARY KEY,
	ServiceName VARCHAR(100),
	Cost DECIMAL(8,2)		-- total no of digits, no of digits after decimal
	);

INSERT INTO CourierServices(ServiceID, ServiceName, Cost)
VALUES
    (1, 'Standard Delivery', 10.00),
    (2, 'Express Delivery', 20.00),
    (3, 'Overnight Delivery', 30.00),
    (4, 'International Shipping', 50.00),
    (5, 'Fragile Handling', 5.00),
    (6, 'Insurance', 10.00),
    (7, 'COD (Cash on Delivery)', 2.00),
    (8, 'Return Service', 5.00),
    (9, 'Gift Wrapping', 3.00),
    (10, 'Custom Packaging', 15.00),
    (11, 'Same-Day Delivery', 50.00),
    (12, 'Temperature-Controlled Shipping', 10.00),
    (13, 'Hazardous Materials Handling', 25.00),
    (14, 'Bulk Shipping Discount', 10.00),
    (15, 'Subscription Shipping', 5.00),
    (16, 'Signature Required', 2.00),
    (17, 'Address Change', 5.00),
    (18, 'Delivery Confirmation', 2.00),
    (19, 'Customs Clearance', 15.00),
    (20, 'Tracking Service', 5.00);


-- Employee Table
CREATE TABLE Employee(
	EmployeeID INT PRIMARY KEY,
	Name VARCHAR(255),
	Email VARCHAR(255) UNIQUE,
	ContactNumber VARCHAR(20),
	Role VARCHAR(50),
	Salary DECIMAL(10,2)
	);

INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary)
VALUES
    (1, 'John Smith', 'john.smith@couriercompany.com', '1234567890', 'Delivery Driver', 35000.00),
    (2, 'Jane Doe', 'jane.doe@couriercompany.com', '2345678901', 'Customer Service Representative', 28000.00),
    (3, 'David Lee', 'david.lee@couriercompany.com', '3456789012', 'Warehouse Manager', 40000.00),
    (4, 'Emily Taylor', 'emily.taylor@couriercompany.com', '4567890123', 'Operations Manager', 50000.00),
    (5, 'Frank Wilson', 'frank.wilson@couriercompany.com', '5678901234', 'IT Technician', 38000.00),
    (6, 'Grace Williams', 'grace.williams@couriercompany.com', '6789012345', 'Accounting Manager', 45000.00),
    (7, 'Henry Baker', 'henry.baker@couriercompany.com', '7890123456', 'Human Resources Manager', 42000.00),
    (8, 'Isabella Clark', 'isabella.clark@couriercompany.com', '8901234567', 'Marketing Manager', 48000.00),
    (9, 'Jack Davis', 'jack.davis@couriercompany.com', '9012345678', 'Delivery Driver', 35000.00),
    (10, 'Kate Evans', 'kate.evans@couriercompany.com', '1234567890', 'Customer Service Representative', 28000.00),
    (11, 'Liam Fox', 'liam.fox@couriercompany.com', '2345678901', 'Warehouse Manager', 40000.00),
    (12, 'Mia Green', 'mia.green@couriercompany.com', '3456789012', 'Operations Manager', 50000.00),
    (13, 'Noah Hill', 'noah.hill@couriercompany.com', '4567890123', 'IT Technician', 38000.00),
    (14, 'Olivia Jones', 'olivia.jones@couriercompany.com', '5678901234', 'Accounting Manager', 45000.00),
    (15, 'Paul King', 'paul.king@couriercompany.com', '6789012345', 'Human Resources Manager', 42000.00),
    (16, 'Quinn Lee', 'quinn.lee@couriercompany.com', '7890123456', 'Marketing Manager', 48000.00),
    (17, 'Riley Martin', 'riley.martin@couriercompany.com', '8901234567', 'Delivery Driver', 35000.00),
    (18, 'Sarah Nelson', 'sarah.nelson@couriercompany.com', '9012345678', 'Customer Service Representative', 28000.00),
    (19, 'Thomas Owens', 'thomas.owens@couriercompany.com', '1234567890', 'Warehouse Manager', 40000.00),
    (20, 'Ursula Parker', 'ursula.parker@couriercompany.com', '2345678901', 'Operations Manager', 50000.00);


-- Location Table
CREATE TABLE Location(
	LocationID INT PRIMARY KEY,
	LocationName VARCHAR(100),
	Address TEXT
	);

INSERT INTO Location (LocationID, LocationName, Address)
VALUES
    (1, 'Mumbai', 'Mumbai, Maharashtra, India'),
    (2, 'Delhi', 'Delhi, India'),
    (3, 'Bangalore', 'Bangalore, Karnataka, India'),
    (4, 'Kolkata', 'Kolkata, West Bengal, India'),
    (5, 'Chennai', 'Chennai, Tamil Nadu, India'),
    (6, 'Hyderabad', 'Hyderabad, Telangana, India'),
    (7, 'Pune', 'Pune, Maharashtra, India'),
    (8, 'Ahmedabad', 'Ahmedabad, Gujarat, India'),
    (9, 'Jaipur', 'Jaipur, Rajasthan, India'),
    (10, 'Lucknow', 'Lucknow, Uttar Pradesh, India'),
    (11, 'Surat', 'Surat, Gujarat, India'),
    (12, 'Coimbatore', 'Coimbatore, Tamil Nadu, India'),
    (13, 'Kanpur', 'Kanpur, Uttar Pradesh, India'),
    (14, 'Nagpur', 'Nagpur, Maharashtra, India'),
    (15, 'Indore', 'Indore, Madhya Pradesh, India'),
    (16, 'Patna', 'Patna, Bihar, India'),
    (17, 'Vadodara', 'Vadodara, Gujarat, India'),
    (18, 'Bhopal', 'Bhopal, Madhya Pradesh, India'),
    (19, 'Ranchi', 'Ranchi, Jharkhand, India'),
    (20, 'Gwalior', 'Gwalior, Madhya Pradesh, India');


-- Payment Table
CREATE TABLE Payment(
	PaymentID INT PRIMARY KEY,
	CourierID INT,
	LocationID INT,
	Amount DECIMAL(10,2),
	PaymentDate DATE,
	FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
	FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
			);

INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate)
VALUES
    (1, 1, 1, 100.00, '2023-10-15'),
    (2, 2, 2, 150.00, '2023-10-17'),
    (3, 3, 3, 80.00, '2023-10-16'),
    (4, 4, 4, 200.00, '2023-10-20'),
    (5, 5, 5, 120.00, '2023-10-18'),
    (6, 6, 6, 180.00, '2023-10-19'),
    (7, 7, 7, 50.00, '2023-10-22'),
    (8, 8, 8, 130.00, '2023-10-21'),
    (9, 9, 9, 90.00, '2023-10-23'),
    (10, 10, 10, 110.00, '2023-10-25'),
    (11, 11, 11, 100.00, '2023-10-24'),
    (12, 12, 12, 150.00, '2023-10-27'),
    (13, 13, 13, 80.00, '2023-10-26'),
    (14, 14, 14, 200.00, '2023-10-28'),
    (15, 15, 15, 120.00, '2023-10-30'),
    (16, 16, 16, 180.00, '2023-10-31'),
    (17, 17, 17, 50.00, '2023-11-01'),
    (18, 18, 18, 130.00, '2023-11-02'),
    (19, 19, 19, 90.00, '2023-11-03'),
    (20, 20, 20, 110.00, '2023-11-04');

USE task_db;
SELECT * FROM User_table;
SELECT * FROM Courier;
SELECT * FROM CourierServices;
SELECT * FROM Employee;
SELECT * FROM Location;
SELECT * FROM Payment;
SELECT * FROM Courier;


-- **************Task 2: Select,Where **************

--1. List all customers: 
SELECT Name from User_table;

--2. List all orders for a specific customer: 
SELECT * FROM User_table u
JOIN
Courier c ON u.Name = c.SenderName
WHERE u.Name = 'Alice Johnson';

--3. List all couriers: 
SELECT * FROM Courier;

--4. List all packages for a specific order: 
SELECT * FROM Courier WHERE SenderName = 'Alice Johnson';

--5. List all deliveries for a specific courier: 
SELECT * FROM Courier WHERE ReceiverName = 'Bob Smith';

--6. List all undelivered packages: 
SELECT * FROM Courier WHERE Status != 'Delivered';

--7. List all packages that are scheduled for delivery today: 
SELECT * FROM Courier WHERE Status = 'Out for Delivery';

--8. List all packages with a specific status: 
SELECT * FROM Courier WHERE Status = 'Pending';

--9. Calculate the total number of packages for each courier:
SELECT SenderName, COUNT(*) AS TotalPackages FROM Courier GROUP BY SenderName;

--10. Find the average delivery time for each courier Output: 0 coz of my data
SELECT SenderName, AVG(DATEDIFF(DAY, p.PaymentDate, c.DeliveryDate)) AS AverageDeliveryTime
FROM Courier c
JOIN Payment p ON c.CourierID = p.CourierID
GROUP BY SenderName;

--11. List all packages with a specific weight range:
SELECT * FROM Courier WHERE Weight BETWEEN 2.1 AND 3;

--12. Retrieve employees whose names contain 'John': 
SELECT * FROM 

--13. Retrieve all courier records with payments greater than $50: 



-- all tables merged
SELECT u.UserID, u.Name, 
		c.CourierID AS SenderID, c.SenderName, cs.ServiceID, cs.ServiceName, 
		e.Name AS EmployeeName, 
		l.LocationID, l.LocationName, 
		p.PaymentID
FROM User_table u
JOIN Courier c ON u.UserID = c.CourierID   
JOIN Payment p ON c.CourierID = p.CourierID
JOIN Location l ON p.LocationID = l.LocationID
JOIN CourierServices cs ON c.CourierID = cs.ServiceID  
JOIN Employee e ON c.CourierID = e.EmployeeID;  

-- **************Task 3: GroupBy, Aggregate Functions, Having, Order By, where **************

USE task_db;
SELECT * FROM User_table;
SELECT * FROM Courier;
SELECT * FROM CourierServices;
SELECT * FROM Employee;
SELECT * FROM Location;
SELECT * FROM Payment;


--14. Find the total number of couriers handled by each employee. 


--15. Calculate the total revenue generated by each location 
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalRevenue
FROM Location l
JOIN Payment p
ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName;


--16. Find the total number of couriers delivered to each location. 
SELECT l.LocationID, l.LocationName, COUNT(c.CourierID) AS TotalCouriersDelivered
FROM Location l
JOIN Payment p ON l.LocationID = p.LocationID
JOIN Courier c ON p.CourierID = c.CourierID
WHERE c.Status = 'Delivered'  -- Only count delivered couriers
GROUP BY l.LocationID, l.LocationName;


--17. Find the courier with the highest average delivery time: 
SELECT c.CourierID, c.TrackingNumber, AVG(DATEDIFF(DAY, p.PaymentDate, c.DeliveryDate)) AS AvgDeliveryTime
FROM Courier c
JOIN Payment p ON c.CourierID = p.CourierID
WHERE c.DeliveryDate IS NOT NULL  -- Only include couriers that have been delivered
GROUP BY c.CourierID, c.TrackingNumber
ORDER BY AvgDeliveryTime DESC
-- here all the orders are paid on date of delivery 


--18. Find Locations with Total Payments Less Than a Certain Amount 
SELECT * FROM Location;
SELECT * FROM Payment;

SELECT L.LocationID, L.LocationName, P.Amount, P.PaymentDate
FROM Location L
LEFT JOIN Payment P ON L.LocationID = P.LocationID
WHERE P.Amount >= 50;


--19. Calculate Total Payments per Location 
SELECT L.LocationID, L.LocationName, SUM(P.Amount) AS TotalPayments
FROM Location L
JOIN Payment P ON L.LocationID = P.LocationID
GROUP BY L.LocationID, L.LocationName;


--20. Retrieve couriers who have received payments totaling more than $1000 in a specific location 
--(LocationID = X): 
SELECT * FROM Courier;
SELECT * FROM Location;
SELECT * FROM Payment;

SELECT C.CourierID, C.SenderName, C.ReceiverName, SUM(P.Amount) AS TotalPayments
FROM Courier C
JOIN Payment P ON C.CourierID = P.CourierID
WHERE P.LocationID = 14
GROUP BY C.CourierID, C.SenderName, C.ReceiverName
HAVING SUM(P.Amount) > 100;


--21. Retrieve couriers who have received payments totaling more than $1000 after a certain date 
--(PaymentDate > 'YYYY-MM-DD'): 
SELECT * FROM Courier;
SELECT * FROM Payment;

SELECT C.CourierID, C.SenderName, P.LocationID, P.PaymentDate, SUM(P.Amount) AS TotalPayment
FROM Courier C
INNER JOIN Payment P ON C.CourierID = P.CourierID
WHERE P.PaymentDate > '2023-10-10'
GROUP BY C.CourierID, C.SenderName, C.TrackingNumber, P.LocationID, P.PaymentDate
HAVING SUM(P.Amount) > 100;


--22. Retrieve locations where the total amount received is more than $5000 before a certain date 
--(PaymentDate > 'YYYY-MM-DD')
SELECT L.LocationID, L.LocationName, P.PaymentDate, SUM(P.Amount) AS TotalPayment
FROM Location L
INNER JOIN Payment P ON L.LocationID = P.LocationID
WHERE P.PaymentDate < '2023-10-30'
GROUP BY L.LocationID, L.LocationName, P.PaymentDate
HAVING SUM(P.Amount) > 110;


-- ************** Task 4: Inner Join,Full Outer Join, Cross Join, Left Outer Join,Right Outer Join
SELECT * FROM User_table;
SELECT * FROM Courier;
SELECT * FROM CourierServices;
SELECT * FROM Payment;
SELECT * FROM Location;
SELECT * FROM Employee;
USE task_db;

--23. Retrieve Payments with Courier Information 
SELECT * FROM Payment;
SELECT * FROM Courier;

SELECT P.PaymentID, C.CourierID, P.Amount, P.PaymentDate, C.SenderName, C.TrackingNumber
FROM Payment P
INNER JOIN Courier C ON P.CourierID = C.CourierID;

--24. Retrieve Payments with Location Information 
SELECT * FROM Payment;
SELECT * FROM Location;

SELECT P.PaymentID, L.LocationID, P.Amount, P.PaymentDate, L.LocationName, L.Address
FROM Payment P
INNER JOIN Location L 
ON P.LocationID = L.LocationID;

SELECT P.PaymentID, L.LocationID, P.Amount, P.PaymentDate, L.LocationName, L.Address
FROM Payment P
LEFT JOIN Location L			-- gives null where no location info present
ON P.LocationID = L.LocationID;


--25. Retrieve Payments with Courier and Location Information 
SELECT P.PaymentID, C.CourierID, L.LocationID, P.Amount, C.SenderName, L.LocationName 
FROM Payment P
INNER JOIN Courier C ON P.CourierID = C.CourierID
INNER JOIN Location L ON P.LocationID = L.LOcationID;

--26. List all payments with courier details INNER will give details where there is match
SELECT * FROM Payment P
INNER JOIN Courier C
ON P.CourierID = C.CourierID;

--27. Total payments received for each courier 
SELECT C.CourierID, C.SenderName, SUM(P.Amount) AS TotalPayments
FROM Courier C
INNER JOIN Payment P
ON C.CourierID = P.CourierID
GROUP BY C.CourierID, C.SenderName;

--28. List payments made on a specific date 
SELECT * FROM Payment
WHERE PaymentDate = '2023-10-15';

--29. Get Courier Information for Each Payment 
SELECT * 
FROM Payment P
INNER JOIN Courier C ON P.CourierID = C.CourierID;

--30. Get Payment Details with Location 
SELECT * FROM 
Payment P
INNER JOIN Location L ON P.LocationID = L.LocationID;

--31. Calculating Total Payments for Each Courier
SELECT C.CourierID, C.SenderName, SUM(P.Amount) AS TotalPayment
FROM Courier C
LEFT JOIN Payment P ON C.CourierID = P.CourierID
GROUP BY C.CourierID, C.SenderName;

--32. List Payments Within a Date Range 
SELECT *
FROM Payment
WHERE PaymentDate BETWEEN '2023-10-05' AND '2023-10-25';

--33. Retrieve a list of all users and their corresponding courier records, including cases where there are no matches on either side 
SELECT * FROM User_table;
SELECT * FROM Courier;
SELECT * FROM CourierServices;

SELECT U.UserID, U.Name, C.CourierID, C.SenderName, C.ReceiverName
FROM User_table U
FULL OUTER JOIN Courier C ON U.Name = C.SenderName OR U.Name = C.ReceiverName;

--34. Retrieve a list of all couriers and their corresponding services, including cases where there are no matches on either side 
SELECT *
FROM Courier C
FULL OUTER JOIN CourierServices CS ON C.CourierID = CS.ServiceID;

--35. Retrieve a list of all employees and their corresponding payments, including cases where there are no matches on either side 
SELECT * FROM Employee;
SELECT * FROM Payment;

SELECT * 
FROM Employee E 
FULL OUTER JOIN Payment P ON E.EmployeeID = P.CourierID; 

--36. List all users and all courier services, showing all possible combinations. 
SELECT * 
FROM User_table 
CROSS JOIN CourierServices;

--37. List all employees and all locations, showing all possible combinations:
SELECT *
FROM Employee
CROSS JOIN Location;

--38. Retrieve a list of couriers and their corresponding sender information (if available) 
SELECT * FROM Courier;
SELECT * FROM User_table;
SELECT C.CourierID, C.SenderName, U.UserID, U.Name AS SenderUserName
FROM Courier C
LEFT JOIN User_table U ON C.SenderName = U.Name;

--39. Retrieve a list of couriers and their corresponding receiver information (if available): 
SELECT C.CourierID, C.SenderName, C.ReceiverName, U.Email as ReceiverMail, U.ContactNumber 
FROM Courier C
LEFT JOIN User_table U ON C.ReceiverName = U.Name;

--40. Retrieve a list of couriers along with the courier service details (if available): 
SELECT * FROM Courier;
SELECT * FROM CourierServices;

SELECT * 
FROM Courier C
LEFT JOIN CourierServices CS ON C.ServiceID = CS.ServiceID;

--41. Retrieve a list of employees and the number of couriers assigned to each employee: 
SELECT * FROM Employee;

--42. Retrieve a list of locations and the total payment amount received at each location: 
SELECT L.LocationID, L.LocationName, SUM(P.Amount) AS TotalPayment
FROM Location L
LEFT JOIN Payment P ON L.LocationID = P.LocationID
GROUP BY L.LocationID, L.LocationName;

--43. Retrieve all couriers sent by the same sender (based on SenderName). 
SELECT * FROM Courier;
SELECT * 
FROM Courier
WHERE SenderName = 'Alice Johnson';


--44. List all employees who share the same role. 
SELECT * FROM Employee;

SELECT E1.Name AS Employee1, E2.Name AS Employee2, E1.role
FROM Employee E1
JOIN Employee E2 ON E1.Role = E2.Role AND E1.EmployeeID != E2.EmployeeID
ORDER BY E1.Role;

SELECT E1.Role, STRING_AGG(E1.Name, ' , ') AS Employees
FROM Employee E1
GROUP BY E1.Role
ORDER BY E1.Role;

--45. Retrieve all payments made for couriers sent from the same location.

--SELECT CAST(C.SenderAddress AS VARCHAR(255)) AS SenderAddress, P.PaymentID, P.Amount, P.PaymentDate
--FROM Courier C
--JOIN Payment P ON C.CourierID = P.CourierID
--WHERE C.SenderAddress IS NOT NULL
--GROUP BY CAST(C.SenderAddress AS VARCHAR(255)), P.PaymentID, P.Amount, P.PaymentDate
--HAVING COUNT(C.CourierID) > 1;

--46. Retrieve all couriers sent from the same location (based on SenderAddress).
SELECT * FROM Courier;

--SELECT 
--    c.SenderAddress, 
--    COUNT(c.CourierID) AS NumberOfCouriers
--FROM 
--    Courier c
--GROUP BY 
--    c.SenderAddress
--HAVING 
--    COUNT(c.CourierID) > 1;  

--47. List employees and the number of couriers they have delivered: 

--SELECT * FROM CourierServices;
--SELECT E.Name AS EmployeeName, COUNT(C.CourierID) AS NumberOfCouriersDelivered
--FROM Courier C
--JOIN Employee E ON C.ReceiverName = E.Name  
--GROUP BY E.Name;


--48. Find couriers that were paid an amount greater than the cost of their respective courier services 

--SELECT c.TrackingNumber, p.Amount AS PaymentAmount, cs.Cost AS ServiceCost
--FROM Payment p
--JOIN Courier c ON p.CourierID = c.CourierID
--JOIN CourierServices cs ON c.CourierID = cs.ServiceID  -- Assuming Courier uses ServiceID to reference CourierServices
--WHERE p.Amount > cs.Cost;



-- ************** Scope: Inner Queries, Non Equi Joins, Equi joins,Exist,Any,All 

SELECT * FROM User_table;
SELECT * FROM Courier;
SELECT * FROM CourierServices;
SELECT * FROM Payment;
SELECT * FROM Location;
SELECT * FROM Employee;
USE task_db;

--49. Find couriers that have a weight greater than the average weight of all couriers 
SELECT * FROM Courier 
WHERE Weight > (SELECT AVG(Weight) FROM Courier);

--50. Find the names of all employees who have a salary greater than the average salary: 
SELECT * FROM Employee
WHERE Salary > (SELECT AVG(Salary) FROM Employee);

--51. Find the total cost of all courier services where the cost is less than the maximum cost 
SELECT SUM(Cost) AS TotalCost
FROM CourierServices
WHERE Cost < (SELECT MAX(Cost) FROM CourierServices);

--52. Find all couriers that have been paid for 
SELECT * 
FROM Courier C
JOIN Payment P ON C.CourierID = P.CourierID;

--53. Find the locations where the maximum payment amount was made 
SELECT * 
FROM Location L
JOIN Payment P ON L.LocationID = P.LocationID
WHERE P.Amount = (SELECT MAX(Amount) FROM Payment);

--54. Find all couriers whose weight is greater than the weight of all couriers sent by a specific sender 
--(e.g., 'SenderName'): SELECT * FROM CourierWHERE SenderName = 'Alice Johnson';   -- 2.50SELECT *FROM Courier CWHERE C.Weight > (SELECT MAX(Weight)					FROM Courier					WHERE SenderName = 'Alice Johnson');