from utils import books

def add_book():
    book_name = input("Enter the name of the book: ").strip().upper()

    if book_name in books:
        print("Book already exists")
    else:
        books[book_name] = {
            "available": True,
            "issued_to": None,
            "issue_date": None,
            "days": 0
        }
        print(f"Book '{book_name}' added successfully")