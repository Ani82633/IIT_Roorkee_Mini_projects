# Library Management System - Python Mini Project

# Step 1: books are stored in a dictionary
library = {
    "Python Basics": {"author": "Test", "available": True, "issued_to": ""},
    "Data Science": {"author": "Test1", "available": False, "issued_to": "Rahul"}
}

# Step 5: usernames and passwords
credentials = {"admin": "admin123", "librarian": "lib123"}


def login():
    # user gets 3 chances to login
    for attempt in range(3):
        username = input("Username: ")
        password = input("Password: ")
        if username in credentials and credentials[username] == password:
            print("Login successful!\n")
            return True
        print("Wrong username or password. Attempts left:", 2 - attempt)
    return False


def display_books():
    if len(library) == 0:
        print("No books in the library.")
        return
    print("\nAll Books:")
    for title in library:
        book = library[title]
        if book["available"]:
            status = "Available"
        else:
            status = "Issued"
        print(title, "| Author:", book["author"], "| Status:", status)


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    if title in library:
        print("This book already exists.")
    else:
        library[title] = {"author": author, "available": True, "issued_to": ""}
        print("Book added successfully.")


def issue_book():
    title = input("Enter book title to issue: ")
    if title not in library:
        print("Book not found.")
    elif not library[title]["available"]:
        print("Sorry, this book is already issued.")
    else:
        name = input("Enter the name of the person: ")
        library[title]["available"] = False
        library[title]["issued_to"] = name
        print("Book issued to", name)


def return_book():
    title = input("Enter book title to return: ")
    if title not in library:
        print("Book not found.")
    elif library[title]["available"]:
        print("This book was not issued.")
    else:
        library[title]["available"] = True
        library[title]["issued_to"] = ""
        print("Book returned successfully.")


def view_issued_books():
    found = False
    print("\nIssued Books:")
    for title in library:
        if not library[title]["available"]:
            print(title, "- issued to", library[title]["issued_to"])
            found = True
    if not found:
        print("No books are issued right now.")


# Step 7: main menu
print("Welcome to the Library Management System")

if login():
    while True:
        print("\n1. View Books")
        print("2. Add a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. View Issued Books")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_issued_books()
        elif choice == "6":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice, please try again.")
else:
    print("Too many failed attempts. Exiting...")