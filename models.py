"""
models.py — Data model classes and custom exceptions for the Library Management System.
Defines Book, Student data classes and the custom exception hierarchy.
"""

import sqlite3


# ==============================================================================
# Custom Exception Hierarchy
# ==============================================================================

class LibraryError(Exception):
    """Base exception for all Library-related errors."""
    pass


class BookNotFoundError(LibraryError):
    """Raised when a book ID does not exist in the database."""

    def __init__(self, book_id: int):
        self.book_id = book_id
        super().__init__(f"No book found with ID: {book_id}")


class StudentNotFoundError(LibraryError):
    """Raised when a student ID does not exist in the database."""

    def __init__(self, student_id: int):
        self.student_id = student_id
        super().__init__(f"No student found with ID: {student_id}")


class IssueNotFoundError(LibraryError):
    """Raised when an issue_id does not exist in the database."""

    def __init__(self, issue_id: int):
        self.issue_id = issue_id
        super().__init__(f"No issue record found with ID: {issue_id}")


class BookUnavailableError(LibraryError):
    """Raised when a book has no available copies for issuance."""

    def __init__(self, book_id: int):
        self.book_id = book_id
        super().__init__(
            f"Book ID {book_id} has no available copies at the moment."
        )


class BookNotIssuedError(LibraryError):
    """Raised when attempting to return a book not currently issued to a student."""

    def __init__(self, book_id: int, student_id: int):
        self.book_id = book_id
        self.student_id = student_id
        super().__init__(
            f"Book ID {book_id} is not currently issued to Student ID {student_id}."
        )


class AlreadyIssuedError(LibraryError):
    """Raised when a student tries to borrow the same book they already have."""

    def __init__(self, book_id: int, student_id: int):
        self.book_id = book_id
        self.student_id = student_id
        super().__init__(
            f"Student ID {student_id} already has Book ID {book_id} issued."
        )


class FineNotDueError(LibraryError):
    """Raised when attempting to pay a fine that is not in DUE status."""

    def __init__(self, issue_id: int):
        self.issue_id = issue_id
        super().__init__(
            f"Issue ID {issue_id} has no outstanding fine to pay "
            f"(fine may already be paid or was never incurred)."
        )


class InvalidOperationError(LibraryError):
    """Raised for invalid menu choices or improper input values."""

    def __init__(self, message: str = "Invalid operation or input."):
        super().__init__(message)


class DuplicateEmailError(LibraryError):
    """Raised when a student email already exists."""

    def __init__(self, email: str):
        self.email = email
        super().__init__(f"A student with email '{email}' is already registered.")


# ==============================================================================
# Book Model
# ==============================================================================

class Book:
    """
    Represents a book in the library catalog.

    Attributes:
        book_id (int): Auto-incremented primary key from DB (None if unsaved).
        title (str): Title of the book.
        author (str): Author of the book.
        total_copies (int): Total copies owned by the library.
        available_copies (int): Copies currently available for lending.
    """

    def __init__(
        self,
        title: str,
        author: str,
        total_copies: int,
        available_copies: int,
        book_id: int = None,
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Book":
        """Factory constructor: creates a Book from a sqlite3.Row object."""
        return cls(
            book_id=row["book_id"],
            title=row["title"],
            author=row["author"],
            total_copies=row["total_copies"],
            available_copies=row["available_copies"],
        )

    def to_dict(self) -> dict:
        """Returns book state as a dictionary."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
        }

    def __str__(self) -> str:
        return (
            f"Book(id={self.book_id}, title='{self.title}', "
            f"author='{self.author}', "
            f"copies={self.available_copies}/{self.total_copies})"
        )


# ==============================================================================
# Student Model
# ==============================================================================

class Student:
    """
    Represents a library member (student).

    Attributes:
        student_id (int): Auto-incremented primary key from DB (None if unsaved).
        name (str): Full name of the student.
        email (str): Unique email address.
    """

    def __init__(self, name: str, email: str, student_id: int = None):
        self.student_id = student_id
        self.name = name
        self.email = email

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Student":
        """Factory constructor: creates a Student from a sqlite3.Row object."""
        return cls(
            student_id=row["student_id"],
            name=row["name"],
            email=row["email"],
        )

    def to_dict(self) -> dict:
        """Returns student info as a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
        }

    def __str__(self) -> str:
        return (
            f"Student(id={self.student_id}, name='{self.name}', "
            f"email='{self.email}')"
        )
