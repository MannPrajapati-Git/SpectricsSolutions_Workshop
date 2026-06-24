books = []

borrowed_book_ids = set()

CATEGORIES = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "History", "Technology")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def display_separator(char="=", length=60):
  
    print(char * length)


def display_header(title):
  
    display_separator()
    print(f"  {title.center(56)}")
    display_separator()


def find_book_by_id(book_id):
   
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def is_duplicate_id(book_id):
    
    return find_book_by_id(book_id) is not None


def display_book(book):
   
    status = "Available ✓" if book["availability"] else "Borrowed  ✗"
    print(f"  ID       : {book['id']}")
    print(f"  Title    : {book['title']}")
    print(f"  Author   : {book['author']}")
    print(f"  Category : {book['category']}")
    print(f"  Status   : {status}")
    print("-" * 40)


def display_categories():
   
    print("\n  Available Categories:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"    {index}. {category}")


def get_valid_integer(prompt):
   
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("  [!] Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("  [!] Invalid input. Please enter a numeric value.")


def get_non_empty_string(prompt):
  
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] Input cannot be empty. Please try again.")


def add_book():
    display_header("ADD NEW BOOK")

    book_id = get_valid_integer("  Enter Book ID        : ")

    if is_duplicate_id(book_id):
        print(f"\n  [!] Error: Book with ID '{book_id}' already exists.")
        print("  [!] Please use a unique Book ID.")
        return

    
    title = get_non_empty_string("  Enter Book Title     : ")
    author = get_non_empty_string("  Enter Author Name   : ")

    
    display_categories()
    while True:
        try:
            cat_choice = int(input(f"  Select Category (1-{len(CATEGORIES)}): ").strip())
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1] 
                break
            else:
                print(f"  [!] Please enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a numeric value.")

   
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "availability": True       
    }

    books.append(new_book)         

    print(f"\n  [✓] Book '{title}' (ID: {book_id}) added successfully!")


def remove_book():
  
    display_header("REMOVE A BOOK")

    if not books:
        print("  [!] No books available in the library.")
        return

    book_id = get_valid_integer("  Enter Book ID to remove: ")

    
    book = find_book_by_id(book_id)
    if book is None:
        print(f"\n  [!] Error: No book found with ID '{book_id}'.")
        return

    
    if not book["availability"]:
        print(f"\n  [!] Error: Book '{book['title']}' is currently borrowed.")
        print("  [!] Cannot remove a book that is checked out.")
        return

   
    print(f"\n  Book to remove:")
    display_book(book)
    confirm = input("  Are you sure you want to remove this book? (yes/no): ").strip().lower()

    if confirm == "yes":
        books.remove(book)       
        print(f"\n  [✓] Book '{book['title']}' (ID: {book_id}) removed successfully!")
    else:
        print("\n  [i] Removal cancelled.")


def view_all_books():

    display_header("ALL BOOKS IN LIBRARY")

    if not books:
        print("  [i] No books found in the library.")
        return

    print(f"  Total Books: {len(books)}")
    print(f"  Available  : {sum(1 for b in books if b['availability'])}")
    print(f"  Borrowed   : {len(borrowed_book_ids)}")
    display_separator("-")

    for book in books:             
        display_book(book)

    print(f"  Total: {len(books)} book(s) found.")

def borrow_book():
  
    display_header("BORROW A BOOK")

    available = [b for b in books if b["availability"]]
    if not available:
        print("  [i] No books are currently available for borrowing.")
        return

    book_id = get_valid_integer("  Enter Book ID to borrow: ")

    
    book = find_book_by_id(book_id)
    if book is None:
        print(f"\n  [!] Error: No book found with ID '{book_id}'.")
        return

    if not book["availability"]:
        print(f"\n  [!] Error: Book '{book['title']}' is currently not available.")
        print("  [!] It has already been borrowed by someone else.")
        return

    
    book["availability"] = False       
    borrowed_book_ids.add(book_id)     

    print(f"\n  [✓] You have successfully borrowed '{book['title']}'!")
    print(f"  [i] Please return it as soon as you're done.")


def return_book():
  
    display_header("RETURN A BOOK")

    if not borrowed_book_ids:
        print("  [i] No books are currently borrowed.")
        return

    book_id = get_valid_integer("  Enter Book ID to return: ")

    book = find_book_by_id(book_id)
    if book is None:
        print(f"\n  [!] Error: No book found with ID '{book_id}'.")
        return

    if book_id not in borrowed_book_ids:   
        print(f"\n  [!] Error: Book '{book['title']}' was not borrowed.")
        print("  [!] You can only return books that have been borrowed.")
        return

    book["availability"] = True            
    borrowed_book_ids.discard(book_id)    

    print(f"\n  [✓] Book '{book['title']}' returned successfully!")
    print("  [✓] Thank you for returning the book.")


def view_available_books():
    display_header("AVAILABLE BOOKS")

    available_books = [book for book in books if book["availability"]]

    if not available_books:
        print("  [i] No books are currently available.")
        print("  [i] All books may have been borrowed.")
        return

    print(f"  Available Books: {len(available_books)}")
    display_separator("-")

    for book in available_books:
        display_book(book)

    print(f"  Total: {len(available_books)} book(s) available.")


def admin_login():
    display_header("ADMIN LOGIN")
    username = input("  Username: ").strip()
    password = input("  Password: ").strip()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\n  [✓] Admin login successful! Welcome, Admin.")
        return True
    else:
        print("\n  [!] Invalid credentials. Access denied.")
        return False


def admin_menu():
   
    if not admin_login():
        return

    while True:
        display_header("ADMIN MENU")
        print("  1. Add a New Book")
        print("  2. Remove a Book")
        print("  3. View All Books")
        print("  4. Logout")
        display_separator("-")

        try:
            choice = int(input("  Enter your choice (1-4): ").strip())
        except ValueError:
            print("\n  [!] Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            add_book()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            view_all_books()
        elif choice == 4:
            print("\n  [i] Admin logged out successfully. Goodbye!")
            break
        else:
            print("\n  [!] Invalid choice. Please select between 1 and 4.")

        input("\n  Press Enter to continue...")


def user_menu():
    display_header("USER MENU")

    while True:
        display_header("USER MENU")
        print("  1. Borrow a Book")
        print("  2. Return a Book")
        print("  3. View Available Books")
        print("  4. Go Back")
        display_separator("-")

        try:
            choice = int(input("  Enter your choice (1-4): ").strip())
        except ValueError:
            print("\n  [!] Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            borrow_book()
        elif choice == 2:
            return_book()
        elif choice == 3:
            view_available_books()
        elif choice == 4:
            print("\n  [i] Returning to Main Menu...")
            break
        else:
            print("\n  [!] Invalid choice. Please select between 1 and 4.")

        input("\n  Press Enter to continue...")


def load_sample_data():

    sample_books = [
        {"id": 101, "title": "The Great Gatsby",       "author": "F. Scott Fitzgerald", "category": "Fiction",     "availability": True},
        {"id": 102, "title": "A Brief History of Time","author": "Stephen Hawking",     "category": "Sci-Fi",      "availability": True},
        {"id": 103, "title": "Sapiens",                "author": "Yuval Noah Harari",   "category": "History",     "availability": True},
        {"id": 104, "title": "Steve Jobs",             "author": "Walter Isaacson",     "category": "Biography",   "availability": True},
        {"id": 105, "title": "Clean Code",             "author": "Robert C. Martin",    "category": "Technology",  "availability": True},
    ]
    for book in sample_books:
        books.append(book)          



def main():
    load_sample_data()

    print("\n")
    display_separator("*")
    print("*" + "  LIBRARY MANAGEMENT SYSTEM  ".center(58) + "*")
    print("*" + "  Welcome! Please select your role.  ".center(58) + "*")
    display_separator("*")

    while True:                        
        display_header("MAIN MENU")
        print("  1. Admin Portal")
        print("  2. User Portal")
        print("  3. Exit")
        display_separator("-")

        try:
            role_choice = int(input("  Enter your choice (1-3): ").strip())
        except ValueError:
            print("\n  [!] Invalid input. Please enter 1, 2, or 3.")
            input("  Press Enter to continue...")
            continue
        if role_choice == 1:
            admin_menu()              
        elif role_choice == 2:
            user_menu()              
        elif role_choice == 3:
            display_separator()
            print("  Thank you for using the Library Management System!")
            print("  Goodbye! 👋")
            display_separator()
            break
        else:
            print("\n  [!] Invalid choice. Please enter 1, 2, or 3.")
            input("  Press Enter to continue...")

if __name__ == "__main__":
    main()