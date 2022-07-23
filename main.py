# Import tabulate library, function tabulate to display data in table format
from tabulate import tabulate

# Import random library, function randint to generate random int for user_id
from random import randint

# Establishing connection with MySQL 
import mysql.connector
from mysql.connector.dbapi import DATETIME
mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "*******", # Change password to your MySQL Workbench password
    database = "db_lms" # .SQL file name containing LMS database
)

print("MySQL database connection is successful")


# FUNCTION 1: Adding new user to database: db_lms, table: tb_user
def add_new_user():
    # For LMS user action: input new user information into the system
    user_id = randint(1,100)
    user_name = input("Enter user name:")
    date_of_birth = input("Enter date of birth (YYYY-MM-DD):")
    occupation = input("Enter occupation:")
    address = input("Enter address:")

    # Converting user inputs into SQL queries insert data into tb_user
    data = (user_id, user_name, date_of_birth, occupation, address)
    sql= "Insert into tb_user values(%s,%s,%s,%s,%s)"

    # Adding new user data into MySQL database: db_lms into tb_user table
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()

    # Letting user know that selected task has been executed
    print(".................................")
    print("New user successfully added to the database")

    #Back to main menu
    main_menu()

# FUNCTION 2: Adding new book to database: db_lms, table: tb_book
def add_new_book():
    # For LMS user action: input new book information into the system
    book_id = input ("Enter book id:")
    book_title = input("Enter book title:")
    category = input("Enter book category:")
    stock = input("Enter book stock:")

    # Converting book inputs into SQL queries insert data into tb_book
    data = (book_id, book_title, category, stock)
    sql = "Insert into tb_book values(%s,%s,%s,%s)"

    # Adding new book data into MySQL database: db_lms into tb_book table 
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()

    # Letting user know that selected task has been executed
    print(".................................")
    print("New book successfully added to the database")
    
    #Back to main menu
    main_menu()

# FUNCTION 3: Adding new borrower to database: db_lms, table: tb_borrower
def add_new_borrower():
    # For LMS user action: input new borrower information into the system
    user_id = input ("Enter borrower user id:")
    book_id = input ("Enter book id:")
    user_name = input("Enter user name:")
    book_title = input("Enter book title:")

    # Converting borrower inputs into SQL queries insert data into tb_book
    # Note: borrowed_date set as today's date as default, returned date = borrowed_date + 3 days
    data = (user_id, book_id, user_name, book_title)
    sql = "Insert into tb_borrower values(%s,%s,%s,%s,CURDATE(),DATE_ADD(CURDATE(), INTERVAL 3 DAY))"

    # Adding new borrower data into MySQL database: db_lms into tb_borrower table 
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()

    # Letting user know that selected task has been executed
    print(".................................")
    print("Borrower data successfully added to the database")

    # Run query current stock for books borrowed
    sql = "SELECT stock FROM tb_book where book_id = '{}'".format(book_id)
    c = mydb.cursor()
    c.execute(sql)   

    # Store current stock as a list and deducting stock by 1 everytime a book is borrowed
    curr_qty = c.fetchall()
    new_qty = curr_qty [0][0] - 1

    # Updating new stock into the database: db_lms, table: db_book for the borrowed book
    deduct_stock_sql = "UPDATE tb_book SET stock = {} where book_id = '{}'".format(new_qty, book_id)
    c = mydb.cursor()
    c.execute(deduct_stock_sql)
    mydb.commit()

    # Back to main menu
    main_menu()


# FUNCTION 4: Display user lists from database: db_lms, table: tb_user
def display_user():
    # Run query to display all columns from table: tb_user
    sql = "select * from tb_user"
    c = mydb.cursor()
    c.execute(sql)

    # Convert outputs from query to display tb_user as tabular format in terminals 
    myresult = c.fetchall()
    headers = ['user_id', 'user_name', 'date_of_birth', 'occupation', 'address']
    print(tabulate(myresult,headers))
    print("..................................")

    # Back to main menu
    main_menu()

# FUNCTION 5: Display book lists from database: db_lms, table: tb_book
def display_book():
    # Run query to display all columns from table: tb_book
    sql = "select * from tb_book"
    c = mydb.cursor()
    c.execute(sql)

    # Convert outputs from query to display tb_book as tabular format in terminals 
    myresult = c.fetchall()
    headers = ['book_id', 'book_title', 'category', 'stock']
    print(tabulate(myresult,headers))
    print("..................................")

    # Back to main menu
    main_menu()

# FUNCTION 6: Display borrower lists from database: db_lms, table: tb_borrow
def display_borrower():
    # Run query to display all columns from table: tb_borrower
    sql = "select * from tb_borrower"
    c = mydb.cursor()
    c.execute(sql) 

    # Convert outputs from query to display tb_borrower as tabular format in terminals 
    myresult = c.fetchall()
    headers = ['user_id', 'book_id', 'user_name', 'book_title', 'borrowed_date', 'returned_date']
    print(tabulate(myresult,headers))
    print("..................................")    

    # Back to main menu
    main_menu()


# FUNCTION 7: Search for a book from database: db_lms, table: tb_book
def search_book():
    # Prompt user to input Book title as SQL query criteria 
    search_title = input("Enter a book title:")

    # Run query to display all columns from tb_book where it match Book title input by user
    sql = "select * from tb_book where book_title = '{}'".format(search_title)
    c = mydb.cursor()
    c.execute(sql)   

    # Convert outputs from query to display tb_book as tabular format in terminals     
    myresult = c.fetchall()
    headers = ['book_id', 'book_title', 'category', 'stock']
    print(tabulate(myresult,headers))
    print("..................................")

    # Back to main menu
    main_menu()

# FUNCTION 8: Return a book lists from database: db_lms, table: tb_borrower
def return_book():
    # Prompt user to input book_id and user_id when user return a borrowed book
    book_id = input ("Enter book id:")
    user_id = input ("Enter user id:")

    # Run query current stock for books returned
    sql = "SELECT stock FROM tb_book where book_id = '{}'".format(book_id)
    c = mydb.cursor()
    c.execute(sql)   

    # Store current stock as a list and adding stock by 1 everytime a book is returned
    curr_qty = c.fetchall()
    add_qty = curr_qty[0][0] + 1

    # Updating new stock into the database: db_lms, table: db_book for the returned book
    add_stock_sql = "UPDATE tb_book SET stock = {} where book_id = '{}'".format(add_qty, book_id)
    c = mydb.cursor()
    c.execute(add_stock_sql)
    mydb.commit()

    # Remove borrower data from tb_borrower when a book has been returned
    remove_sql = "DELETE FROM tb_borrower WHERE user_id = {}".format(user_id)
    c = mydb.cursor()
    c.execute(remove_sql)
    mydb.commit() 

    # Letting user know that selected task has been executed
    print("""User id:{} has been removed from borrower list and 
    Returned book id: {} stock has been updated to book list.""".format(user_id,book_id))

    # Back to main menu
    main_menu() 


# FUNCTION 9: Exit LMS
def leave():
    # Letting user know that selected task has been executed
    print("""
    Thank you for using LMS. See you next time ~
    ------------------------------------------------------
    "Today a reader, tomorrow a leader" - Margaret Fuller
    """)

# MAIN MENU - Library management system 
def main_menu():
    # User interface layout
    print("""........... Welcome to Library Management System........... 
    1. Add New User
    2. Add New Book
    3. Borrow Book
    4. Display User List
    5. Display Book List
    6. Display Borrower List
    7. Search Book
    8. Return Book
    9. Exit
    """)

    # Prompting user to enter any task above 
    choice = input("Enter task no: ")
    print(".......................................")

    # After user enter task no, respective task functions will be executed
    if(choice=='1'):
        add_new_user()
    elif(choice=='2'):
        add_new_book()
    elif(choice=='3'):
        add_new_borrower()
    elif(choice=='4'):
        display_user()
    elif(choice=='5'):
        display_book()
    elif(choice=='6'):
        display_borrower()
    elif(choice=='7'):
        search_book()
    elif(choice=='8'):
        return_book()
    elif(choice=='9'):
        leave()
    # If user key in no outside of available inputs, main menu will be displayed
    else:
        main_menu()

# Displaying main menu when main.py file is executed on terminal
main_menu()

