
USE PETPALS;



IF OBJECT_ID('dbo.Participants', 'U') IS NOT NULL DROP TABLE dbo.Participants;
IF OBJECT_ID('dbo.Adoption_Events', 'U') IS NOT NULL DROP TABLE dbo.Adoption_Events;
IF OBJECT_ID('dbo.Donations', 'U') IS NOT NULL DROP TABLE dbo.Donations;
IF OBJECT_ID('dbo.Pets', 'U') IS NOT NULL DROP TABLE dbo.Pets;
GO

-- Create PETS table
CREATE TABLE dbo.Pets (
    PetID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Age INT CHECK (Age > 0),
    Breed NVARCHAR(100) NOT NULL,
    Type NVARCHAR(10) CHECK (Type IN ('Dog', 'Cat')) NOT NULL,
    DogBreed NVARCHAR(100) NULL,
    CatColor NVARCHAR(100) NULL
);



CREATE TABLE dbo.Donations (
    DonationID INT IDENTITY(1,1) PRIMARY KEY,
    DonorName NVARCHAR(100) NOT NULL,
    Amount DECIMAL(10, 2) CHECK (Amount >= 0),
    ItemType NVARCHAR(100) NULL,
    DonationDate DATE NOT NULL
);


-- Create ADOPTION_EVENTS table
CREATE TABLE dbo.Adoption_Events (
    EventID INT IDENTITY(1,1) PRIMARY KEY,
    EventName NVARCHAR(100) NOT NULL,
    EventDate DATE NOT NULL
);


-- Create PARTICIPANTS table
CREATE TABLE dbo.Participants (
    ParticipantID INT IDENTITY(1,1) PRIMARY KEY,
    ParticipantName NVARCHAR(100) NOT NULL,
    EventID INT NOT NULL,
    FOREIGN KEY (EventID) REFERENCES dbo.Adoption_Events(EventID)
);
CREATE TABLE event_registrations (
    RegistrationID INT IDENTITY(1,1) PRIMARY KEY,
    EventID INT NOT NULL,
    ParticipantName NVARCHAR(100) NOT NULL,
    FOREIGN KEY (EventID) REFERENCES AdoptionEvents(EventID)
);

SELECT * FROM adoption_events;
INSERT INTO Adoption_Events (EventName, EventDate)
VALUES ('Spring Pet Drive', '2025-04-15');

