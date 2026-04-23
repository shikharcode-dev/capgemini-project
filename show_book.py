from utils import books

def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("\nLibrary Books:\n")
        
        for book, data in books.items():
            if data["available"]:
                print(f"{book} -> Available")
            else:
                print(f"{book} -> Issued to {data['issued_to']}")