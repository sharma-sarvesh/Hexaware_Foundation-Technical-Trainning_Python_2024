--1. Provide a SQL script that initializes the database for the Pet Adoption Platform ”PetPals”.
IF NOT EXISTS (SELECT * FROM sys.database WHERE Name = 'petpals')
BEGIN
	CREATE DATABASE petpals;
END
GO

USE petpals;

--2. Create tables for pets, shelters, donations, adoption events, and participants. 
-- Pets Table
--3. Define appropriate primary keys, foreign keys, and constraints. 
--4. Ensure the script handles potential errors, such as if the database or tables already exist.

IF NOT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Pets')
BEGIN
	CREATE TABLE Pets (
		PetId INT PRIMARY KEY IDENTITY(1,1),
		Name VARCHAR(255) NOT NULL,
		Age INT CHECK(Age >= 0),
		Breed VARCHAR(255),
		Type VARCHAR(255),
		AvailableForAdoption BIT DEFAULT 1,
		ShelterID INT,
		FOREIGN KEY (ShelterID) REFERENCES Shelters(ShelterId) ON DELETE SET NULL
	);
END
GO

INSERT INTO Pets (Name, Age, Breed, Type, AvailableForAdoption, ShelterID) VALUES
	('Bruno', 3, 'Labrador', 'Dog', 1, 11),  
	('Fluffy', 2, 'Persian', 'Cat', 1, 12),  
	('Rex', 4, 'German Shepherd', 'Dog', 0, 13),  
	('Simba', 1, 'Golden Retriever', 'Dog', 1, 14),  
	('Tuffy', 5, 'Shih Tzu', 'Dog', 1, 15),  
	('Leo', 7, 'Siamese', 'Cat', 0, 16),  
	('Rocky', 3, 'Bulldog', 'Dog', 1, 17),  
	('Jelly', 2, 'Sphynx', 'Cat', 1, 18),  
	('Sheru', 8, 'Doberman', 'Dog', 0, 19),  
	('Melly', 1, 'Ragdoll', 'Cat', 1, 20);  

-- Shelters Table
CREATE TABLE Shelters (
	ShelterId INT PRIMARY KEY IDENTITY(11,1),
	ShelterName VARCHAR(255) NOT NULL,
	ShelterLocation VARCHAR(255) NOT NULL
	);

INSERT INTO Shelters (ShelterName, ShelterLocation) VALUES
	('Happy Paws Shelter', 'Mumbai'),
	('Companion Care Shelter', 'Chennai'),
	('Pet Haven', 'Delhi'),
	('Furry Friends Shelter', 'Kolkata'),
	('Paw Prints Shelter', 'Bangalore'),
	('Safe Shelter', 'Hyderabad'),
	('Hope for Paws', 'Pune'),
	('Animal Rescue Shelter', 'Jaipur'),
	('Pet Paradise Shelter', 'Ahmedabad'),
	('Forever Friends Shelter', 'Lucknow');


-- Donations Table
CREATE TABLE Donations(
    DonationID INT PRIMARY KEY IDENTITY(21,1),
    DonorName VARCHAR(255),
    DonationType VARCHAR(50),
    DonationAmount DECIMAL(10,2),
    DonationItem VARCHAR(255),
    DonationDate DATETIME DEFAULT GETDATE(),
	ShelterId INT,
	FOREIGN KEY (ShelterId) REFERENCES Shelters(ShelterId) ON DELETE SET NULL
);

INSERT INTO Donations(DonorName, DonationType, DonationAmount, DonationItem, DonationDate, ShelterID) VALUES
    ('Rajesh Gupta', 'Cash', 10000, NULL, '2024-01-15 10:30:00', 11),
    ('Anita Sharma', 'Item', NULL, 'Dog Food', '2024-02-10 14:00:00', 12),
    ('Vikram Patel', 'Cash', 5000, NULL, '2024-03-05 09:15:00', 13),
    ('Suman Rao', 'Cash', 8000, NULL, '2024-04-12 16:45:00', 14),
    ('Arjun Desai', 'Item', NULL, 'Cat Food', '2024-05-20 11:20:00', 15),
    ('Kavita Mehta', 'Cash', 6000, NULL, '2024-06-15 08:00:00', 16),
    ('Neha Joshi', 'Item', NULL, 'Dog Toys', '2024-07-10 12:30:00', 17),
    ('Manoj Singh', 'Cash', 15000, NULL, '2024-08-18 15:00:00', 18),
    ('Rani Kapoor', 'Item', NULL, 'Pet Beds', '2024-09-22 17:10:00', 19),
    ('Ajay Yadav', 'Cash', 7000, NULL, '2024-10-01 09:50:00', 20);


-- AdoptionEvents Table
CREATE TABLE AdoptionEvents(
	EventId INT PRIMARY KEY IDENTITY(31,1),
	EventName VARCHAR(255),
	EventDate DATETIME DEFAULT GETDATE(),
	EventLocation VARCHAR(255)
	);

INSERT INTO AdoptionEvents(EventName, EventDate, EventLocation) VALUES
    ('Pets Adoption Mumbai', '2024-01-20 10:00:00', 'Mumbai'),
    ('Pet Adoption Fest', '2024-02-25 11:30:00', 'Chennai'),
    ('Furry Friends Fest', '2024-03-15 14:00:00', 'Delhi'),
    ('Rescue Adoption Drive', '2024-04-10 09:00:00', 'Kolkata'),
    ('Happy Tails Event', '2024-05-05 13:00:00', 'Bangalore'),
    ('Pawfect Fest', '2024-06-08 15:30:00', 'Hyderabad'),
    ('Pets Drive', '2024-07-18 10:45:00', 'Pune'),
    ('Adopt for Love Event', '2024-08-22 12:30:00', 'Jaipur'),
    ('Find a Friend Event', '2024-09-19 11:15:00', 'Ahmedabad'),
    ('Pets Fest', '2024-10-10 16:00:00', 'Lucknow');


-- Participants Table
CREATE TABLE Participants(
	ParticipantId INT PRIMARY KEY IDENTITY(41,1),
	ParticipantName VARCHAR(255),
	EventID INT,
	FOREIGN KEY (EventID) REFERENCES AdoptionEvents(EventId) ON DELETE CASCADE
	);

INSERT INTO Participants(ParticipantName, EventID) VALUES
	('Sahil', 31),
	('Rajesh', 31),
	('Rahul', 32),
	('Ankita', 32),
	('Tanmay', 33),
	('Vikram', 33),
	('Om', 34),
	('Ishika', 34),
	('Pragya', 35),
	('Raj', 35);


SELECT * FROM Pets;
SELECT * FROM Shelters;
SELECT * FROM Donations;
SELECT * FROM AdoptionEvents;
SELECT * FROM Participants;



--5. Write an SQL query that retrieves a list of available pets (those marked as available for adoption) 
--from the "Pets" table. Include the pet's name, age, breed, and type in the result set. Ensure that 
--the query filters out pets that are not available for adoption.
SELECT Name as PetName, Age as PetAge, Breed as PetBreed, Type as PetType
FROM Pets
WHERE AvailableForAdoption = 1;

--6. Write an SQL query that retrieves the names of participants (shelters and adopters) registered 
--for a specific adoption event. Use a parameter to specify the event ID. Ensure that the query 
--joins the necessary tables to retrieve the participant names and types.
SELECT P.ParticipantName, AE.EventId, AE.EventName, AE.EventLocation  
FROM Participants as P
JOIN AdoptionEvents as AE ON P.EventId = AE.EventId
WHERE AE.EventID = 31;


--7. Create a stored procedure in SQL that allows a shelter to update its information (name and 
--location) in the "Shelters" table. Use parameters to pass the shelter ID and the new information. 
--Ensure that the procedure performs the update and handles potential errors, such as an invalid 
--shelter ID.
CREATE PROCEDURE UpdateShelterInfo 
	@ShelterId INT, @NewShelterName VARCHAR(255), @NewShelterLocation VARCHAR(255)
AS
BEGIN
	UPDATE Shelters
	SET ShelterName = @NewShelterName,
		ShelterLocation = @NewShelterLocation
	WHERE ShelterId = @ShelterId
	IF @@ROWCOUNT = 0
	BEGIN
		PRINT 'Invalid ShelterId';
	END
	ELSE
	BEGIN
		PRINT 'Shelter Information Updates Successfully';
	END
END;

EXEC UpdateShelterInfo @ShelterId = 12, @NewShelterName = 'New Care Shelter', @NewShelterLocation = 'Aurangabad';
SELECT * FROM Shelters;

--8. Write an SQL query that calculates and retrieves the total donation amount for each shelter (by 
--shelter name) from the "Donations" table. The result should include the shelter name and the 
--total donation amount. Ensure that the query handles cases where a shelter has received no 
--donations.
SELECT * FROM Shelters;
SELECT * FROM Donations;

SELECT S.ShelterName, SUM(D.DonationAmount) as TotalDonation
FROM Shelters as S
LEFT JOIN Donations as D ON S.ShelterId = D.ShelterID
GROUP BY S.ShelterName;


--9. Write an SQL query that retrieves the names of pets from the "Pets" table that do not have an 
--owner (i.e., where "OwnerID" is null). Include the pet's name, age, breed, and type in the result set.
SELECT * FROM Pets;

ALTER TABLE Pets ADD OwnerId INT;

UPDATE Pets
SET OwnerId = 0 
WHERE AvailableForAdoption = 0;



SELECT Name, Age, Breed, Type
FROM Pets
WHERE OwnerId IS NULL;


--10. Write an SQL query that retrieves the total donation amount for each month and year (e.g., 
--January 2023) from the "Donations" table. The result should include the month-year and the 
--corresponding total donation amount. Ensure that the query handles cases where no donations 
--were made in a specific month-year
SELECT * FROM Donations;

SELECT 
    FORMAT(DonationDate, 'MMMM') + '-' + CAST(YEAR(DonationDate) AS VARCHAR) AS MonthYear, 
    SUM(DonationAmount) AS TotalDonationAmount
FROM 
    Donations 
GROUP BY FORMAT(DonationDate, 'MMMM'),YEAR(DonationDate);

--11. Retrieve a list of distinct breeds for all pets that are either aged between 1 and 3 years or older
--than 5 years.
SELECT * FROM Pets;

SELECT DISTINCT Breed, Type
FROM Pets
WHERE Age BETWEEN 1 AND 3 OR Age > 5;

--12. Retrieve a list of pets and their respective shelters where the pets are currently available for 
--adoption.

SELECT  P.Name AS PetName, P.Age AS PetAge, P.Breed AS PetBreed, 
		S.ShelterName, S.ShelterLocation
FROM Pets P
JOIN Shelters S ON P.ShelterID = S.ShelterID
WHERE p.AvailableForAdoption = 1;


--13. Find the total number of participants in events organized by shelters located in specific city.
--Example: City=Chennai
SELECT * FROM Pets;
SELECT * FROM Shelters;
SELECT * FROM Donations;
SELECT * FROM AdoptionEvents;
SELECT * FROM Participants;

SELECT COUNT(P.ParticipantId) AS TotalParticipants
FROM Participants P
JOIN AdoptionEvents A ON P.EventID = A.EventId
JOIN Shelters s ON a.EventLocation = s.ShelterLocation
WHERE s.ShelterLocation = 'Mumbai';


--14. Retrieve a list of unique breeds for pets with ages between 1 and 5 years.
SELECT DISTINCT Breed, Type
FROM Pets
WHERE AGE BETWEEN 1 AND 5;

--15. Find the pets that have not been adopted by selecting their information from the 'Pet' table.
SELECT * FROM PETS
WHERE AvailableForAdoption = 1;


--16. Retrieve the names of all adopted pets along with the adopter's name from the 'Adoption' and 
--'User' tables.

CREATE TABLE Adoptions (
    AdoptionId INT PRIMARY KEY IDENTITY(1,1),
    PetId INT,
    AdopterName VARCHAR(255),
    AdoptionDate DATETIME DEFAULT GETDATE(),
    ShelterId INT,
    FOREIGN KEY (PetId) REFERENCES Pets(PetId) ON DELETE CASCADE,
    FOREIGN KEY (ShelterId) REFERENCES Shelters(ShelterId) ON DELETE SET NULL
);

INSERT INTO Adoptions (PetId, AdopterName, AdoptionDate, ShelterId) VALUES
    (3, 'Amit', '2024-03-10 10:00:00', 13),
    (6, 'Sarvesh', '2024-06-20 12:30:00', 16),
    (8, 'Jay', '2024-08-15 14:00:00', 17),
    (9, 'Pratham', '2024-09-05 09:45:00', 18);

SELECT * FROM Adoptions;

SELECT P.Name AS PetName, A.AdopterName
FROM Adoptions A
JOIN Pets P ON A.PetId = P.PetId
WHERE P.AvailableForAdoption = 0;


--17. Retrieve a list of all shelters along with the count of pets currently available for adoption in each 
--shelter.
SELECT * FROM Shelters;

SELECT S.ShelterName, S.ShelterLocation, COUNT(P.PetId) AS AvailablePetsCount
FROM Shelters S
LEFT JOIN Pets P ON S.ShelterId = P.ShelterId AND P.AvailableForAdoption = 1
GROUP BY S.ShelterId, ShelterName, S.ShelterLocation;


--18. Find pairs of pets from the same shelter that have the same breed.
SELECT P1.Name AS Pet1, P2.Name AS Pet2, P1.Breed, S.ShelterName
FROM Pets P1
JOIN Pets P2 ON P1.Breed = P2.Breed AND P1.PetId != P2.PetId
JOIN Shelters S ON P1.ShelterID = S.ShelterId;
-- Result is NA because no common pets in Database.

--19. List all possible combinations of shelters and adoption events.
SELECT * FROM Shelters
CROSS JOIN AdoptionEvents;

--20. Determine the shelter that has the highest number of adopted pets

SELECT S.ShelterName, COUNT(A.PetId) AS NumberOfAdoptedPets
FROM Adoptions A
JOIN Shelters S ON A.ShelterId = S.ShelterId
GROUP BY S.ShelterName
ORDER BY NumberOfAdoptedPets DESC;

