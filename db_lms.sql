# Create LMS database
CREATE DATABASE IF NOT EXISTS db_lms;

# Use LMS database 
USE db_lms;

# Create table for users 
CREATE TABLE IF NOT EXISTS tb_user (
	user_id INT NOT NULL,
	user_name VARCHAR(50) NOT NULL,
	date_of_birth DATE NOT NULL,
	occupation VARCHAR(50) NOT NULL,
	address VARCHAR(200) NOT NULL,
	PRIMARY KEY (user_id)
);

# Test table display
#DESCRIBE tb_user;

# Insert dummy data into users table 
#INSERT INTO tb_user (user_id, user_name, date_of_birth, occupation, address)
#VALUES ('1', 'jovita kurniawan', '1997-01-22', 'product manager', 'Jl Bulevard Raya No.15 Apartemen SunVille Unit 20-21'); 

# Test table data display
#SELECT * FROM tb_user;

# Create table for books 
CREATE TABLE IF NOT EXISTS tb_book (
	book_id INT NOT NULL,
	book_title VARCHAR(100) NOT NULL,
	category VARCHAR(50) NOT NULL,
	stock INT NOT NULL,
	PRIMARY KEY (book_id)
);

# Test table display
#DESCRIBE tb_book;

# Insert dummy data into books table
#INSERT INTO tb_book (book_id, book_title, category, stock)
#VALUES ('100', 'The Art of Thinking Clearly', 'Personal Growth', '10'); 


# Test table data display
#SELECT * FROM tb_book;

# Create table for borrowers
CREATE TABLE IF NOT EXISTS tb_borrower (
	user_id INT NOT NULL,
	book_id INT NOT NULL,
	user_name VARCHAR(50) NOT NULL,
	book_title VARCHAR(100) NOT NULL,
    borrowed_date DATE NOT NULL,
    returned_date DATE NOT NULL,
	PRIMARY KEY (user_id, book_id),
    FOREIGN KEY (book_id) REFERENCES tb_book(book_id),
	FOREIGN KEY (user_id) REFERENCES tb_user(user_id)
);

# Test table display
#DESCRIBE tb_borrower;

# Insert dummy data into books table
#INSERT INTO tb_borrower (user_id, book_id, user_name, book_title, borrowed_date, returned_date)
#VALUES ('1', '100', 'jovita kurniawan', 'The Art of Thinking Clearly', '2022-07-22', '2022-07-25'); 

# Test table data display
#SELECT * FROM tb_borrower;
