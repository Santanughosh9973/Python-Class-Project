import json
from datetime import date, timedelta
from pathlib import Path


# Custom exception for library errors.This is our custom exception.
class LibraryError(Exception):
    pass


# Book class
class Book:
    def __init__(self, book_id, title, author, category, year, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.year = str(year)
        self.status = status

    def to_dict(self):
        return self.__dict__.copy()


# Student class
class Student:
    def __init__(self, student_id, name, email="", phone=""):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return self.__dict__.copy()


# Main Library class
class Library:

    # Default Settings
    DEFAULT_SETTINGS = {
        "library_name": "LibraryMS",
        "institution_name": "Brainware University",
        "borrow_days": 14,
        "daily_overdue_charge": 5.0,
        "admin_name": "Santanu Ghosh",
        "admin_email": "santanu@libraryms.edu",
        "currency_symbol": "₹"
    }

    # Maximum borrowing period
    BORROW_DAYS = 14

    # Fine per overdue day
    DAILY_OVERDUE_CHARGE = 5.0

    def __init__(self, data_dir="data"):

        # Create data folder if it does not exist
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

        # Data file locations
        self.books_file = self.data_dir / "books.json"
        self.students_file = self.data_dir / "students.json"
        self.transactions_file = self.data_dir / "transactions.json"
        self.settings_file = self.data_dir / "settings.json"

        # Load existing data
        self.books = self._load(self.books_file, [])
        self.students = self._load(self.students_file, [])
        self.transactions = self._load(self.transactions_file, [])
        self.settings = self._load(self.settings_file, self.DEFAULT_SETTINGS.copy())

        # Sync runtime constants with settings
        self.BORROW_DAYS = int(self.settings.get("borrow_days", 14))
        self.DAILY_OVERDUE_CHARGE = float(self.settings.get("daily_overdue_charge", 5.0))

    # ------------------------------------------------
    # FILE HANDLING
    # ------------------------------------------------

    def _load(self, path, default):

        try:
            # Check whether file exists
            if not path.exists():

                # Create the file with default data
                self._save(path, default)

                return default.copy()

            # Open JSON file
            with open(path, "r", encoding="utf-8") as file:

                # Convert JSON into Python data
                return json.load(file)

        except (json.JSONDecodeError, OSError):

            # Return empty/default data if file has a problem
            return default.copy()

    def _save(self, path, data):

        # Open file for writing
        with open(path, "w", encoding="utf-8") as file:

            # Save Python data as JSON
            json.dump(data, file, indent=4)

    def _save_all(self):

        # Save all library records
        self._save(self.books_file, self.books)
        self._save(self.students_file, self.students)
        self._save(self.transactions_file, self.transactions)
        self._save(self.settings_file, self.settings)

    # ------------------------------------------------
    # SETTINGS
    # ------------------------------------------------

    def get_settings(self):
        return self.settings.copy()

    def update_settings(self, new_settings):

        try:
            borrow_days = int(new_settings.get("borrow_days", self.BORROW_DAYS))
            if borrow_days < 1 or borrow_days > 90:
                raise LibraryError("Borrowing period must be between 1 and 90 days.")
        except (ValueError, TypeError):
            raise LibraryError("Borrowing period must be a valid number.")

        try:
            overdue_charge = float(new_settings.get("daily_overdue_charge", self.DAILY_OVERDUE_CHARGE))
            if overdue_charge < 0:
                raise LibraryError("Daily overdue charge cannot be negative.")
        except (ValueError, TypeError):
            raise LibraryError("Daily overdue charge must be a valid number.")

        self.settings["library_name"] = str(new_settings.get("library_name", "LibraryMS")).strip() or "LibraryMS"
        self.settings["institution_name"] = str(new_settings.get("institution_name", "")).strip()
        self.settings["borrow_days"] = borrow_days
        self.settings["daily_overdue_charge"] = overdue_charge
        self.settings["admin_name"] = str(new_settings.get("admin_name", "Santanu Ghosh")).strip()
        self.settings["admin_email"] = str(new_settings.get("admin_email", "")).strip()
        self.settings["currency_symbol"] = str(new_settings.get("currency_symbol", "₹")).strip() or "₹"

        self.BORROW_DAYS = borrow_days
        self.DAILY_OVERDUE_CHARGE = overdue_charge

        self._save(self.settings_file, self.settings)
        return self.settings.copy()

    # ------------------------------------------------
    # BOOK OPERATIONS
    # ------------------------------------------------

    def add_book(self, book_id, title, author, category, year):

        # Check required fields
        if not all([book_id, title, author, category, year]):
            raise LibraryError("All book fields are required.")

        # Check duplicate book ID
        if any(
            book["book_id"].lower() == book_id.lower()
            for book in self.books
        ):
            raise LibraryError("Book ID already exists.")

        # Check year
        if not year.isdigit() or len(year) != 4:
            raise LibraryError("Year must be a valid 4-digit number.")

        # Create Book object
        book = Book(
            book_id,
            title,
            author,
            category,
            year
        )

        # Convert object into dictionary
        self.books.append(book.to_dict())

        # Save data
        self._save_all()

    def delete_book(self, book_id):

        # Find the book
        book = self._find_book(book_id)

        # Do not delete an issued book
        if book["status"] == "Issued":
            raise LibraryError(
                "Issued books cannot be deleted."
            )

        # Delete book
        self.books.remove(book)

        # Save changes
        self._save_all()

    def search_books(self, query):

        # Convert search text to lowercase
        query = query.lower()

        # Search multiple fields
        return [
            book
            for book in self.books
            if query in book["book_id"].lower()
            or query in book["title"].lower()
            or query in book["author"].lower()
            or query in book["category"].lower()
        ]

    def _find_book(self, book_id):

        # Search book by ID
        for book in self.books:

            if book["book_id"].lower() == book_id.lower():
                return book

        # If not found
        raise LibraryError("Invalid book ID.")

    # ------------------------------------------------
    # STUDENT OPERATIONS
    # ------------------------------------------------

    def add_student(
        self,
        student_id,
        name,
        email="",
        phone=""
    ):

        # Student ID and name are required
        if not student_id or not name:
            raise LibraryError(
                "Student ID and name are required."
            )

        # Check duplicate student ID
        if any(
            student["student_id"].lower() == student_id.lower()
            for student in self.students
        ):
            raise LibraryError(
                "Student ID already exists."
            )

        # Create Student object
        student = Student(
            student_id,
            name,
            email,
            phone
        )

        # Store student
        self.students.append(student.to_dict())

        # Save data
        self._save_all()

    def _find_student(self, student_id):

        # Search student by ID
        for student in self.students:

            if student["student_id"].lower() == student_id.lower():
                return student

        raise LibraryError("Invalid student ID.")

    # ------------------------------------------------
    # ISSUE BOOK
    # ------------------------------------------------

    def issue_book(
        self,
        book_id,
        student_id,
        days
    ):

        # Find book
        book = self._find_book(book_id)

        # Check student
        self._find_student(student_id)

        # Check whether book is already issued
        if book["status"] == "Issued":
            raise LibraryError(
                "This book is already issued."
            )

        # Convert days to integer
        try:
            days = int(days)

        except ValueError:
            raise LibraryError(
                "Borrowing days must be a number."
            )

        # Validate borrowing days
        if days < 1 or days > 30:
            raise LibraryError(
                "Borrowing days must be between 1 and 30."
            )

        # Today's date
        issue_date = date.today()

        # Calculate due date
        due_date = issue_date + timedelta(days=days)

        # Change book status
        book["status"] = "Issued"

        # Create transaction
        transaction = {

            "transaction_id": f"T{len(self.transactions) + 1:03d}",

            "book_id": book["book_id"],

            "title": book["title"],

            "student_id": student_id,

            "issue_date": issue_date.isoformat(),

            "due_date": due_date.isoformat(),

            "return_date": "",

            "charge": 0,

            "overdue_charge": 0,

            "status": "Issued"
        }

        # Add transaction
        self.transactions.append(transaction)

        # Save everything
        self._save_all()

    # ------------------------------------------------
    # RETURN BOOK
    # ------------------------------------------------

    def return_book(self, book_id):

        # Find book
        book = self._find_book(book_id)

        # Check book status
        if book["status"] != "Issued":
            raise LibraryError(
                "This book is not currently issued."
            )

        transaction = None

        # Find latest issue transaction
        for item in reversed(self.transactions):

            if (
                item["book_id"].lower() == book_id.lower()
                and item["status"] == "Issued"
            ):

                transaction = item
                break

        # Transaction not found
        if transaction is None:
            raise LibraryError(
                "Issue transaction not found."
            )

        # Today's date
        today = date.today()

        # Convert due date from text to date
        due_date = date.fromisoformat(
            transaction["due_date"]
        )

        # Calculate overdue days
        overdue_days = max(
            (today - due_date).days,
            0
        )

        # Calculate fine
        charge = (
            overdue_days *
            self.DAILY_OVERDUE_CHARGE
        )

        # Update transaction
        transaction["return_date"] = today.isoformat()

        transaction["charge"] = charge
        transaction["overdue_charge"] = charge

        transaction["status"] = "Returned"

        # Change book status
        book["status"] = "Available"

        # Save changes
        self._save_all()

        # Return fine information
        return {
            "charge": charge,
            "overdue_days": overdue_days
        }

    # ------------------------------------------------
    # BOOK STATUS
    # ------------------------------------------------

    def get_available_books(self):

        return [
            book
            for book in self.books
            if book["status"] == "Available"
        ]

    def get_issued_books(self):

        return [
            book
            for book in self.books
            if book["status"] == "Issued"
        ]

    # ------------------------------------------------
    # STATISTICS
    # ------------------------------------------------

    def statistics(self):

        # Get all transactions
        issued_transactions = [
            transaction
            for transaction in self.transactions
            if transaction["status"]
            in ("Issued", "Returned")
        ]

        # Count book issues
        issue_counts = {}

        for transaction in issued_transactions:

            title = transaction["title"]

            if title not in issue_counts:
                issue_counts[title] = 0

            issue_counts[title] += 1

        # Sort most issued books
        most_issued = []
        for title, count in sorted(
            issue_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )[:5]:
            author = "Unknown"
            for b in self.books:
                if b.get("title", "").strip().lower() == title.strip().lower():
                    author = b.get("author", "Unknown")
                    break
            most_issued.append({
                "title": title,
                "author": author,
                "issue_count": count
            })

        # Calculate total charges
        total_charges = sum(
            float(transaction.get("charge") or transaction.get("overdue_charge") or 0)
            for transaction in self.transactions
        )

        # Return statistics
        return {

            "total_books": len(self.books),

            "available_books": len(
                self.get_available_books()
            ),

            "issued_books": len(
                self.get_issued_books()
            ),

            "total_students": len(self.students),

            "total_transactions": len(
                self.transactions
            ),

            "total_charges": total_charges,

            "most_issued": most_issued
        }