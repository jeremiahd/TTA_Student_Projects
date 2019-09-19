use Library

INSERT INTO library_branch
	(BranchName, Address)
VALUES
	('Sharpstown', '123 Sharp St, Sharpstown'),
	('Central', '543 Main St, CenterCity'),
	('Uptown', '987 Rich Ave, MoneyTown'),
	('Downtown', '432 Commute Ave, CrowdedCityUSA')
;

INSERT INTO publisher
	(PublisherName, Address, Phone)
VALUES
	('Picador USA', '123 Street St', '800-123-1234'),
	('Vintage', '123 Street St', '800-123-1234'),
	('Scholastic Press', '123 Street St', '800-123-1234'),
	('Gallup Press', '123 Street St', '800-123-1234'),
	('Broadway Books', '123 Street St', '800-123-1234'),
	('Berkley', '123 Street St', '800-123-1234'),
	('Penguin Books', '123 Street St', '800-123-1234'),
	('Riverhead Books', '123 Street St', '800-123-1234'),
	('Katherine Tegen Books', '123 Street St', '800-123-1234'),
	('Arthur A. Levine Books', '123 Street St', '800-123-1234'),
	('Random House Trade Paperbacks', '123 Street St', '800-123-1234'),
	('Knopf Books for Young Readers', '123 Street St', '800-123-1234'),
	('Bantam', '123 Street St', '800-123-1234'),
	('G. P. Putnam''s Sons', '123 Street St', '800-123-1234'),
	('Thomas Nelson', '123 Street St', '800-123-1234'),
	('Scribner', '123 Street St', '800-123-1234')
;

INSERT INTO books
	(BookID, Title, PublisherName)
VALUES
	(0, 'The Lost Tribe', 'Picador USA'),
	(1, 'Fifty Shades of Grey', 'Vintage'),
	(2, 'The Hunger Games', 'Scholastic Press'),
	(3, 'Catching Fire', 'Scholastic Press'),
	(4, 'StrengthsFinder', 'Gallup Press'),
	(5,'Mockingjay', 'Scholastic Press'),
	(6,'Fifty Shades Darker', 'Vintage'),
	(7,'Fifty Shades Freed', 'Vintage'),
	(8,'Gone Girl', 'Broadway Books'),
	(9,'The Help', 'Berkley'),
	(10,'The Fault in our Stars', 'Penguin Books'),
	(11,'The Girl on the Train', 'Riverhead Books'),
	(12,'Divergent', 'Katherine Tegen Books'),
	(13,'Harry Potter and the Deathly Hallows', 'Arthur A. Levine Books'),
	(14,'Unbroken', 'Random House Trade Paperbacks'),
	(15,'Wonder', 'Knopf Books for Young Readers'),
	(16,'A Game of Thrones', 'Bantam'),
	(17,'The Husband''s Secret', 'Berkley'),
	(18,'Who Moved My Cheese?', 'G. P. Putnam''s Sons'),
	(19,'Heaven is for Real', 'Thomas Nelson'),
	(20,'Misery', 'Scribner'),
	(21,'The Institute', 'Scribner')
;

INSERT INTO book_authors
	(BookID, AuthorName)
VALUES
	(0, 'Mark Lee'),
	(1, 'E L James'),
	(2, 'Suzanne Collins'),
	(3, 'Suzanne Collins'),
	(4, 'Tom Rath'),
	(5, 'Suzanne Collins'),
	(6, 'E L James'),
	(7, 'E L James'),
	(8, 'Gillian Flynn'),
	(9, 'Kathryn Stockett'),
	(10, 'John Green'),
	(11, 'Paula Hawkins'),
	(12, 'Veronica Roth'),
	(13, 'J. K. Rowling'),
	(14, 'Laura Hillenbrand'),
	(15, 'R. J. Palacio'),
	(16, 'George R.R. Martin'),
	(17, 'Liane Moriarty'),
	(18, 'Spencer Johnson'),
	(19, 'Todd Burpo'),
	(20, 'Stephen King'),
	(21, 'Stephen King')
;

INSERT INTO book_copies
	(BookID, BranchID, Number_Of_Copies)
VALUES
	('0', '0', '5'),
	('1', '0', '8'),
	('2', '0', '12'),
	('3', '0', '6'),
	('4', '0', '5'),
	('5', '0', '9'),
	('6', '0', '13'),
	('7', '0', '6'),
	('8', '0', '8'),
	('9', '0', '10'),
	('10', '1', '11'),
	('11', '1', '4'),
	('12', '1', '7'),
	('21', '1', '14'),
	('14', '1', '13'),
	('15', '1', '8'),
	('16', '1', '0'),
	('17', '1', '13'),
	('18', '1', '6'),
	('19', '1', '14'),
	('4', '2', '9'),
	('7', '2', '13'),
	('13', '2', '8'),
	('8', '2', '10'),
	('1', '2', '20'),
	('0', '2', '5'),
	('5', '2', '8'),
	('10', '2', '6'),
	('13', '2', '4'),
	('17', '2', '7'),
	('16', '3', '10'),
	('3', '3', '5'),
	('2', '3', '7'),
	('7', '3', '4'),
	('11', '3', '8'),
	('18', '3', '5'),
	('19', '3', '8'),
	('4', '3', '11'),
	('20', '3', '12'),
	('8', '3', '12')
;

INSERT INTO borrower
	(Name, Address, Phone)
VALUES
	('Jim Beam', '123 AfterWork Street', '123-345-3455'),
	('Margret Smith', '345 Asdf Ave', '345-345-3453'),
	('Betty White', '098 Some Rd', '123-123-1233'),
	('Tim Timothy', '111 Tim Rd', '000-000-0000'),
	('Forrest Gump', '123 Shrimp Ave', '333-444-5555'),
	('Sam Samson', '555 Samsonite road', '123-123-1233'),
	('Gip Gipperson', '555 Five St.', '543-534-5344'),
	('Mary Lamb', '12 Sheep Rd #B', '111-111-1111')
;

INSERT INTO book_loans
	(BookID, BranchID, CardNo, DateOut, DateDue)
VALUES
	('0', '0', '10000', '2019-09-01', '2019-09-08'),
	('1', '0', '10000', '2019-09-01', '2019-09-08'),
	('2', '0', '10000', '2019-09-01', '2019-09-08'),
	('3', '0', '10000', '2019-09-01', '2019-09-08'),
	('4', '0', '10000', '2019-09-01', '2019-09-08'),
	('5', '0', '10001', '2019-09-01', '2019-09-08'),
	('6', '0', '10001', '2019-09-01', '2019-09-08'),
	('7', '0', '10001', '2019-09-01', '2019-09-08'),
	('8', '0', '10001', '2019-09-01', '2019-09-08'),
	('9', '0', '10001', '2019-09-01', '2019-09-08'),
	('10', '1', '10002', '2019-09-02', '2019-09-09'),
	('10', '1', '10003', '2019-09-02', '2019-09-09'),
	('10', '1', '10004', '2019-09-02', '2019-09-09'),
	('11', '1', '10005', '2019-09-02', '2019-09-09'),
	('11', '1', '10006', '2019-09-02', '2019-09-09'),
	('11', '1', '10006', '2019-09-02', '2019-09-09'),
	('12', '1', '10000', '2019-09-02', '2019-09-09'),
	('13', '1', '10001', '2019-09-02', '2019-09-09'),
	('14', '1', '10002', '2019-09-02', '2019-09-09'),
	('15', '1', '10003', '2019-09-02', '2019-09-09'),
	('4', '2', '10004', '2019-09-05', '2019-09-12'),
	('4', '2', '10001', '2019-09-05', '2019-09-12'),
	('7', '2', '10002', '2019-09-05', '2019-09-12'),
	('7', '2', '10003', '2019-09-05', '2019-09-12'),
	('13', '2', '10004', '2019-09-05', '2019-09-12'),
	('8', '2', '10001', '2019-09-05', '2019-09-12'),
	('1', '2', '10005', '2019-09-05', '2019-09-12'),
	('0', '2', '10005', '2019-09-05', '2019-09-12'),
	('0', '2', '10006', '2019-08-01', '2019-08-08'),
	('10', '2', '10006', '2019-08-01', '2019-08-08'),
	('13', '2', '10002', '2019-08-01', '2019-08-08'),
	('17', '2', '10003', '2019-08-01', '2019-08-08'),
	('16', '3', '10004', '2019-08-01', '2019-08-08'),
	('3', '3', '10005', '2019-08-01', '2019-08-08'),
	('2', '3', '10006', '2019-08-01', '2019-08-08'),
	('7', '3', '10006', '2019-08-01', '2019-08-08'),
	('11', '3', '10002', '2019-07-01', '2019-07-08'),
	('18', '3', '10001', '2019-07-01', '2019-07-08'),
	('19', '3', '10003', '2019-07-01', '2019-07-08'),
	('4', '3', '10004', '2019-07-01', '2019-07-08'),
	('5', '3', '10000', '2019-07-01', '2019-07-08'),
	('8', '3', '10001', '2019-07-01', '2019-07-08'),
	('18', '1', '10006', '2019-07-01', '2019-07-08'),
	('6', '0', '10006', '2019-09-09', '2019-09-16'),
	('12', '1', '10005', '2019-09-09', '2019-09-16'),
	('8', '3', '10004', '2019-09-09', '2019-09-16'),
	('1', '2', '10003', '2019-09-09', '2019-09-16'),
	('19', '1', '10002', '2019-09-09', '2019-09-16'),
	('0', '0', '10001', '2019-09-09', '2019-09-19'),
	('13', '1', '10000', '2019-09-09', '2019-09-19')
;

