# Project 2: Library Management System
# Problem Statement:
# Create a command-line Library Management System where both Admin and Users can perform different operations such as managing and borrowing books.

# Functional Requirements:
# Admin:
# 1. Add a new book
# 2. Remove a book
# 3. View all books
# User:
# 4. Borrow a book
# 5. Return a book
# 6. View available books

# Mandatory Requirements:
# You must use:

# List → to store all books
# Dictionary → to store book details (id, title, author, availability)
# Set → to track borrowed book IDs
# Tuple → to store fixed categories (e.g., ("Fiction", "Non-Fiction", "Sci-Fi"))


# Programming Concepts:
# Use if-else for role-based menu (Admin/User)
# Use a while loop for continuous execution

# Use functions for each feature


# Exception Handling:
# Handle:

# Invalid input
# Book not found
# Duplicate book ID
# Borrowing unavailable book
# Returning a book not borrowed


# Note:

# Use only core Python (no external libraries, no GUI)
# Code should be modular and well-structured
# Proper use of all required concepts is mandatory

books = []
book_details={}
borrowed_book_id={}
categories=("Fiction", "Non-Fiction", "Sci-Fi")

def add_book():
    book_id = input("Enter Book ID : ")
    book_title = input("Enter Book Title : ")
    book_author = input("Enter Book Author : ")
    book_category = input("Enter Book Category : ")
    book_details = {"id":book_id , "title":book_title , "author":book_author , "category":book_category}
    books.append(book_details)
    print(f"the book has added successfully: {books}")
    print("------------------------------------------------------")


def remove_book():
    book_id = input("Enter Book ID : ")
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book removed successfully.")
            return
    else:
        print("Book not found.")
    print("------------------------------------------------------")

def view_all_books():
    if not books:
        print("No books found.")
        return
    for book in books:
        print(book)
    print("------------------------------------------------------")


def borrow_book():
    book_id = input("Enter Book ID : ")
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            list_borrowed_book_id = list(borrowed_book_id)
            list_borrowed_book_id.append(book_id)
            print("borrowed book id =",list_borrowed_book_id)
            print("Book borrowed successfully.")
            return
    else:
        print("Book not found.")
    print("------------------------------------------------------")

def return_book():
    book_id = input("Enter Book ID : ")
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book returned successfully.")
            return
    else:
        print("Book not found.")
    print("------------------------------------------------------")

def view_available_books():
    if not books:
        print("No books found.")
        return
    for book in books:
        print(book)
    print("------------------------------------------------------")

while True:
    print("1. Admin")
    print("2. User")
    choice = input("Enter your choice :")
    if choice == "1":
        print("1. Add book")
        print("2. Remove book")
        print("3. View all books")
        print("4. Exit")
        choice = input("Enter your choice :")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            view_all_books()
        elif choice == "4":
            break
        else :
            print("Invalid choice. Please try again.")
    
    elif choice == "2":
        print("1. Borrow book")
        print("2. Return book")
        print("3. View available books")
        print("4. Exit")
        choice = input("Enter your choice :")
        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            view_available_books()
        elif choice == "4":
            break
        else :
            print("Invalid choice. Please try again.")

    else:
        print("Invalid choice. Please try again.")
        break






    