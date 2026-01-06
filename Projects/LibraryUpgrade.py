# Library Project

# space function
def space():
    print("\n")
    return


users = {}

# BOOKs FUNCTION
books = {
    "1": {
        "title": "Atomic Habits",
        "author": "James Clear",
        "preview": "Atomic Habits explains how small daily changes compound into remarkable results. Clear focuses on habit loops, identity-based change, and practical systems."
    },
    "2": {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "preview": "Covey’s classic outlines seven timeless principles for effectiveness, from being proactive to sharpening the saw. It blends personal growth with leadership lessons."
    },
    "3": {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "preview": "The Power of Now emphasizes living fully in the present moment, letting go of past regrets and future anxieties to achieve peace and awareness."
    },
    "4": {
        "title": "Mindset: The New Psychology of Success",
        "author": "Carol S. Dweck",
        "preview": "Mindset explores fixed vs. growth mindsets, showing how beliefs about ability shape success in school, work, and relationships."
    },
    "5": {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "preview": "Mark Manson delivers a blunt, humorous take on values and priorities, encouraging readers to focus only on what truly matters."
    },
}

# ADMIN MODE FUNCTION
def edmeyn():
    edmin = {
        "1": "Add Book",
        "2": "Remove Book",
        "3": "Edit Review",
        "4": "View All Books And Options",
        "5": "Exit Admin Mode"
    }
    return edmin


# ADMIN PAAAWEEER!!
def edm_pow():
    admin_pwd = input("Enter admin password: ")
    space()
    if admin_pwd == "admin67":
        admin_menu()
    else:
        bck = input("type anything to return to log-in menu..\n")
        if bck != "":
            return

#Admin Menu/Control
def admin_menu():
    print("Admin Control".center(20, "-"))
    space()
    while True:
        for key, value in sorted(edmeyn().items()):
            print(f"{key}. {value}")
            space()

        admin_choice = input("Select an option: ")

        if admin_choice == "1":  # add books
            
            book_id = input("Enter Book ID: ")
            books[book_id] = {
                "title": input("Enter new book title: "),
                "author": input("Enter new book author: "),
                "preview": input("Enter book preview: ")
            }
            print(f"Book '{books[book_id]['title']}' added to the library.")
            

        elif admin_choice == "2": #remove books
            print("Current Books in Library: ")
            for key, value in sorted(books.items()):
                print(f"{key}. {value['title']} by {value['author']}")
                space()

            rem_id = input("Enter book ID to remove book: ")

            if rem_id in books:
                removed_book = books.pop(rem_id)
                space()
                print(f"Book '{removed_book['title']}' by {removed_book['author']} removed from the library.")
                space()
            elif rem_id != "":
                return
            else:
                print("Book ID not found.")
                space()
                    
        elif admin_choice == "3":  # edit books
            edit_id = input("Enter book ID to edit book:")

            if edit_id in books:
                new_title = input("Enter new title: ")
                new_author = input("Enter new author: ")
                new_preview = input("Enter new preview: ")

                books[edit_id] = {
                    "title": new_title,
                    "author": new_author,
                    "preview": new_preview
                }
                print(f"Book '{books[edit_id]['title']}' updated.")
            else:
                print("Book ID not found.")

        elif admin_choice == "4":  # view all books
            print("\nAll Books in Library: \n")
            for key, value in sorted(books.items()):
                print(f"{key}. {value['title']} by {value['author']}\n{value['preview']}")
                space()

        elif admin_choice == "5":
            print("Exiting Admin Mode.")
            log_men()
            space()
            break

        else:
            print("Invalid option. Try again.")
            space()


def Library(): # The library
    kept_books = []

    while True:
        print("\nWelcome To The Library\n")
        print("Available Books:")
        for key, value in sorted(books.items()):
            print(f"{key}. {value['title']} by {value['author']}")

        space()
        print("a. View Kept Books")
        print("b. Admin Mode")
        print("c. Quit")

        choice = input("\nSelect an action or a book: ")

        if choice == "c":
            print("Exiting Library. Goodbye!")
            break

        elif choice == "b":
            edm_pow()

        elif choice == "a":
            if kept_books:
                print("Your kept books:")
                space()
                for index, (book_id, book_title) in enumerate(kept_books, start=1):
                    print(f"{index}. {book_title}")

                print("r. Return a book")
                space()
                km_choice = input("Choose a number to view, or 'r' to return: ")

                if km_choice == "r":
                    try:
                        return_index = int(input("Enter the number of the book to return: "))
                        if 1 <= return_index <= len(kept_books):
                            book_id, book_title = kept_books.pop(return_index - 1)
                            books[book_id] = book_title
                            print(f"{book_title} RETURNED TO LIBRARY")
                        else:
                            print("Invalid book number.")
                            space()
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                elif km_choice.isdigit():
                    num = int(km_choice)
                    if 1 <= num <= len(kept_books):
                        book_id, book_title = kept_books[num - 1]
                        print(f"\nPreview of {book_title}:\n{books[book_id]['preview']}")
                        space()
                    else:
                        print("Invalid book number.")
                        space()

                else:
                    print("Invalid option. Returning to main menu.")
                    space()
            else:
                print("You have no kept books.")
                space()

        elif choice in books:
            print(f"\nYou selected: {books[choice]['title']} by {books[choice]['author']}")
            space()

            while True:
                print("\nOptions:")
                print("a. Keep Book")
                print("b. Preview and Review")
                print("c. Return Book")
                print("d. Go Back Selection")
                space()

                option = input("Choose an option: ")

                if option == "a":
                    kept = books.pop(choice)
                    kept_books.append((choice, kept))
                    print(f"You kept {kept}. It is no longer available in the library.")
                    space()
                    break

                elif option == "b":
                    space()
                    print(f"\nPreview of {books[choice]['title']}:\n{books[choice]['preview']}")
                    space()

                elif option == "c":
                    for index, (book_id, book_name) in enumerate(kept_books):
                        if book_id == choice:
                            books[book_id] = book_name
                            kept_books.pop(index)
                            
                            print(f"{book_name} RETURNED TO LIBRARY")
                            space()
                            break
                    else:
                        print("You have not kept this book.")
                        space()
                    break

                elif option == "d":
                    print("Going back to book selection...")
                    space()
                    break

                else:
                    print("Invalid option. Try again.")
                    space()
        else:
            print("Invalid book number. Try again.")
            space()


# Creation of Account
def coa():
    while True:
        print("  CREATE YOUR ACCOUNT TO CONTINUE!  ")
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        confirmpassword = input("CONFIRM PASSWORD: ")
        space()

        if confirmpassword != password:
            print("Passwords do not match. Try again.")
            continue

        if username in users:
            print(f"Username '{username}' already exists. Try again.")
            space()
            login_process()

        users[username] = {"password": password, "borrowed": []}
        print(f"User '{username}' created successfully.")
        break


# Account Library
def login_process():
    a = 0
    while a < 3:
        print("  LOGIN YOUR ACCOUNT  ")
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        space()

        if username in users and users[username]["password"] == password:
            print("Success Log in")
            Library()
            return True
        else:
            print("Incorrect Username or Password. Try Again.")
            a += 1
            input("Too many failed attempts. Press enter to continue")
            log_men()


# Login Menu
def log_men():
    while True:
        print("  WELCOME TO THE LIBRARY SYSTEM  ")
        space()
        print("1. Create Account")
        print("2. Login")
        print("3. Admin Mode")
        space()

        choice = input("Select an option: ")

        if choice == "1":
            coa()
        elif choice == "2":
            if login_process():
                break
        elif choice == "3":
            edm_pow()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
            space()


log_men()
