from utils import books
#from datetime import date. this is for temp and real time use
from datetime import date, timedelta

def issue_book():
    book_name = input("Enter book name to issue: ").strip().upper()

    if book_name in books and books[book_name]["available"]:
        student = input("Enter student name: ").strip()
        days = int(input("Enter number of days: "))

        books[book_name]["available"] = False
        books[book_name]["issued_to"] = student
        #books[book_name]["issue_date"] = date.today()  this will use the real time and in real we cant wait for 10 days so,
        
        books[book_name]["issue_date"] = date.today() - timedelta(days=10) # here it is used as "Pretend book was issued 10 days ago"
        
        books[book_name]["days"] = days

        print(f"Book '{book_name}' issued to {student} for {days} days")
    else:
        print("Book not available")