CREATE DATABASE TicketBookingSystem;

USE TicketBookingSystem;


CREATE TABLE Venue (
    venue_id INT PRIMARY KEY IDENTITY(1,1),
    venue_name VARCHAR(100),
    address VARCHAR(100)
);

CREATE TABLE Event (
    event_id INT PRIMARY KEY IDENTITY(1,1),
    event_name VARCHAR(100),
    event_date DATE,
    event_time TIME,
    venue_id INT,
    total_seats INT,
    available_seats INT,
    ticket_price DECIMAL(10, 2),
    event_type VARCHAR(20), -- ENUM not supported in SQL Server
    FOREIGN KEY (venue_id) REFERENCES Venue(venue_id)
);


CREATE TABLE Customer (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(15)
);


CREATE TABLE Booking (
    booking_id INT PRIMARY KEY IDENTITY(1,1),
    customer_id INT,
    event_id INT,
    num_tickets INT,
    total_cost DECIMAL(10, 2),
    booking_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id)
);


SELECT * FROM Venue;

SELECT * FROM Event;

SELECT * FROM Customer;

SELECT * FROM Booking;

