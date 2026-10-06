"""
library.py — Core Library service class for the Library Management System.
Encapsulates all business logic: book management, student registration,
issue/return transactions, fine payment tracking, overdue fee computation,
and statistics.
"""

import sqlite3
from datetime import date, timedelta, datetime
from typing import List, Optional

from database import DatabaseManager
from models import (
    Book,
    Student,
    BookNotFoundError,
    StudentNotFoundError,
    IssueNotFoundError,
    BookUnavailableError,
    BookNotIssuedError,
    AlreadyIssuedError,
    FineNotDueError,
    DuplicateEmailError,
    InvalidOperationError,
)


# Lending configuration constants
DEFAULT_LENDING_DAYS: int = 7           # Borrow window in days
FINE_RATE_PER_DAY: float = 5.0         # Overdue fine per day (in currency units)
TOP_ISSUED_BOOKS_LIMIT: int = 3        # How many top-issued books to report


class Library:
    """
    Provides all library operations including catalog management,
    member management, book lending, fine tracking, and reporting.

    Attributes:
        db (DatabaseManager): Underlying database manager instance.
    """

    def __init__(self, db_path: str = "library.db"):
        self.db = DatabaseManager(db_path)

    # ==========================================================================
    # Book Management
    # ==========================================================================

    def add_book(self, title: str, author: str, copies: int = 1) -> Book:
        """
        Adds a new book entry to the catalog.

        Args:
            title (str): Book title.
            author (str): Book author name.
            copies (int): Number of copies to add (must be >= 1).

        Returns:
            Book: The newly created Book object with its assigned ID.

        Raises:
            InvalidOperationError: If copies < 1 or title/author are empty.
        """
        title = title.strip()
        author = author.strip()

        if not title:
            raise InvalidOperationError("Book title cannot be empty.")
        if not author:
            raise InvalidOperationError("Book author cannot be empty.")
        if copies < 1:
            raise InvalidOperationError(
                f"Number of copies must be at least 1, got {copies}."
            )

        with self.db.get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO books (title, author, total_copies, available_copies)
                VALUES (?, ?, ?, ?)
                """,
                (title, author, copies, copies),
            )
            conn.commit()
            book_id = cursor.lastrowid

        return Book(
            book_id=book_id,
            title=title,
            author=author,
            total_copies=copies,
            available_copies=copies,
        )

    def display_available_books(self) -> List[Book]:
        """
        Retrieves all books that have at least one available copy.

        Returns:
            List[Book]: List of Book objects with available copies.
        """
        with self.db.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM books
                WHERE available_copies > 0
                ORDER BY title ASC
                """
            ).fetchall()

        return [Book.from_row(row) for row in rows]

    def list_all_books(self) -> List[Book]:
        """
        Retrieves all books in the catalog regardless of availability.

        Returns:
            List[Book]: All books in the catalog.
        """
        with self.db.get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM books ORDER BY title ASC"
            ).fetchall()

        return [Book.from_row(row) for row in rows]

    def search_books(self, keyword: str, field: str = "all") -> List[Book]:
        """
        Searches books by title, author, or both fields.

        Args:
            keyword (str): The search keyword (case-insensitive partial match).
            field (str): Search field — 'title', 'author', or 'all'.

        Returns:
            List[Book]: Matching Book objects.

        Raises:
            InvalidOperationError: If field is not a valid option.
        """
        keyword = keyword.strip()
        if not keyword:
            raise InvalidOperationError("Search keyword cannot be empty.")

        pattern = f"%{keyword}%"

        field_options = {"title", "author", "all"}
        if field not in field_options:
            raise InvalidOperationError(
                f"Invalid search field '{field}'. Choose from: {field_options}"
            )

        with self.db.get_connection() as conn:
            if field == "title":
                rows = conn.execute(
                    "SELECT * FROM books WHERE title LIKE ? ORDER BY title ASC",
                    (pattern,),
                ).fetchall()
            elif field == "author":
                rows = conn.execute(
                    "SELECT * FROM books WHERE author LIKE ? ORDER BY author ASC",
                    (pattern,),
                ).fetchall()
            else:  # all
                rows = conn.execute(
                    """
                    SELECT * FROM books
                    WHERE title LIKE ? OR author LIKE ?
                    ORDER BY title ASC
                    """,
                    (pattern, pattern),
                ).fetchall()

        return [Book.from_row(row) for row in rows]

    def get_book_by_id(self, book_id: int) -> Book:
        """
        Fetches a single book by its ID.

        Args:
            book_id (int): The book's primary key.

        Returns:
            Book: The matching Book object.

        Raises:
            BookNotFoundError: If no book with that ID exists.
        """
        with self.db.get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM books WHERE book_id = ?", (book_id,)
            ).fetchone()

        if row is None:
            raise BookNotFoundError(book_id)

        return Book.from_row(row)

    # ==========================================================================
    # Student / Member Management
    # ==========================================================================

    def register_student(self, name: str, email: str) -> Student:
        """
        Registers a new library member (student).

        Args:
            name (str): Full name of the student.
            email (str): Unique email address.

        Returns:
            Student: The newly registered Student object with its assigned ID.

        Raises:
            InvalidOperationError: If name or email is empty / invalid.
            DuplicateEmailError: If a student with that email already exists.
        """
        name = name.strip()
        email = email.strip().lower()

        if not name:
            raise InvalidOperationError("Student name cannot be empty.")
        if not email or "@" not in email:
            raise InvalidOperationError("Please enter a valid email address.")

        with self.db.get_connection() as conn:
            existing = conn.execute(
                "SELECT student_id FROM students WHERE email = ?", (email,)
            ).fetchone()
            if existing:
                raise DuplicateEmailError(email)

            cursor = conn.execute(
                "INSERT INTO students (name, email) VALUES (?, ?)",
                (name, email),
            )
            conn.commit()
            student_id = cursor.lastrowid

        return Student(student_id=student_id, name=name, email=email)

    def list_students(self) -> List[Student]:
        """
        Returns all registered students.

        Returns:
            List[Student]: All student records.
        """
        with self.db.get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM students ORDER BY name ASC"
            ).fetchall()

        return [Student.from_row(row) for row in rows]

    def get_student_by_id(self, student_id: int) -> Student:
        """
        Fetches a single student by their ID.

        Args:
            student_id (int): The student's primary key.

        Returns:
            Student: The matching Student object.

        Raises:
            StudentNotFoundError: If no student with that ID exists.
        """
        with self.db.get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM students WHERE student_id = ?", (student_id,)
            ).fetchone()

        if row is None:
            raise StudentNotFoundError(student_id)

        return Student.from_row(row)

    # ==========================================================================
    # Book Issues — Issue & Return
    # ==========================================================================

    def issue_book(
        self,
        book_id: int,
        student_id: int,
        duration_days: int = DEFAULT_LENDING_DAYS,
    ) -> dict:
        """
        Issues a book to a student.

        Decrements available_copies by 1 and creates an ISSUED record in issues.

        Args:
            book_id (int): The book to issue.
            student_id (int): The student borrowing the book.
            duration_days (int): Lending window in days.

        Returns:
            dict: Issue summary with issue_date, due_date, and IDs.

        Raises:
            BookNotFoundError: If book_id is invalid.
            StudentNotFoundError: If student_id is invalid.
            BookUnavailableError: If no copies are available.
            AlreadyIssuedError: If the student already has this book issued.
        """
        book = self.get_book_by_id(book_id)
        student = self.get_student_by_id(student_id)

        if book.available_copies <= 0:
            raise BookUnavailableError(book_id)

        with self.db.get_connection() as conn:
            active = conn.execute(
                """
                SELECT issue_id FROM issues
                WHERE book_id = ? AND student_id = ? AND status = 'ISSUED'
                """,
                (book_id, student_id),
            ).fetchone()
            if active:
                raise AlreadyIssuedError(book_id, student_id)

            today = date.today()
            due = today + timedelta(days=duration_days)

            cursor = conn.execute(
                """
                INSERT INTO issues
                    (book_id, student_id, issue_date, due_date, fine_status, status)
                VALUES (?, ?, ?, ?, 'NONE', 'ISSUED')
                """,
                (book_id, student_id, today.isoformat(), due.isoformat()),
            )

            conn.execute(
                """
                UPDATE books
                SET available_copies = available_copies - 1
                WHERE book_id = ?
                """,
                (book_id,),
            )

            conn.commit()
            issue_id = cursor.lastrowid

        return {
            "issue_id": issue_id,
            "book_id": book_id,
            "book_title": book.title,
            "student_id": student_id,
            "student_name": student.name,
            "issue_date": today.isoformat(),
            "due_date": due.isoformat(),
        }

    def return_book(self, book_id: int, student_id: int) -> dict:
        """
        Processes a book return.

        Calculates any overdue fine, updates the issue record with fine_status:
        - 'DUE'  if fine_amount > 0 (user still owes money)
        - 'NONE' if returned on time

        Args:
            book_id (int): The book being returned.
            student_id (int): The student returning the book.

        Returns:
            dict: Return summary including fine_amount, fine_status, dates.

        Raises:
            BookNotFoundError: If book_id is invalid.
            StudentNotFoundError: If student_id is invalid.
            BookNotIssuedError: If no active issue exists for this pair.
        """
        book = self.get_book_by_id(book_id)
        student = self.get_student_by_id(student_id)

        with self.db.get_connection() as conn:
            txn = conn.execute(
                """
                SELECT * FROM issues
                WHERE book_id = ? AND student_id = ? AND status = 'ISSUED'
                ORDER BY issue_date DESC
                LIMIT 1
                """,
                (book_id, student_id),
            ).fetchone()

            if txn is None:
                raise BookNotIssuedError(book_id, student_id)

            today = date.today()
            fine = self.calculate_overdue_fee(txn["due_date"], today.isoformat())
            fine_status = "DUE" if fine > 0 else "NONE"

            conn.execute(
                """
                UPDATE issues
                SET return_date = ?,
                    fine_amount = ?,
                    fine_status = ?,
                    status = 'RETURNED'
                WHERE issue_id = ?
                """,
                (today.isoformat(), fine, fine_status, txn["issue_id"]),
            )

            conn.execute(
                """
                UPDATE books
                SET available_copies = available_copies + 1
                WHERE book_id = ?
                """,
                (book_id,),
            )

            conn.commit()

        return {
            "issue_id": txn["issue_id"],
            "book_id": book_id,
            "book_title": book.title,
            "student_id": student_id,
            "student_name": student.name,
            "issue_date": txn["issue_date"],
            "due_date": txn["due_date"],
            "return_date": today.isoformat(),
            "fine_amount": fine,
            "fine_status": fine_status,
        }

    # ==========================================================================
    # Overdue Fee Calculation
    # ==========================================================================

    def calculate_overdue_fee(
        self,
        due_date_str: str,
        return_date_str: str,
        rate_per_day: float = FINE_RATE_PER_DAY,
    ) -> float:
        """
        Calculates overdue fine based on days past due.

        Args:
            due_date_str (str): Due date in ISO format (YYYY-MM-DD).
            return_date_str (str): Return/today date in ISO format.
            rate_per_day (float): Fine amount per overdue day.

        Returns:
            float: Total fine amount (0.0 if on time or early).
        """
        due = date.fromisoformat(due_date_str)
        returned = date.fromisoformat(return_date_str)
        days_late = max(0, (returned - due).days)
        return round(days_late * rate_per_day, 2)

    # ==========================================================================
    # Fine Payment System
    # ==========================================================================

    def pay_fine(self, issue_id: int) -> dict:
        """
        Marks an outstanding fine as PAID.

        Args:
            issue_id (int): The issue record whose fine should be marked paid.

        Returns:
            dict: Payment summary with student, book, amount, and new status.

        Raises:
            IssueNotFoundError: If no issue with that ID exists.
            FineNotDueError: If the issue has no outstanding fine (status != 'DUE').
        """
        with self.db.get_connection() as conn:
            row = conn.execute(
                """
                SELECT i.*, b.title AS book_title, s.name AS student_name
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                JOIN students s ON i.student_id = s.student_id
                WHERE i.issue_id = ?
                """,
                (issue_id,),
            ).fetchone()

            if row is None:
                raise IssueNotFoundError(issue_id)

            if row["fine_status"] != "DUE":
                raise FineNotDueError(issue_id)

            conn.execute(
                "UPDATE issues SET fine_status = 'PAID' WHERE issue_id = ?",
                (issue_id,),
            )
            conn.commit()

        return {
            "issue_id": issue_id,
            "book_id": row["book_id"],
            "book_title": row["book_title"],
            "student_id": row["student_id"],
            "student_name": row["student_name"],
            "fine_amount": row["fine_amount"],
            "fine_status": "PAID",
        }

    def list_due_fines(self) -> List[dict]:
        """
        Returns all issue records with outstanding (DUE) fines.

        Returns:
            List[dict]: Issues where fine_status = 'DUE', with book/student info.
        """
        with self.db.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT
                    i.issue_id,
                    b.book_id,
                    b.title AS book_title,
                    s.student_id,
                    s.name AS student_name,
                    i.issue_date,
                    i.due_date,
                    i.return_date,
                    i.fine_amount,
                    i.fine_status
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                JOIN students s ON i.student_id = s.student_id
                WHERE i.fine_status = 'DUE'
                ORDER BY i.fine_amount DESC
                """
            ).fetchall()

        return [dict(row) for row in rows]

    def list_due_fines_by_student(self, student_id: int) -> List[dict]:
        """
        Returns all outstanding (DUE) fines for a specific student.

        Args:
            student_id (int): The student's primary key.

        Returns:
            List[dict]: DUE fines for that student.

        Raises:
            StudentNotFoundError: If the student_id is invalid.
        """
        # Validate student exists
        self.get_student_by_id(student_id)

        with self.db.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT
                    i.issue_id,
                    b.book_id,
                    b.title AS book_title,
                    s.student_id,
                    s.name AS student_name,
                    i.issue_date,
                    i.due_date,
                    i.return_date,
                    i.fine_amount,
                    i.fine_status
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                JOIN students s ON i.student_id = s.student_id
                WHERE i.fine_status = 'DUE' AND i.student_id = ?
                ORDER BY i.fine_amount DESC
                """,
                (student_id,),
            ).fetchall()

        return [dict(row) for row in rows]

    def list_paid_fines(self) -> List[dict]:
        """
        Returns all issue records with collected (PAID) fines representing income.

        Returns:
            List[dict]: Issues where fine_status = 'PAID', with book/student info.
        """
        with self.db.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT
                    i.issue_id,
                    b.book_id,
                    b.title AS book_title,
                    s.student_id,
                    s.name AS student_name,
                    i.issue_date,
                    i.due_date,
                    i.return_date,
                    i.fine_amount,
                    i.fine_status
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                JOIN students s ON i.student_id = s.student_id
                WHERE i.fine_status = 'PAID'
                ORDER BY i.return_date DESC
                """
            ).fetchall()

        return [dict(row) for row in rows]

    def list_paid_fines_by_student(self, student_id: int) -> List[dict]:
        """
        Returns all paid fines (income) collected from a specific student.

        Args:
            student_id (int): The student's primary key.

        Returns:
            List[dict]: PAID fines for that student.

        Raises:
            StudentNotFoundError: If the student_id is invalid.
        """
        self.get_student_by_id(student_id)

        with self.db.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT
                    i.issue_id,
                    b.book_id,
                    b.title AS book_title,
                    s.student_id,
                    s.name AS student_name,
                    i.issue_date,
                    i.due_date,
                    i.return_date,
                    i.fine_amount,
                    i.fine_status
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                JOIN students s ON i.student_id = s.student_id
                WHERE i.fine_status = 'PAID' AND i.student_id = ?
                ORDER BY i.return_date DESC
                """,
                (student_id,),
            ).fetchall()

        return [dict(row) for row in rows]

    # ==========================================================================
    # Issue Listings
    # ==========================================================================

    def list_active_issues(self) -> List[dict]:
        """
        Returns all currently active (ISSUED) issues with book/student details.

        Returns:
            List[dict]: Each dict has issue_id, book/student details, dates.
        """
        with self.db.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT
                    i.issue_id,
                    b.book_id,
                    b.title AS book_title,
                    s.student_id,
                    s.name AS student_name,
                    i.issue_date,
                    i.due_date
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                JOIN students s ON i.student_id = s.student_id
                WHERE i.status = 'ISSUED'
                ORDER BY i.due_date ASC
                """
            ).fetchall()

        return [dict(row) for row in rows]

    def list_all_issues(self) -> List[dict]:
        """
        Returns all issue records (both ISSUED and RETURNED) with full details.

        Returns:
            List[dict]: All issue records sorted by issue_date descending.
        """
        with self.db.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT
                    i.issue_id,
                    b.book_id,
                    b.title AS book_title,
                    s.student_id,
                    s.name AS student_name,
                    i.issue_date,
                    i.due_date,
                    i.return_date,
                    i.fine_amount,
                    i.fine_status,
                    i.status
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                JOIN students s ON i.student_id = s.student_id
                ORDER BY i.issue_date DESC
                """
            ).fetchall()

        return [dict(row) for row in rows]

    # ==========================================================================
    # Statistics & Reporting
    # ==========================================================================

    def get_statistics(self) -> dict:
        """
        Generates a statistical summary of the library's current state.

        Returns:
            dict: Summary stats including counts, fine totals, and top-issued books.
        """
        with self.db.get_connection() as conn:
            total_books = conn.execute(
                "SELECT COUNT(*) as cnt FROM books"
            ).fetchone()["cnt"]

            available_count = conn.execute(
                "SELECT SUM(available_copies) as cnt FROM books"
            ).fetchone()["cnt"] or 0

            total_copies = conn.execute(
                "SELECT SUM(total_copies) as cnt FROM books"
            ).fetchone()["cnt"] or 0

            issued_count = conn.execute(
                "SELECT COUNT(*) as cnt FROM issues WHERE status = 'ISSUED'"
            ).fetchone()["cnt"]

            total_fines_paid = conn.execute(
                """
                SELECT COALESCE(SUM(fine_amount), 0.0) as total
                FROM issues
                WHERE fine_status = 'PAID'
                """
            ).fetchone()["total"]

            total_fines_due = conn.execute(
                """
                SELECT COALESCE(SUM(fine_amount), 0.0) as total
                FROM issues
                WHERE fine_status = 'DUE'
                """
            ).fetchone()["total"]

            # Top issued books
            top_books_rows = conn.execute(
                f"""
                SELECT
                    b.book_id,
                    b.title,
                    b.author,
                    COUNT(i.issue_id) AS times_issued
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                GROUP BY i.book_id
                ORDER BY times_issued DESC
                LIMIT {TOP_ISSUED_BOOKS_LIMIT}
                """
            ).fetchall()

            top_books = [dict(row) for row in top_books_rows]

            total_issues = conn.execute(
                "SELECT COUNT(*) as cnt FROM issues"
            ).fetchone()["cnt"]

        return {
            "total_unique_books": total_books,
            "total_copies": total_copies,
            "available_copies": available_count,
            "currently_issued": issued_count,
            "total_issues": total_issues,
            "total_fines_paid": total_fines_paid,
            "total_fines_due": total_fines_due,
            "top_issued_books": top_books,
        }
