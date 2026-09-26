from flask import Flask, render_template, request, redirect, url_for, flash

from library import Library, LibraryError


# =========================================================
# CREATE FLASK APPLICATION
# =========================================================

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = "library-management-system-secret-key"

# Create Library object
library = Library("data")


# =========================================================
# GLOBAL COUNTS
# =========================================================

@app.context_processor
def inject_counts():

    return {
        "book_count": len(library.books),
        "student_count": len(library.students),
        "issued_count": len(library.get_issued_books()),
        "available_count": len(library.get_available_books())
    }


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/")
def dashboard():

    stats = library.statistics()

    # Latest 8 transactions
    recent_transactions = library.transactions[-8:][::-1]

    return render_template(
        "dashboard.html",
        stats=stats,
        recent_transactions=recent_transactions
    )


# =========================================================
# BOOKS
# =========================================================

@app.route("/books")
def books():

    query = request.args.get("q", "").strip()

    if query:
        results = library.search_books(query)
    else:
        results = library.books

    return render_template(
        "books.html",
        books=results,
        query=query
    )


# =========================================================
# ADD BOOK
# =========================================================

@app.route("/books/add", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":

        try:

            book_id = request.form["book_id"].strip()
            title = request.form["title"].strip()
            author = request.form["author"].strip()
            category = request.form["category"].strip()
            year = request.form["year"].strip()

            library.add_book(
                book_id,
                title,
                author,
                category,
                year
            )

            flash(
                "Book added successfully.",
                "success"
            )

            return redirect(
                url_for("books")
            )

        except LibraryError as error:

            flash(
                str(error),
                "error"
            )

    return render_template(
        "add_book.html"
    )


# =========================================================
# DELETE BOOK
# =========================================================

@app.route(
    "/books/delete/<book_id>",
    methods=["POST"]
)
def delete_book(book_id):

    try:

        library.delete_book(book_id)

        flash(
            "Book deleted successfully.",
            "success"
        )

    except LibraryError as error:

        flash(
            str(error),
            "error"
        )

    return redirect(
        url_for("books")
    )


# =========================================================
# STUDENTS
# =========================================================

@app.route("/students")
def students():

    query = request.args.get(
        "q",
        ""
    ).strip().lower()

    student_list = library.students

    if query:

        student_list = [

            student

            for student in library.students

            if query in student["student_id"].lower()

            or query in student["name"].lower()

            or query in student.get(
                "email",
                ""
            ).lower()
        ]

    return render_template(
        "students.html",
        students=student_list,
        query=query
    )


# =========================================================
# ADD STUDENT
# =========================================================

@app.route(
    "/students/add",
    methods=["GET", "POST"]
)
def add_student():

    if request.method == "POST":

        try:

            student_id = request.form[
                "student_id"
            ].strip()

            name = request.form[
                "name"
            ].strip()

            email = request.form[
                "email"
            ].strip()

            phone = request.form[
                "phone"
            ].strip()

            library.add_student(
                student_id,
                name,
                email,
                phone
            )

            flash(
                "Student added successfully.",
                "success"
            )

            return redirect(
                url_for("students")
            )

        except LibraryError as error:

            flash(
                str(error),
                "error"
            )

    return render_template(
        "add_student.html"
    )


# =========================================================
# ISSUE BOOK
# =========================================================

@app.route(
    "/issue",
    methods=["GET", "POST"]
)
def issue_book():

    if request.method == "POST":

        try:

            # Get selected book
            book_id = request.form[
                "book_id"
            ].strip()

            # Get selected student
            student_id = request.form[
                "student_id"
            ].strip()

            # Fixed borrowing period
            # User does not need to enter this.
            days = 14

            # Issue book
            library.issue_book(
                book_id,
                student_id,
                days
            )

            flash(
                "Book issued successfully.",
                "success"
            )

            return redirect(
                url_for("transactions")
            )

        except LibraryError as error:

            flash(
                str(error),
                "error"
            )

    # Get available books
    available_books = (
        library.get_available_books()
    )

    # Get all students
    students = library.students

    return render_template(
        "issue.html",
        books=available_books,
        students=students
    )


# =========================================================
# RETURN BOOK
# =========================================================

@app.route(
    "/return",
    methods=["GET", "POST"]
)
def return_book():

    if request.method == "POST":

        try:

            book_id = request.form[
                "book_id"
            ].strip()

            result = library.return_book(
                book_id
            )

            # Handle both possible return formats
            if isinstance(result, dict):

                charge = result.get(
                    "charge",
                    0
                )

            else:

                charge = result or 0

            if charge > 0:

                flash(
                    f"Book returned. "
                    f"Overdue charge: "
                    f"₹{charge:.2f}",
                    "success"
                )

            else:

                flash(
                    "Book returned successfully. "
                    "No overdue charge.",
                    "success"
                )

            return redirect(
                url_for("transactions")
            )

        except LibraryError as error:

            flash(
                str(error),
                "error"
            )

    issued_books = (
        library.get_issued_books()
    )

    return render_template(
        "return.html",
        issued_books=issued_books
    )


# =========================================================
# TRANSACTIONS
# =========================================================

@app.route("/transactions")
def transactions():

    transaction_list = (
        library.transactions[::-1]
    )

    return render_template(
        "transactions.html",
        transactions=transaction_list
    )


# =========================================================
# STATISTICS
# =========================================================

@app.route("/stats")
def stats():

    statistics = library.statistics()

    return render_template(
        "stats.html",
        stats=statistics
    )


# =========================================================
# ABOUT
# =========================================================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )