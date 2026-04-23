from utils import books
from datetime import date

def return_book():
    book_name = input("Enter book name to return: ").strip().upper()

    if book_name in books and not books[book_name]["available"]:
        today = date.today()
        issue_date = books[book_name]["issue_date"]
        allowed_days = books[book_name]["days"]

        days_passed = (today - issue_date).days

        fine = 0

        if days_passed > allowed_days:
            late_days = days_passed - allowed_days

            if late_days <= 7:
                fine = late_days * 10
            elif late_days <= 14:
                fine = late_days * 20
            else:
                fine = late_days * 60

        print(f"Days Passed: {days_passed}")
        print(f"Fine: ₹{fine}")

        books[book_name]["available"] = True
        books[book_name]["issued_to"] = None
        books[book_name]["issue_date"] = None
        books[book_name]["days"] = 0

        print(f"Book '{book_name}' returned successfully")
    else:
        print("Invalid return")