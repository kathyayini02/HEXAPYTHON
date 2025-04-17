
USE VirtualArtGallery;


 /*
CREATE TABLE Artists (
    ArtistID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(255) NOT NULL,
    Biography TEXT,
    BirthDate DATE,
    Nationality VARCHAR(100),
    Website VARCHAR(255),
    ContactInfo TEXT
);


CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(100) UNIQUE NOT NULL,
    PasswordHash NVARCHAR(255) NOT NULL,
    Email NVARCHAR(255) UNIQUE NOT NULL,
    FirstName NVARCHAR(100),
    LastName NVARCHAR(100),
    DateOfBirth DATE,
    ProfilePicture NVARCHAR(500),
    Role NVARCHAR(50) DEFAULT 'User'
);


CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL
);


CREATE TABLE Artworks (
    ArtworkID INT PRIMARY KEY IDENTITY(1,1),
    Title VARCHAR(255) NOT NULL,
    ArtistID INT,
    CategoryID INT,
    CreationDate DATE,
    Medium VARCHAR(255),
    ImageURL VARCHAR(255),
    Price DECIMAL(10,2) CHECK (Price >= 0),
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE SET NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);


CREATE TABLE Galleries (
    GalleryID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Location TEXT,
    CuratorID INT,
    OpeningHours NVARCHAR(255),
    FOREIGN KEY (CuratorID) REFERENCES Artists(ArtistID) ON DELETE SET NULL
);


CREATE TABLE User_Favorite_Artwork (
    UserID INT,
    ArtworkID INT,
    PRIMARY KEY (UserID, ArtworkID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (ArtworkID) REFERENCES Artworks(ArtworkID) ON DELETE CASCADE
);


CREATE TABLE Artwork_Gallery (
    ArtworkID INT,
    GalleryID INT,
    DisplayOrder INT DEFAULT 1,
    PRIMARY KEY (ArtworkID, GalleryID),
    FOREIGN KEY (ArtworkID) REFERENCES Artworks(ArtworkID) ON DELETE CASCADE,
    FOREIGN KEY (GalleryID) REFERENCES Galleries(GalleryID) ON DELETE CASCADE
);


CREATE TABLE User_Galleries (
    GalleryID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT,
    Name NVARCHAR(255) NOT NULL,
    Description TEXT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);


CREATE TABLE User_Gallery_Artworks (
    GalleryID INT,
    ArtworkID INT,
    PRIMARY KEY (GalleryID, ArtworkID),
    FOREIGN KEY (GalleryID) REFERENCES User_Galleries(GalleryID) ON DELETE CASCADE,
    FOREIGN KEY (ArtworkID) REFERENCES Artworks(ArtworkID) ON DELETE CASCADE
);



INSERT INTO Artists (Name, Biography, BirthDate, Nationality, Website, ContactInfo) 
VALUES
('Pablo Picasso', 'Spanish painter and sculptor.', '1881-10-25', 'Spanish', 'https://picasso.com', 'picasso@art.com'),
('Vincent van Gogh', 'Dutch post-impressionist painter.', '1853-03-30', 'Dutch', 'https://vangogh.com', 'vangogh@art.com'),
('Leonardo da Vinci', 'Italian polymath.', '1452-04-15', 'Italian', 'https://davinci.com', 'davinci@art.com'),
('Claude Monet', 'French Impressionist painter.', '1840-11-14', 'French', 'https://monet.com', 'monet@art.com'),
('Salvador Dalí', 'Spanish surrealist artist.', '1904-05-11', 'Spanish', 'https://dali.com', 'dali@art.com'),
('Frida Kahlo', 'Mexican painter known for self-portraits.', '1907-07-06', 'Mexican', 'https://kahlo.com', 'kahlo@art.com'),
('Edvard Munch', 'Norwegian painter, known for "The Scream".', '1863-12-12', 'Norwegian', 'https://munch.com', 'munch@art.com'),
('Rembrandt', 'Dutch painter and printmaker.', '1606-07-15', 'Dutch', 'https://rembrandt.com', 'rembrandt@art.com'),
('Andy Warhol', 'American pop artist.', '1928-08-06', 'American', 'https://warhol.com', 'warhol@art.com'),
('Georgia O’Keeffe', 'American modernist painter.', '1887-11-15', 'American', 'https://okeeffe.com', 'okeeffe@art.com');


INSERT INTO Users (Username, PasswordHash, Email, FirstName, LastName, DateOfBirth, ProfilePicture) 
SELECT 'artlover123', 'hashedpassword1', 'artlover@example.com', 'John', 'Doe', '1995-08-21', 'profilepic1.jpg'
WHERE NOT EXISTS (SELECT 1 FROM Users WHERE Email = 'artlover@example.com');

INSERT INTO Users (Username, PasswordHash, Email, FirstName, LastName, DateOfBirth, ProfilePicture) 
SELECT 'galleryfan', 'hashedpassword2', 'galleryfan@example.com', 'Jane', 'Smith', '1992-03-15', 'profilepic2.jpg'
WHERE NOT EXISTS (SELECT 1 FROM Users WHERE Email = 'galleryfan@example.com');


INSERT INTO Categories (Name) 
VALUES
('Painting'), ('Sculpture'), ('Photography'), ('Digital Art'), ('Illustration'),
('Abstract Art'), ('Watercolor'), ('Printmaking'), ('Graphic Design'), ('Conceptual Art');


INSERT INTO Artworks (Title, ArtistID, CategoryID, CreationDate, Medium, ImageURL, Price) 
VALUES
('Starry Night', 2, 1, '1889-06-01', 'Oil on Canvas', 'starry_night.jpg', 1000.00),
('Mona Lisa', 3, 1, '1503-10-01', 'Oil on Wood', 'mona_lisa.jpg', 5000.00);


INSERT INTO Galleries (Name, Description, Location, CuratorID, OpeningHours) 
VALUES
('Modern Art Gallery', 'A collection of modern masterpieces.', 'Paris, France', 1, '9AM - 6PM'),
('Renaissance Collection', 'Showcasing artworks from the Renaissance.', 'Florence, Italy', 3, '10AM - 5PM');


INSERT INTO Artwork_Gallery (ArtworkID, GalleryID)
SELECT 1, 1 WHERE NOT EXISTS (SELECT 1 FROM Artwork_Gallery WHERE ArtworkID = 1 AND GalleryID = 1);

INSERT INTO Artwork_Gallery (ArtworkID, GalleryID)
SELECT 2, 2 WHERE NOT EXISTS (SELECT 1 FROM Artwork_Gallery WHERE ArtworkID = 2 AND GalleryID = 2);


INSERT INTO User_Favorite_Artwork (UserID, ArtworkID)
SELECT 1, 1 WHERE NOT EXISTS (SELECT 1 FROM User_Favorite_Artwork WHERE UserID = 1 AND ArtworkID = 1);

INSERT INTO User_Favorite_Artwork (UserID, ArtworkID)
SELECT 2, 2 WHERE NOT EXISTS (SELECT 1 FROM User_Favorite_Artwork WHERE UserID = 2 AND ArtworkID = 2);


INSERT INTO User_Galleries (UserID, Name, Description)
SELECT 1, 'My Masterpieces', 'A collection of my favorite artworks'
WHERE NOT EXISTS (SELECT 1 FROM User_Galleries WHERE UserID = 1 AND Name = 'My Masterpieces');

INSERT INTO User_Galleries (UserID, Name, Description)
SELECT 2, 'Abstract Wonders', 'My favorite abstract paintings'
WHERE NOT EXISTS (SELECT 1 FROM User_Galleries WHERE UserID = 2 AND Name = 'Abstract Wonders');


INSERT INTO User_Gallery_Artworks (GalleryID, ArtworkID)
SELECT 1, 1 WHERE NOT EXISTS (SELECT 1 FROM User_Gallery_Artworks WHERE GalleryID = 1 AND ArtworkID = 1);

INSERT INTO User_Gallery_Artworks (GalleryID, ArtworkID)
SELECT 2, 2 WHERE NOT EXISTS (SELECT 1 FROM User_Gallery_Artworks WHERE GalleryID = 2 AND ArtworkID = 2);*/

select * from Artists;
select * from Users;
select * from Categories; 
select * from Artworks;
select * from Galleries;
select * from Artwork_Gallery;
select * from User_Favorite_Artwork;
select * from User_Galleries;
select * from User_Gallery_Artworks;