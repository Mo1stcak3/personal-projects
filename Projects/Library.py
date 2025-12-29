def space():
    print("\n")
    return

def books():
    books = {
        "1": "Atomic Habits by James Clear",
        "2": "The 7 Habits of Highly Effective People by Stephen R. Covey",
        "3": "The Power of Now by Eckhart Tolle",
        "4": "Mindset: The New Psychology of Success by Carol S. Dweck",
        "5": "The Subtle Art of Not Giving a F*ck by Mark Manson"
    }

    previews = {
        "1": "Atomic Habits explains how small daily changes compound into remarkable results. Clear focuses on habit loops, identity-based change, and practical systems.",
        "2": "Covey’s classic outlines seven timeless principles for effectiveness, from being proactive to sharpening the saw. It blends personal growth with leadership lessons.",
        "3": "The Power of Now emphasizes living fully in the present moment, letting go of past regrets and future anxieties to achieve peace and awareness.",
        "4": "Mindset explores fixed vs. growth mindsets, showing how beliefs about ability shape success in school, work, and relationships.",
        "5": "Mark Manson delivers a blunt, humorous take on values and priorities, encouraging readers to focus only on what truly matters."
    }

    kept_books = []

    while True:
        print("\nWelcome To The Library\n")
        print("Available Books:")
        for key, value in books.items():
            print(f"{key}. {value}")
        print("k. View Kept Books")
        print("q. Quit")
        

        choice = input("\nSelect a book number: ")

        if choice == "q":
            print("Exiting Library. Goodbye!")
            break
        elif choice == "k":
            if kept_books:
                print("Your kept books:")
                for book in kept_books:
                    print(f"- {book}")
            else:
                print("You have no kept books.")
        if choice in books:
            print(f"\nYou selected: {books[choice]}")
            while True:
                print("\nOptions:")
                print("a. Keep Book")
                print("b. Preview and Review")
                print("c. Return Book")
                print("d. Go Back Selection")

                option = input("Choose an option: ")

                if option == "a":
                    kept = books.pop(choice)
                    kept_books.append(kept)    
                    print(f"You kept {kept}. It is no longer available in the library.")
                    kb = input("Do you want to view your kept books? (y/n): ")
                    if kb.lower() == 'y':
                        print("Your kept books:")
                        for book in kept_books:
                            print(f"- {book}")
                        print("\n")
                    break  
                elif option == "b":
                    print(f"\nPreview of {books[choice]}:\n{previews[choice]}")
                elif option == "c":
                    returned = books.pop(choice)
                    print(f"You returned {returned}. It is no longer available in the library.")
                    break
                elif option == "d":
                    print("Going back to book selection...")
                    break
                else:
                    print("Invalid option. Try again.")
        else:
            print("Invalid book number. Try again.")

#Creation of Account
def coa():
    print("  CREATE YOUR ACCOUNT TO CONTIUE!  ")
    clog = input("Username: ")
    cpw = input("Password: ")
    space()
    return clog, cpw

#Account Library
def login_process(clog, pw):
    a = 0
    while a < 3:
        print("  LOGIN YOUR ACCOUNT  ")
        log = input("USERNAME: ")
        pw = input("PASSWORD: ")
        space()

        if log.lower() == clog.lower() and pw.lower() == cpw.lower():
            print("Success Log in")
            books()
            return True
        else:
            print("bulbul kaba?! hackerist yern?")
            a += 1

    print("HECKER KABA???")
    return False

clog, cpw = coa()
login_process(clog, cpw)
