use Library
/* Question 1 */
CREATE PROC question1
AS
BEGIN
	SELECT Branch.BranchName, Book.Title, Copies.Number_Of_Copies
	FROM book_copies Copies
	INNER JOIN books Book ON Book.BookId = Copies.BookId
	INNER JOIN library_branch Branch ON Branch.BranchId = Copies.BranchId
	WHERE Book.Title = 'The Lost Tribe' AND Branch.BranchName = 'Sharpstown'
END

/* Question 2 */
CREATE PROC question2
AS
BEGIN
	SELECT Branch.BranchName, Book.Title, Copies.Number_Of_Copies
	FROM book_copies Copies
	INNER JOIN books Book ON Book.BookId = Copies.BookId
	INNER JOIN library_branch Branch ON Branch.BranchId = Copies.BranchId
	WHERE Book.Title = 'The Lost Tribe'
END

/* Question 3 */
CREATE PROC question3
AS
BEGIN
	SELECT Borrower.Name
	FROM borrower
	LEFT JOIN book_loans Loan ON Loan.CardNo = borrower.CardNo
	WHERE Loan.CardNo IS NULL
END

/* Question 4 */
CREATE PROC question4
AS
BEGIN
	DECLARE @todaysDate varchar(50)
	SET @todaysDate = ( SELECT CONVERT (date, GETDATE()) );
	SELECT Book.Title, borrower.Name, borrower.Address
	FROM book_loans Loan
	INNER JOIN borrower Borrower ON Borrower.CardNo = Loan.CardNo
	INNER JOIN books Book ON Book.BookId = Loan.BookId
	INNER JOIN library_branch Branch ON Branch.BranchId = Loan.BranchId
	WHERE Branch.BranchName = 'Sharpstown' AND Loan.DateDue = @todaysDate
END

/* Question 5 */
CREATE PROC question5
AS
BEGIN
	SELECT Branch.BranchName, COUNT(*) LoanedBooks
	FROM book_loans Loan
	INNER JOIN library_branch Branch ON Branch.BranchId = Loan.BranchId
	GROUP BY Branch.BranchName
END

/* Question 6 */
CREATE PROC question6
AS
BEGIN
	SELECT Borrower.Name, Borrower.Address, COUNT(*) LoanedBooks
	FROM book_loans Loan
	INNER JOIN borrower Borrower ON Borrower.CardNo = Loan.CardNo
	INNER JOIN library_branch Branch ON Branch.BranchId = Loan.BranchId
	GROUP BY Borrower.Name, Borrower.Address
	HAVING COUNT(*) > 5
END

/* Question 7 */
CREATE PROC question7
AS
BEGIN
	SELECT Book.Title, SUM(Copy.Number_Of_Copies) AS Copies
	FROM books Book
	INNER JOIN book_copies Copy ON Copy.BookId = Book.BookId
	INNER JOIN book_authors Author ON Author.BookId = Copy.BookId
	INNER JOIN library_branch Branch ON Branch.BranchId = Copy.BranchId
	WHERE Author.AuthorName = 'Stephen King' AND Branch.BranchName = 'Central'
	GROUP BY Book.Title
END