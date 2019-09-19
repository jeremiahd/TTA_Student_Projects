CREATE DATABASE Library
use Library

CREATE TABLE library_branch (
	BranchId int NOT NULL PRIMARY KEY IDENTITY(0,1),
	BranchName varchar(50),
	Address varchar(50)
)

CREATE TABLE publisher (
	PublisherName varchar(50) NOT NULL PRIMARY KEY,
	Address varchar(50),
	Phone varchar(50)
)

CREATE TABLE books (
	BookId int NOT NULL UNIQUE,
	Title varchar(50),
	PublisherName varchar(50) FOREIGN KEY REFERENCES publisher(PublisherName)
)

CREATE TABLE book_authors (
	BookId int FOREIGN KEY REFERENCES books(BookId),
	AuthorName varchar(50)
)

CREATE TABLE book_copies (
	BookId int FOREIGN KEY REFERENCES books(BookId),
	BranchId int FOREIGN KEY REFERENCES library_branch(BranchId),
	Number_Of_Copies int
)

CREATE TABLE borrower (
	CardNo int NOT NULL PRIMARY KEY IDENTITY(10000,1),
	Name varchar(50),
	Address varchar(50),
	Phone varchar(50)
)

CREATE TABLE book_loans (
	BookId int FOREIGN KEY REFERENCES books(BookId),
	BranchId int FOREIGN KEY REFERENCES library_branch(BranchId),
	CardNo int FOREIGN KEY REFERENCES borrower(CardNo),
	DateOut date,
	DateDue date
)

CREATE TABLE authors (
	BookID int FOREIGN KEY REFERENCES books(BookId),
	AuthorName varchar(50)
)