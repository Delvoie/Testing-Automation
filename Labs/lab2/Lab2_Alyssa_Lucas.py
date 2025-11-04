# Date: Oct 9, 2025
# Name: "Library Management Software"
# Programmer: Alyssa and Lucas
# Description: file with operations to add a read and search book in a library

import csv
import os

MIN_YEAR = 400
MAX_YEAR = 2025
CSV_FILE = "library.csv"


# Function to validate user input
def valid_input(title, author, year):
    if not title or len(title) > 100:
        raise ValueError("Title cannot be empty and must be between 1 and 100 characters")
    if not author or len(author) > 100:
        raise ValueError("Author cannot be empty and must be between 1 and 100 characters")
    if not year:
        raise ValueError("Year cannot be empty")
    if not year.isdigit():
        raise ValueError("Year must be a number")
    if int(year) < MIN_YEAR or int(year) > MAX_YEAR:
        raise ValueError("Year must be between 400 and 2025")
    else:
        # if valid
        print("Book added successfully!")
    return title, author, year


# Book class with constraints
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Initialize book list
books = []


# CRUD Operations

# 1 load all books
def load_books_from_csv():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(Book(row['title'], row['author'], row['year']))


# 3 adding a book to csv
def add_book():
    print("Add a Book")
    try:
        input_title = input("Enter title: ")
        input_author = input("Enter author: ")
        input_year = input("Enter year: ")

        title, author, year = valid_input(input_title, input_author, input_year)
        new_book = Book(title, author, year)
        books.append(new_book)
        with open(CSV_FILE, 'w', newline='') as file:
            #set fieldnames
            fieldnames = ['title', 'author', 'year']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in books:
                writer.writerow({'title': book.title, 'author': book.author, 'year': book.year})
    except ValueError as error:
        print(f"Book Failed to be crated: {error}")
    print("-" * 70)


# read all
def list_all_books():
    print("List all books")
    if len(books) == 0:
        print("No books in the library.")
    else:
        for book in books:
            print(f"{book.title} {book.author} {book.year}")
    print("-" * 70)


# search
def search_book():
    print("Search a Book")
    try:
        search_input = input("Enter title, author or year: ")
        # search from a list of books as a placeholder for csv
        for book in books:
            if book.title == search_input or book.author == search_input or book.year == search_input:
                print(f"{book.title} {book.author} {book.year}")
    except ValueError:
        print("Book not found")
    print("-" * 70)


# Start a program asking for user input
def main_function():
    load_books_from_csv()
    choice = ""

    while choice != "4":
        print("Library Management\n")
        # Prompt user for menu
        print("1. Add a Book")
        print("2. Read all books")
        print("3. Search a book")
        print("4 Exit")
        choice = input("Please select an option (1-4): ")

        # If 1 add book function
        if choice == "1":
            add_book()
        # If 2 add read all books functions
        elif choice == "2":
            list_all_books()
        # If 3 search for a book function
        elif choice == '3':
            search_book()
        # If 4 exit program
        elif choice == '4':
            print("Exiting Library....")
        # Restart loop
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Start the program
if __name__ == "__main__":
    main_function()
