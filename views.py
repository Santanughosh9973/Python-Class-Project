"""
views.py — CLI display formatting and user-input prompt handlers.
Provides ASCII tables, menu rendering, and view controllers for each menu option.

Every view that requires an ID selection first displays the relevant entity table
so the user never needs to remember IDs externally.
"""

import os
from datetime import date
from typing import List

from library import Library
from models import (
    Book,
    Student,
    LibraryError,
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


# ==============================================================================
# Terminal Formatting Utilities
# ==============================================================================

WIDTH = 72  # Total line width for header/footer banners


def clear_screen() -> None:
    """Clears the terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def display_header(title: str) -> None:
    """Renders a full-width banner header with a title."""
    print("=" * WIDTH)
    print(f"  {title.upper()}")
    print("=" * WIDTH)


def display_subheader(title: str) -> None:
    """Renders a lightweight sub-section header."""
    print(f"\n  ── {title} " + "─" * max(0, WIDTH - len(title) - 7))


def display_separator() -> None:
    """Renders a light separator line."""
    print("-" * WIDTH)


def display_success(msg: str) -> None:
    """Prints a success-styled message."""
    print(f"\n  ✔  {msg}")


def display_error(msg: str) -> None:
    """Prints an error-styled message."""
    print(f"\n  ✘  ERROR: {msg}")


def display_info(msg: str) -> None:
    """Prints an informational note."""
    print(f"\n  ℹ  {msg}")


def pause() -> None:
    """Pauses and waits for the user to press Enter."""
    print()
    input("  Press [Enter] to continue...")


def prompt_int(prompt_text: str) -> int:
    """
    Prompts the user for an integer input.

    Args:
        prompt_text (str): The input prompt label.

    Returns:
        int: Validated integer value.

    Raises:
        InvalidOperationError: If the input is not a valid integer.
    """
    raw = input(f"  {prompt_text}: ").strip()
    if not raw.lstrip("-").isdigit():
        raise InvalidOperationError(f"'{raw}' is not a valid integer.")
    return int(raw)


def prompt_str(prompt_text: str, allow_empty: bool = False) -> str:
    """
    Prompts the user for a string input.

    Args:
        prompt_text (str): The input prompt label.
        allow_empty (bool): If False, raises error on blank input.

    Returns:
        str: The stripped string value.

    Raises:
        InvalidOperationError: If input is empty and allow_empty is False.
    """
    raw = input(f"  {prompt_text}: ").strip()
    if not allow_empty and not raw:
        raise InvalidOperationError(f"'{prompt_text}' cannot be empty.")
    return raw


# ==============================================================================
# Table Rendering Helpers
# ==============================================================================

def render_books_table(books: List[Book]) -> None:
    """
    Renders a formatted ASCII table of book records.

    Args:
        books (List[Book]): The list of books to display.
    """
    if not books:
        display_info("No books found.")
        return

    id_w = max(4, max(len(str(b.book_id)) for b in books))
    title_w = min(35, max(5, max(len(b.title) for b in books)))
    author_w = min(25, max(6, max(len(b.author) for b in books)))
    copies_w = 15

    def row_line(bid, title, author, copies):
        return (
            f"  {str(bid):<{id_w}}  "
            f"{str(title):<{title_w}}  "
            f"{str(author):<{author_w}}  "
            f"{str(copies):<{copies_w}}"
        )

    header = row_line("ID", "Title", "Author", "Available/Total")
    separator = "  " + "-" * (id_w + title_w + author_w + copies_w + 8)

    print()
    print(header)
    print(separator)
    for b in books:
        copies_str = f"{b.available_copies}/{b.total_copies}"
        title_display = b.title[:title_w] if len(b.title) > title_w else b.title
        author_display = (
            b.author[:author_w] if len(b.author) > author_w else b.author
        )
        print(row_line(b.book_id, title_display, author_display, copies_str))
    print()


def render_students_table(students: List[Student]) -> None:
    """
    Renders a formatted ASCII table of student records.

    Args:
        students (List[Student]): The list of students to display.
    """
    if not students:
        display_info("No students registered yet.")
        return

    id_w = max(4, max(len(str(s.student_id)) for s in students))
    name_w = min(30, max(4, max(len(s.name) for s in students)))
    email_w = min(35, max(5, max(len(s.email) for s in students)))

    def row_line(sid, name, email):
        return (
            f"  {str(sid):<{id_w}}  "
            f"{str(name):<{name_w}}  "
            f"{str(email):<{email_w}}"
        )

    header = row_line("ID", "Name", "Email")
    separator = "  " + "-" * (id_w + name_w + email_w + 6)

    print()
    print(header)
    print(separator)
    for s in students:
        name_display = s.name[:name_w] if len(s.name) > name_w else s.name
        email_display = s.email[:email_w] if len(s.email) > email_w else s.email
        print(row_line(s.student_id, name_display, email_display))
    print()


def render_active_issues_table(issues: List[dict]) -> None:
    """
    Renders an ASCII table of currently active (ISSUED) book issues.
    Shows issue_id, book, student, issued date, due date, and overdue status.

    Args:
        issues (List[dict]): Active issue rows from list_active_issues().
    """
    if not issues:
        display_info("No active issues at the moment.")
        return

    today = date.today()
    print()

    id_w   = 7
    bid_w  = 5
    title_w = 26
    sid_w  = 5
    name_w = 20
    idate_w = 12
    ddate_w = 12

    def row_fmt(iid, bid, title, sid, name, idate, ddate, status):
        return (
            f"  {str(iid):<{id_w}}"
            f"{str(bid):<{bid_w}}"
            f"{str(title):<{title_w}}"
            f"{str(sid):<{sid_w}}"
            f"{str(name):<{name_w}}"
            f"{str(idate):<{idate_w}}"
            f"{str(ddate):<{ddate_w}}"
            f"  {str(status)}"
        )

    total_w = id_w + bid_w + title_w + sid_w + name_w + idate_w + ddate_w + 10
    print(row_fmt("Issue#", "Bk#", "Title", "St#", "Student", "Issued", "Due", "Status"))
    print("  " + "-" * total_w)

    for r in issues:
        due_d = date.fromisoformat(r["due_date"])
        status = "⚠ OVERDUE" if due_d < today else "Active"
        title_d = r["book_title"][:title_w] if len(r["book_title"]) > title_w else r["book_title"]
        name_d  = r["student_name"][:name_w] if len(r["student_name"]) > name_w else r["student_name"]
        print(row_fmt(
            r["issue_id"], r["book_id"], title_d,
            r["student_id"], name_d,
            r["issue_date"], r["due_date"], status,
        ))
    print()


def render_all_issues_table(issues: List[dict]) -> None:
    """
    Renders an ASCII table of all issue records (ISSUED and RETURNED).
    Includes fine amount and fine status columns.

    Args:
        issues (List[dict]): All issue rows from list_all_issues().
    """
    if not issues:
        display_info("No issue records found.")
        return

    today = date.today()
    print()

    id_w    = 7
    title_w = 22
    name_w  = 18
    date_w  = 12
    fine_w  = 9
    fstat_w = 7
    stat_w  = 9

    def row_fmt(iid, title, name, idate, rdate, fine, fstat, stat):
        return (
            f"  {str(iid):<{id_w}}"
            f"{str(title):<{title_w}}"
            f"{str(name):<{name_w}}"
            f"{str(idate):<{date_w}}"
            f"{str(rdate):<{date_w}}"
            f"{str(fine):<{fine_w}}"
            f"{str(fstat):<{fstat_w}}"
            f"  {str(stat)}"
        )

    total_w = id_w + title_w + name_w + date_w * 2 + fine_w + fstat_w + stat_w + 4
    print(row_fmt("Issue#", "Title", "Student", "Issued", "Returned", "Fine", "FnStat", "Status"))
    print("  " + "-" * total_w)

    for r in issues:
        title_d  = r["book_title"][:title_w] if len(r["book_title"]) > title_w else r["book_title"]
        name_d   = r["student_name"][:name_w] if len(r["student_name"]) > name_w else r["student_name"]
        rdate    = r["return_date"] if r["return_date"] else "-"
        fine_str = f"₹{r['fine_amount']:.2f}" if r["fine_amount"] > 0 else "-"
        fstat    = r["fine_status"]
        stat     = r["status"]
        print(row_fmt(
            r["issue_id"], title_d, name_d,
            r["issue_date"], rdate,
            fine_str, fstat, stat,
        ))
    print()


def render_dues_table(dues: List[dict]) -> None:
    """
    Renders an ASCII table of outstanding (DUE) fine records.

    Args:
        dues (List[dict]): DUE fine rows from list_due_fines() or list_due_fines_by_student().
    """
    if not dues:
        display_info("No outstanding dues found.")
        return

    print()

    id_w    = 7
    title_w = 26
    name_w  = 20
    date_w  = 12
    fine_w  = 10

    def row_fmt(iid, title, name, due_date, ret_date, fine):
        return (
            f"  {str(iid):<{id_w}}"
            f"{str(title):<{title_w}}"
            f"{str(name):<{name_w}}"
            f"{str(due_date):<{date_w}}"
            f"{str(ret_date):<{date_w}}"
            f"  {str(fine):<{fine_w}}"
        )

    total_w = id_w + title_w + name_w + date_w * 2 + fine_w + 4
    print(row_fmt("Issue#", "Book Title", "Student", "Due Date", "Returned", "Fine Owed"))
    print("  " + "-" * total_w)

    for r in dues:
        title_d  = r["book_title"][:title_w] if len(r["book_title"]) > title_w else r["book_title"]
        name_d   = r["student_name"][:name_w] if len(r["student_name"]) > name_w else r["student_name"]
        rdate    = r["return_date"] if r["return_date"] else "-"
        fine_str = f"₹{r['fine_amount']:.2f}"
        print(row_fmt(r["issue_id"], title_d, name_d, r["due_date"], rdate, fine_str))
    print()


def render_payments_table(payments: List[dict]) -> None:
    """
    Renders an ASCII table of paid fine (income) records.

    Args:
        payments (List[dict]): PAID fine rows from list_paid_fines() or list_paid_fines_by_student().
    """
    if not payments:
        display_info("No payment transactions found.")
        return

    print()

    id_w    = 7
    title_w = 26
    name_w  = 20
    date_w  = 12
    fine_w  = 12

    def row_fmt(iid, title, name, ret_date, fine):
        return (
            f"  {str(iid):<{id_w}}"
            f"{str(title):<{title_w}}"
            f"{str(name):<{name_w}}"
            f"{str(ret_date):<{date_w}}"
            f"  {str(fine):<{fine_w}}"
        )

    total_w = id_w + title_w + name_w + date_w + fine_w + 4
    print(row_fmt("Issue#", "Book Title", "Student", "Paid Date", "Amount Paid"))
    print("  " + "-" * total_w)

    for r in payments:
        title_d  = r["book_title"][:title_w] if len(r["book_title"]) > title_w else r["book_title"]
        name_d   = r["student_name"][:name_w] if len(r["student_name"]) > name_w else r["student_name"]
        rdate    = r["return_date"] if r["return_date"] else "-"
        fine_str = f"₹{r['fine_amount']:.2f}"
        print(row_fmt(r["issue_id"], title_d, name_d, rdate, fine_str))
    print()


# ==============================================================================
# Main Menu
# ==============================================================================

def display_menu() -> None:
    """Renders the main interactive menu."""
    print()
    display_header("Library Management System")
    print(f"  {'[1]':<5} Display Available Books")
    print(f"  {'[2]':<5} Search Books (by Title / Author)")
    print(f"  {'[3]':<5} Add New Book to Catalog")
    print(f"  {'[4]':<5} Register New Student / Member")
    print(f"  {'[5]':<5} Display All Students / Members")
    print(f"  {'[6]':<5} Issue a Book to Student")
    print(f"  {'[7]':<5} Return a Book")
    print(f"  {'─' * 55}")
    print(f"  {'[8]':<5} View Active Issues  (currently borrowed)")
    print(f"  {'[9]':<5} View All Issues     (full history)")
    print(f"  {'─' * 55}")
    print(f"  {'[10]':<5} View All Outstanding Dues")
    print(f"  {'[11]':<5} View Dues by Student")
    print(f"  {'[12]':<5} Pay a Fine (Clear Due)")
    print(f"  {'─' * 55}")
    print(f"  {'[13]':<5} View All Money Income (Paid Fines)")
    print(f"  {'[14]':<5} View Money Income by Student")
    print(f"  {'─' * 55}")
    print(f"  {'[15]':<5} Library Statistics & Reports")
    print(f"  {'─' * 55}")
    print(f"  {'[0]':<5} Exit")
    display_separator()


# ==============================================================================
# Individual View Controllers
# ==============================================================================

def view_available_books(library: Library) -> None:
    """Displays all books that have at least one available copy."""
    display_header("Available Books")
    books = library.display_available_books()
    if not books:
        display_info("All books are currently checked out or no books are in the catalog.")
    else:
        print(f"  Showing {len(books)} available book(s):")
        render_books_table(books)
    pause()


def view_search_books(library: Library) -> None:
    """Prompts user for a keyword and search field, then displays results."""
    display_header("Search Books")
    try:
        keyword = prompt_str("Enter search keyword (title or author)")
        print()
        print("  Search by:")
        print("    [1] Title only")
        print("    [2] Author only")
        print("    [3] Both (default)")
        field_choice = input("  Your choice [1/2/3]: ").strip()

        field_map = {"1": "title", "2": "author", "3": "all", "": "all"}
        field = field_map.get(field_choice, "all")

        results = library.search_books(keyword, field)
        if not results:
            display_info(f"No books found matching '{keyword}'.")
        else:
            print(f"\n  Found {len(results)} result(s) for '{keyword}':")
            render_books_table(results)
    except LibraryError as e:
        display_error(str(e))
    pause()


def view_add_book(library: Library) -> None:
    """Prompts for book details and adds a new book to the catalog."""
    display_header("Add New Book")
    try:
        title = prompt_str("Book Title")
        author = prompt_str("Author Name")
        copies = prompt_int("Number of Copies (e.g. 3)")

        book = library.add_book(title, author, copies)
        display_success(
            f"Book added successfully!\n"
            f"    Book ID : {book.book_id}\n"
            f"    Title   : {book.title}\n"
            f"    Author  : {book.author}\n"
            f"    Copies  : {book.total_copies}"
        )
    except LibraryError as e:
        display_error(str(e))
    pause()


def view_register_student(library: Library) -> None:
    """Prompts for student details and registers a new library member."""
    display_header("Register New Student / Member")
    try:
        name = prompt_str("Full Name")
        email = prompt_str("Email Address")

        student = library.register_student(name, email)
        display_success(
            f"Student registered successfully!\n"
            f"    Student ID : {student.student_id}\n"
            f"    Name       : {student.name}\n"
            f"    Email      : {student.email}"
        )
    except LibraryError as e:
        display_error(str(e))
    pause()


def view_list_students(library: Library) -> None:
    """Displays all registered students in a table."""
    display_header("Registered Students / Members")
    students = library.list_students()
    if not students:
        display_info("No students have been registered yet.")
    else:
        print(f"  Showing {len(students)} registered member(s):")
        render_students_table(students)
    pause()


def view_issue_book(library: Library) -> None:
    """
    Handles book issuance.
    Shows available books and registered students before asking for IDs.
    """
    display_header("Issue Book to Student")

    try:
        # --- Contextual: show available books ---
        display_subheader("Available Books")
        books = library.display_available_books()
        if not books:
            display_info("No books are currently available for issue.")
            pause()
            return
        render_books_table(books)

        # --- Contextual: show registered students ---
        display_subheader("Registered Students")
        students = library.list_students()
        if not students:
            display_info("No students are registered yet.")
            pause()
            return
        render_students_table(students)

        # --- Prompt for IDs ---
        book_id = prompt_int("Enter Book ID to Issue")
        student_id = prompt_int("Enter Student ID")

        result = library.issue_book(book_id, student_id)
        display_success(
            f"Book issued successfully!\n"
            f"    Issue #       : {result['issue_id']}\n"
            f"    Book          : [{result['book_id']}] {result['book_title']}\n"
            f"    Student       : [{result['student_id']}] {result['student_name']}\n"
            f"    Issue Date    : {result['issue_date']}\n"
            f"    Due Date      : {result['due_date']}  (return by this date to avoid fines)"
        )
    except LibraryError as e:
        display_error(str(e))
    pause()


def view_return_book(library: Library) -> None:
    """
    Handles book return.
    Shows active issues before asking for Book ID and Student ID.
    After return, if a fine is incurred prompts whether the user paid immediately.
    """
    display_header("Return a Book")

    try:
        # --- Contextual: show active issues ---
        display_subheader("Currently Active Issues")
        active = library.list_active_issues()
        if not active:
            display_info("There are no active issues to return.")
            pause()
            return
        render_active_issues_table(active)

        # --- Prompt for IDs ---
        book_id    = prompt_int("Enter Book ID to Return")
        student_id = prompt_int("Enter Student ID")

        result = library.return_book(book_id, student_id)

        if result["fine_amount"] > 0:
            fine_msg = f"₹{result['fine_amount']:.2f}  [STATUS: DUE]"
        else:
            fine_msg = "None (returned on time)"

        display_success(
            f"Book returned successfully!\n"
            f"    Issue #       : {result['issue_id']}\n"
            f"    Book          : [{result['book_id']}] {result['book_title']}\n"
            f"    Student       : [{result['student_id']}] {result['student_name']}\n"
            f"    Issue Date    : {result['issue_date']}\n"
            f"    Due Date      : {result['due_date']}\n"
            f"    Return Date   : {result['return_date']}\n"
            f"    Overdue Fine  : {fine_msg}"
        )

        # --- If fine incurred, offer immediate payment ---
        if result["fine_amount"] > 0:
            print()
            paid_now = input(
                f"  Did the student pay ₹{result['fine_amount']:.2f} now? [y/N]: "
            ).strip().lower()
            if paid_now in ("y", "yes"):
                pay_result = library.pay_fine(result["issue_id"])
                display_success(
                    f"Fine of ₹{pay_result['fine_amount']:.2f} marked as PAID.\n"
                    f"    Issue #  : {pay_result['issue_id']}\n"
                    f"    Student  : {pay_result['student_name']}"
                )
            else:
                display_info(
                    f"Fine marked as DUE. Use option [12] to collect payment later."
                )

    except LibraryError as e:
        display_error(str(e))
    pause()


def view_active_issues(library: Library) -> None:
    """Displays all currently active (ISSUED) book loans."""
    display_header("Active Issues — Currently Borrowed Books")
    issues = library.list_active_issues()
    today = date.today()

    overdue = [i for i in issues if date.fromisoformat(i["due_date"]) < today]
    on_time = [i for i in issues if date.fromisoformat(i["due_date"]) >= today]

    if issues:
        print(
            f"  Total Active: {len(issues)}  |  "
            f"On Time: {len(on_time)}  |  "
            f"Overdue: {len(overdue)}"
        )

    render_active_issues_table(issues)
    pause()


def view_all_issues(library: Library) -> None:
    """Displays the complete issue history — both active and returned."""
    display_header("All Issues — Complete History")
    issues = library.list_all_issues()

    if issues:
        issued   = sum(1 for i in issues if i["status"] == "ISSUED")
        returned = sum(1 for i in issues if i["status"] == "RETURNED")
        dues     = sum(1 for i in issues if i["fine_status"] == "DUE")
        paid     = sum(1 for i in issues if i["fine_status"] == "PAID")
        print(
            f"  Total: {len(issues)}  |  "
            f"Active: {issued}  |  Returned: {returned}  |  "
            f"Dues Pending: {dues}  |  Fines Paid: {paid}"
        )

    render_all_issues_table(issues)
    pause()


def view_all_dues(library: Library) -> None:
    """Displays all outstanding (DUE) fines across all students."""
    display_header("All Outstanding Dues")
    dues = library.list_due_fines()

    if dues:
        total_due = sum(d["fine_amount"] for d in dues)
        print(f"  {len(dues)} outstanding due(s)  |  Total owed: ₹{total_due:.2f}")

    render_dues_table(dues)
    pause()


def view_dues_by_student(library: Library) -> None:
    """
    Displays outstanding dues for a specific student.
    Shows the students list first so the user can pick an ID.
    """
    display_header("Dues by Student")

    try:
        # --- Contextual: show all students ---
        display_subheader("Registered Students")
        students = library.list_students()
        if not students:
            display_info("No students are registered yet.")
            pause()
            return
        render_students_table(students)

        # --- Prompt for student ID ---
        student_id = prompt_int("Enter Student ID to view dues")

        dues = library.list_due_fines_by_student(student_id)
        student = library.get_student_by_id(student_id)

        display_subheader(f"Outstanding Dues for {student.name}")
        if dues:
            total_due = sum(d["fine_amount"] for d in dues)
            print(f"  {len(dues)} outstanding due(s)  |  Total owed: ₹{total_due:.2f}")
        render_dues_table(dues)

    except LibraryError as e:
        display_error(str(e))
    pause()


def view_pay_fine(library: Library) -> None:
    """
    Marks a DUE fine as PAID.
    Shows all outstanding dues first so the user can pick the correct Issue ID.
    """
    display_header("Pay a Fine")

    try:
        # --- Contextual: show all DUE fines ---
        display_subheader("Outstanding Dues (DUE status)")
        dues = library.list_due_fines()
        if not dues:
            display_info("There are no outstanding dues to pay.")
            pause()
            return
        total_due = sum(d["fine_amount"] for d in dues)
        print(f"  {len(dues)} outstanding due(s)  |  Total owed: ₹{total_due:.2f}")
        render_dues_table(dues)

        # --- Prompt for issue ID ---
        issue_id = prompt_int("Enter Issue # to mark as PAID")

        result = library.pay_fine(issue_id)
        display_success(
            f"Fine payment recorded successfully!\n"
            f"    Issue #   : {result['issue_id']}\n"
            f"    Book      : [{result['book_id']}] {result['book_title']}\n"
            f"    Student   : [{result['student_id']}] {result['student_name']}\n"
            f"    Amount    : ₹{result['fine_amount']:.2f}\n"
            f"    Status    : PAID ✔"
        )

    except LibraryError as e:
        display_error(str(e))
    pause()


def view_all_payments(library: Library) -> None:
    """Displays all collected money income transactions across the library."""
    display_header("All Money Income — Paid Fine Transactions")
    payments = library.list_paid_fines()

    if payments:
        total_income = sum(p["fine_amount"] for p in payments)
        print(f"  {len(payments)} transaction(s) recorded  |  Total Income Collected: ₹{total_income:.2f}")

    render_payments_table(payments)
    pause()


def view_payments_by_student(library: Library) -> None:
    """
    Displays all money income transactions paid by a specific student.
    Shows the registered students table first so user can select student ID.
    """
    display_header("Money Income by Student")

    try:
        display_subheader("Registered Students")
        students = library.list_students()
        if not students:
            display_info("No students are registered yet.")
            pause()
            return
        render_students_table(students)

        student_id = prompt_int("Enter Student ID to view payments made")

        payments = library.list_paid_fines_by_student(student_id)
        student = library.get_student_by_id(student_id)

        display_subheader(f"Payments Received from {student.name}")
        if payments:
            total_income = sum(p["fine_amount"] for p in payments)
            print(f"  {len(payments)} payment(s) recorded  |  Total Paid by Student: ₹{total_income:.2f}")
        render_payments_table(payments)

    except LibraryError as e:
        display_error(str(e))
    pause()


def view_statistics(library: Library) -> None:
    """Renders the library statistics and reporting summary."""
    display_header("Library Statistics & Reports")
    stats = library.get_statistics()

    print()
    print(f"  {'─' * 48}")
    print(f"   📚  Catalog Overview")
    print(f"  {'─' * 48}")
    print(f"   Total Unique Titles       : {stats['total_unique_books']}")
    print(f"   Total Copies Owned        : {stats['total_copies']}")
    print(f"   Currently Available       : {stats['available_copies']}")
    print(f"   Currently Issued (out)    : {stats['currently_issued']}")
    print()
    print(f"  {'─' * 48}")
    print(f"   📋  Issues Overview")
    print(f"  {'─' * 48}")
    print(f"   Total Issues (all time)   : {stats['total_issues']}")
    print()
    print(f"  {'─' * 48}")
    print(f"   💰  Fines Overview")
    print(f"  {'─' * 48}")
    print(f"   Total Fines Collected     : ₹{stats['total_fines_paid']:.2f}")
    print(f"   Total Outstanding Dues    : ₹{stats['total_fines_due']:.2f}")
    print()

    if stats["top_issued_books"]:
        print(f"  {'─' * 48}")
        print(f"   🏆  Top {len(stats['top_issued_books'])} Most Issued Books")
        print(f"  {'─' * 48}")
        for i, book in enumerate(stats["top_issued_books"], 1):
            print(
                f"   {i}. [{book['book_id']}] {book['title']} "
                f"by {book['author']}"
                f"  ({book['times_issued']} time(s))"
            )
    else:
        display_info("No issue data yet to compute top books.")

    print()
    pause()
