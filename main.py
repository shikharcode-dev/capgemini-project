from add_book import add_book
from show_book import show_books
from issue_book import issue_book
from return_book import return_book

def library():
    while True:
        print("========= Library Menu =========")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_book()
            elif choice == 2:
                show_books()
            elif choice == 3:
                issue_book()
            elif choice == 4:
                return_book()
            elif choice == 5:
                print("Thank you!")
                break
            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

library()