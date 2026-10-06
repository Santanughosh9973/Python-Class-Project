"""
test_library.py — Unit tests for the Library Management System.
Tests business logic, custom exceptions, DB interactions,
overdue fee calculation, fine payment tracking, and statistics.
"""

import os
import unittest
import tempfile
from datetime import date, timedelta

from library import Library
from models import (
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


class TestLibrarySetup(unittest.TestCase):
    """Base test class that creates a fresh isolated database for each test."""

    def setUp(self):
        """Create a temporary database file for isolation."""
        self.db_fd, self.db_path = tempfile.mkstemp(suffix=".db")
        self.library = Library(db_path=self.db_path)

    def tearDown(self):
        """Remove the temporary database after each test."""
        os.close(self.db_fd)
        os.unlink(self.db_path)


# ==============================================================================
# Book Management Tests
# ==============================================================================

class TestBookManagement(TestLibrarySetup):

    def test_add_book_success(self):
        """Adding a valid book returns a Book with the correct attributes."""
        book = self.library.add_book("Clean Code", "Robert Martin", 3)
        self.assertIsNotNone(book.book_id)
        self.assertEqual(book.title, "Clean Code")
        self.assertEqual(book.author, "Robert Martin")
        self.assertEqual(book.total_copies, 3)
        self.assertEqual(book.available_copies, 3)

    def test_add_book_default_single_copy(self):
        """Adding a book without specifying copies defaults to 1."""
        book = self.library.add_book("Dune", "Frank Herbert")
        self.assertEqual(book.total_copies, 1)
        self.assertEqual(book.available_copies, 1)

    def test_add_book_empty_title_raises(self):
        """Adding a book with empty title raises InvalidOperationError."""
        with self.assertRaises(InvalidOperationError):
            self.library.add_book("", "Some Author", 1)

    def test_add_book_empty_author_raises(self):
        """Adding a book with empty author raises InvalidOperationError."""
        with self.assertRaises(InvalidOperationError):
            self.library.add_book("Some Book", "", 1)

    def test_add_book_zero_copies_raises(self):
        """Adding a book with zero copies raises InvalidOperationError."""
        with self.assertRaises(InvalidOperationError):
            self.library.add_book("Bad Book", "No Author", 0)

    def test_add_book_negative_copies_raises(self):
        """Adding a book with negative copies raises InvalidOperationError."""
        with self.assertRaises(InvalidOperationError):
            self.library.add_book("Bad Book", "No Author", -2)

    def test_display_available_books_returns_only_available(self):
        """display_available_books returns only books with available copies."""
        b1 = self.library.add_book("Book A", "Author A", 2)
        b2 = self.library.add_book("Book B", "Author B", 1)
        s = self.library.register_student("Alice", "alice@example.com")
        self.library.issue_book(b2.book_id, s.student_id)

        available = self.library.display_available_books()
        available_ids = [b.book_id for b in available]
        self.assertIn(b1.book_id, available_ids)
        self.assertNotIn(b2.book_id, available_ids)

    def test_search_books_by_title(self):
        """search_books finds matching books by title keyword."""
        self.library.add_book("The Pragmatic Programmer", "Andy Hunt", 1)
        self.library.add_book("Clean Code", "Robert Martin", 1)
        results = self.library.search_books("pragmatic", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Pragmatic Programmer")

    def test_search_books_by_author(self):
        """search_books finds matching books by author keyword."""
        self.library.add_book("Clean Code", "Robert Martin", 1)
        self.library.add_book("The Clean Coder", "Robert Martin", 1)
        results = self.library.search_books("Martin", "author")
        self.assertEqual(len(results), 2)

    def test_search_books_all_fields(self):
        """search_books with 'all' matches title and author."""
        self.library.add_book("Dune", "Frank Herbert", 1)
        self.library.add_book("Foundation", "Isaac Asimov", 1)
        results = self.library.search_books("frank", "all")
        self.assertEqual(len(results), 1)

    def test_search_books_empty_keyword_raises(self):
        """search_books with empty keyword raises InvalidOperationError."""
        with self.assertRaises(InvalidOperationError):
            self.library.search_books("  ")

    def test_get_book_by_invalid_id_raises(self):
        """Getting a book with invalid ID raises BookNotFoundError."""
        with self.assertRaises(BookNotFoundError):
            self.library.get_book_by_id(99999)


# ==============================================================================
# Student Management Tests
# ==============================================================================

class TestStudentManagement(TestLibrarySetup):

    def test_register_student_success(self):
        """Registering a valid student returns a Student with correct attributes."""
        student = self.library.register_student("Bob Smith", "bob@example.com")
        self.assertIsNotNone(student.student_id)
        self.assertEqual(student.name, "Bob Smith")
        self.assertEqual(student.email, "bob@example.com")

    def test_register_student_email_normalized_lowercase(self):
        """Student email is stored in lowercase."""
        student = self.library.register_student("Carol", "CAROL@Example.COM")
        self.assertEqual(student.email, "carol@example.com")

    def test_register_student_duplicate_email_raises(self):
        """Registering a student with a duplicate email raises DuplicateEmailError."""
        self.library.register_student("Alice", "alice@example.com")
        with self.assertRaises(DuplicateEmailError):
            self.library.register_student("Alicia", "alice@example.com")

    def test_register_student_empty_name_raises(self):
        """Registering a student with empty name raises InvalidOperationError."""
        with self.assertRaises(InvalidOperationError):
            self.library.register_student("", "test@example.com")

    def test_register_student_invalid_email_raises(self):
        """Registering a student with an email lacking '@' raises InvalidOperationError."""
        with self.assertRaises(InvalidOperationError):
            self.library.register_student("Dave", "notanemail")

    def test_list_students_returns_all(self):
        """list_students returns all registered students."""
        self.library.register_student("Alice", "a@ex.com")
        self.library.register_student("Bob", "b@ex.com")
        students = self.library.list_students()
        self.assertEqual(len(students), 2)

    def test_get_student_invalid_id_raises(self):
        """Getting a student with invalid ID raises StudentNotFoundError."""
        with self.assertRaises(StudentNotFoundError):
            self.library.get_student_by_id(99999)


# ==============================================================================
# Issue & Return Tests
# ==============================================================================

class TestIssues(TestLibrarySetup):

    def setUp(self):
        super().setUp()
        self.book = self.library.add_book("Python 101", "Guido", 2)
        self.student = self.library.register_student("Eve", "eve@example.com")

    def test_issue_book_decrements_available_copies(self):
        """Issuing a book reduces available_copies by 1."""
        self.library.issue_book(self.book.book_id, self.student.student_id)
        updated = self.library.get_book_by_id(self.book.book_id)
        self.assertEqual(updated.available_copies, self.book.available_copies - 1)

    def test_issue_book_returns_correct_summary(self):
        """Issue result dict contains correct book, student, and date info."""
        result = self.library.issue_book(self.book.book_id, self.student.student_id)
        self.assertEqual(result["book_id"], self.book.book_id)
        self.assertEqual(result["student_id"], self.student.student_id)
        self.assertIn("issue_id", result)
        expected_due = (date.today() + timedelta(days=7)).isoformat()
        self.assertEqual(result["due_date"], expected_due)

    def test_issue_book_invalid_book_raises(self):
        """Issuing a non-existent book raises BookNotFoundError."""
        with self.assertRaises(BookNotFoundError):
            self.library.issue_book(99999, self.student.student_id)

    def test_issue_book_invalid_student_raises(self):
        """Issuing to a non-existent student raises StudentNotFoundError."""
        with self.assertRaises(StudentNotFoundError):
            self.library.issue_book(self.book.book_id, 99999)

    def test_issue_book_unavailable_raises(self):
        """Issuing a book with no copies raises BookUnavailableError."""
        s2 = self.library.register_student("Frank", "frank@example.com")
        self.library.issue_book(self.book.book_id, self.student.student_id)
        self.library.issue_book(self.book.book_id, s2.student_id)
        s3 = self.library.register_student("Grace", "grace@example.com")
        with self.assertRaises(BookUnavailableError):
            self.library.issue_book(self.book.book_id, s3.student_id)

    def test_issue_same_book_twice_raises(self):
        """A student borrowing the same book twice raises AlreadyIssuedError."""
        self.library.issue_book(self.book.book_id, self.student.student_id)
        with self.assertRaises(AlreadyIssuedError):
            self.library.issue_book(self.book.book_id, self.student.student_id)

    def test_return_book_increments_available_copies(self):
        """Returning a book restores available_copies by 1."""
        self.library.issue_book(self.book.book_id, self.student.student_id)
        self.library.return_book(self.book.book_id, self.student.student_id)
        updated = self.library.get_book_by_id(self.book.book_id)
        self.assertEqual(updated.available_copies, self.book.available_copies)

    def test_return_book_not_issued_raises(self):
        """Returning a book not on loan raises BookNotIssuedError."""
        with self.assertRaises(BookNotIssuedError):
            self.library.return_book(self.book.book_id, self.student.student_id)

    def test_return_book_after_return_raises(self):
        """Returning the same book twice (without reissuing) raises BookNotIssuedError."""
        self.library.issue_book(self.book.book_id, self.student.student_id)
        self.library.return_book(self.book.book_id, self.student.student_id)
        with self.assertRaises(BookNotIssuedError):
            self.library.return_book(self.book.book_id, self.student.student_id)

    def test_return_on_time_sets_fine_status_none(self):
        """Returning on time sets fine_status to NONE and fine_amount to 0."""
        self.library.issue_book(self.book.book_id, self.student.student_id)
        result = self.library.return_book(self.book.book_id, self.student.student_id)
        self.assertEqual(result["fine_amount"], 0.0)
        self.assertEqual(result["fine_status"], "NONE")

    def test_return_late_sets_fine_status_due(self):
        """Returning late sets fine_status to DUE with a positive fine_amount."""
        # Issue with -1 day window so due date is yesterday → overdue on return today
        self.library.issue_book(self.book.book_id, self.student.student_id, duration_days=-1)
        result = self.library.return_book(self.book.book_id, self.student.student_id)
        self.assertGreater(result["fine_amount"], 0.0)
        self.assertEqual(result["fine_status"], "DUE")


# ==============================================================================
# Overdue Fee Calculation Tests
# ==============================================================================

class TestOverdueFee(TestLibrarySetup):

    def test_no_fine_when_on_time(self):
        """No fine when returned on the due date."""
        due = date.today()
        fine = self.library.calculate_overdue_fee(due.isoformat(), due.isoformat())
        self.assertEqual(fine, 0.0)

    def test_no_fine_when_returned_early(self):
        """No fine when returned before the due date."""
        due = (date.today() + timedelta(days=3)).isoformat()
        returned = date.today().isoformat()
        fine = self.library.calculate_overdue_fee(due, returned)
        self.assertEqual(fine, 0.0)

    def test_fine_for_one_day_late(self):
        """Fine is exactly 1 day rate when returned 1 day late."""
        due = (date.today() - timedelta(days=1)).isoformat()
        returned = date.today().isoformat()
        fine = self.library.calculate_overdue_fee(due, returned)
        self.assertEqual(fine, 5.0)

    def test_fine_for_multiple_days_late(self):
        """Fine scales correctly with multiple overdue days."""
        due = (date.today() - timedelta(days=5)).isoformat()
        returned = date.today().isoformat()
        fine = self.library.calculate_overdue_fee(due, returned)
        self.assertEqual(fine, 25.0)

    def test_custom_rate_fine(self):
        """Fine is computed using the custom rate when provided."""
        due = (date.today() - timedelta(days=3)).isoformat()
        returned = date.today().isoformat()
        fine = self.library.calculate_overdue_fee(due, returned, rate_per_day=10.0)
        self.assertEqual(fine, 30.0)


# ==============================================================================
# Fine Payment System Tests
# ==============================================================================

class TestFinePayment(TestLibrarySetup):

    def setUp(self):
        super().setUp()
        self.book = self.library.add_book("Overdue Test Book", "Author X", 1)
        self.student = self.library.register_student("Fine Payer", "payer@example.com")
        # Issue with -1 day window so due date is yesterday → overdue on return today
        self.library.issue_book(self.book.book_id, self.student.student_id, duration_days=-1)
        self.result = self.library.return_book(self.book.book_id, self.student.student_id)
        self.issue_id = self.result["issue_id"]

    def test_overdue_return_appears_in_due_fines(self):
        """A late return appears in list_due_fines() with fine_status DUE."""
        dues = self.library.list_due_fines()
        due_ids = [d["issue_id"] for d in dues]
        self.assertIn(self.issue_id, due_ids)

    def test_due_fines_by_student_returns_correct_fines(self):
        """list_due_fines_by_student returns only that student's dues."""
        dues = self.library.list_due_fines_by_student(self.student.student_id)
        self.assertEqual(len(dues), 1)
        self.assertEqual(dues[0]["student_id"], self.student.student_id)
        self.assertEqual(dues[0]["fine_status"], "DUE")

    def test_due_fines_by_student_invalid_id_raises(self):
        """list_due_fines_by_student with invalid student_id raises StudentNotFoundError."""
        with self.assertRaises(StudentNotFoundError):
            self.library.list_due_fines_by_student(99999)

    def test_pay_fine_marks_paid(self):
        """pay_fine() changes fine_status from DUE to PAID."""
        result = self.library.pay_fine(self.issue_id)
        self.assertEqual(result["fine_status"], "PAID")
        self.assertEqual(result["issue_id"], self.issue_id)

    def test_pay_fine_removes_from_due_list(self):
        """After paying, the issue no longer appears in list_due_fines()."""
        self.library.pay_fine(self.issue_id)
        dues = self.library.list_due_fines()
        due_ids = [d["issue_id"] for d in dues]
        self.assertNotIn(self.issue_id, due_ids)

    def test_pay_fine_on_already_paid_raises(self):
        """Calling pay_fine() on an already PAID fine raises FineNotDueError."""
        self.library.pay_fine(self.issue_id)
        with self.assertRaises(FineNotDueError):
            self.library.pay_fine(self.issue_id)

    def test_pay_fine_on_none_status_raises(self):
        """Calling pay_fine() on a NONE fine (no overdue) raises FineNotDueError."""
        # Issue and return on time
        book2 = self.library.add_book("On Time Book", "Author Y", 1)
        self.library.issue_book(book2.book_id, self.student.student_id)
        result = self.library.return_book(book2.book_id, self.student.student_id)
        self.assertEqual(result["fine_status"], "NONE")
        with self.assertRaises(FineNotDueError):
            self.library.pay_fine(result["issue_id"])

    def test_pay_fine_invalid_issue_id_raises(self):
        """pay_fine() with invalid issue_id raises IssueNotFoundError."""
        with self.assertRaises(IssueNotFoundError):
            self.library.pay_fine(99999)

    def test_list_paid_fines(self):
        """list_paid_fines returns issues marked as PAID."""
        self.assertEqual(len(self.library.list_paid_fines()), 0)
        self.library.pay_fine(self.issue_id)
        paid = self.library.list_paid_fines()
        self.assertEqual(len(paid), 1)
        self.assertEqual(paid[0]["issue_id"], self.issue_id)
        self.assertEqual(paid[0]["fine_status"], "PAID")

    def test_list_paid_fines_by_student(self):
        """list_paid_fines_by_student returns paid transactions for that student."""
        self.library.pay_fine(self.issue_id)
        paid = self.library.list_paid_fines_by_student(self.student.student_id)
        self.assertEqual(len(paid), 1)
        self.assertEqual(paid[0]["student_id"], self.student.student_id)

    def test_list_paid_fines_by_student_invalid_raises(self):
        """list_paid_fines_by_student raises StudentNotFoundError on invalid ID."""
        with self.assertRaises(StudentNotFoundError):
            self.library.list_paid_fines_by_student(99999)


# ==============================================================================
# Issue Listing Tests
# ==============================================================================

class TestIssueListing(TestLibrarySetup):

    def test_no_active_issues_initially(self):
        """No active issues on a fresh database."""
        issues = self.library.list_active_issues()
        self.assertEqual(issues, [])

    def test_active_issues_after_issue(self):
        """Active issues reflect the current issued loans."""
        book = self.library.add_book("Effective Python", "Brett Slatkin", 1)
        student = self.library.register_student("Kai", "kai@example.com")
        self.library.issue_book(book.book_id, student.student_id)

        issues = self.library.list_active_issues()
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]["book_id"], book.book_id)
        self.assertEqual(issues[0]["student_id"], student.student_id)

    def test_returned_books_not_in_active_issues(self):
        """Returned books do not appear in active issues."""
        book = self.library.add_book("Fluent Python", "Luciano Ramalho", 1)
        student = self.library.register_student("Lena", "lena@example.com")
        self.library.issue_book(book.book_id, student.student_id)
        self.library.return_book(book.book_id, student.student_id)
        issues = self.library.list_active_issues()
        self.assertEqual(len(issues), 0)

    def test_list_all_issues_contains_both_statuses(self):
        """list_all_issues returns both ISSUED and RETURNED records."""
        book = self.library.add_book("Book X", "Author X", 2)
        s1 = self.library.register_student("M1", "m1@ex.com")
        s2 = self.library.register_student("M2", "m2@ex.com")

        self.library.issue_book(book.book_id, s1.student_id)         # stays ISSUED
        self.library.issue_book(book.book_id, s2.student_id)
        self.library.return_book(book.book_id, s2.student_id)        # RETURNED

        all_issues = self.library.list_all_issues()
        statuses = {i["status"] for i in all_issues}
        self.assertIn("ISSUED", statuses)
        self.assertIn("RETURNED", statuses)
        self.assertEqual(len(all_issues), 2)


# ==============================================================================
# Statistics Tests
# ==============================================================================

class TestStatistics(TestLibrarySetup):

    def test_initial_statistics_zeros(self):
        """Fresh library shows zero counts."""
        stats = self.library.get_statistics()
        self.assertEqual(stats["total_unique_books"], 0)
        self.assertEqual(stats["currently_issued"], 0)
        self.assertEqual(stats["total_issues"], 0)
        self.assertEqual(stats["total_fines_paid"], 0.0)
        self.assertEqual(stats["total_fines_due"], 0.0)
        self.assertEqual(stats["top_issued_books"], [])

    def test_statistics_after_issuance(self):
        """Statistics update correctly after a book issuance."""
        book = self.library.add_book("Book X", "Author X", 3)
        student = self.library.register_student("Henry", "henry@example.com")
        self.library.issue_book(book.book_id, student.student_id)

        stats = self.library.get_statistics()
        self.assertEqual(stats["total_unique_books"], 1)
        self.assertEqual(stats["total_copies"], 3)
        self.assertEqual(stats["available_copies"], 2)
        self.assertEqual(stats["currently_issued"], 1)
        self.assertEqual(stats["total_issues"], 1)

    def test_statistics_fines_due_and_paid(self):
        """Statistics correctly split fines into due and paid buckets."""
        b1 = self.library.add_book("Book A", "Auth A", 2)
        b2 = self.library.add_book("Book B", "Auth B", 1)
        s1 = self.library.register_student("P1", "p1@ex.com")
        s2 = self.library.register_student("P2", "p2@ex.com")

        # Issue both with -1 day window so due date is yesterday → both are overdue
        self.library.issue_book(b1.book_id, s1.student_id, duration_days=-1)
        r1 = self.library.return_book(b1.book_id, s1.student_id)

        self.library.issue_book(b2.book_id, s2.student_id, duration_days=-1)
        r2 = self.library.return_book(b2.book_id, s2.student_id)

        # Pay one fine
        self.library.pay_fine(r1["issue_id"])

        stats = self.library.get_statistics()
        self.assertGreater(stats["total_fines_paid"], 0.0)
        self.assertGreater(stats["total_fines_due"], 0.0)
        # Paid and due should be equal since same duration
        self.assertAlmostEqual(stats["total_fines_paid"], stats["total_fines_due"])

    def test_top_issued_books(self):
        """Most issued book appears first in the top list."""
        b1 = self.library.add_book("Hot Book", "Author A", 5)
        b2 = self.library.add_book("Cold Book", "Author B", 5)
        s1 = self.library.register_student("Ivan", "ivan@example.com")
        s2 = self.library.register_student("Jane", "jane@example.com")

        self.library.issue_book(b1.book_id, s1.student_id)
        self.library.return_book(b1.book_id, s1.student_id)
        self.library.issue_book(b1.book_id, s2.student_id)
        self.library.return_book(b1.book_id, s2.student_id)
        self.library.issue_book(b2.book_id, s1.student_id)

        stats = self.library.get_statistics()
        top = stats["top_issued_books"]
        self.assertGreater(len(top), 0)
        self.assertEqual(top[0]["book_id"], b1.book_id)
        self.assertEqual(top[0]["times_issued"], 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
