"""
database.py — Database manager for the Library Management System.
Handles SQLite3 connection management and schema initialization / migration.
"""

import sqlite3
import os


class DatabaseManager:
    """
    Manages the SQLite3 database connection and schema.

    Attributes:
        db_path (str): Path to the SQLite database file.
    """

    def __init__(self, db_path: str = "library.db"):
        self.db_path = db_path
        self.init_db()

    def close(self) -> None:
        """No persistent connection to close; provided for API consistency."""
        pass  # Connections are opened/closed per-operation via context managers

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def get_connection(self) -> sqlite3.Connection:
        """
        Provides a database connection with Row factory enabled.

        Returns:
            sqlite3.Connection: A configured database connection.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        # Enable foreign key enforcement
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def init_db(self) -> None:
        """
        Initializes (or migrates) database schema.

        Handles three scenarios automatically:
        1. Fresh database  — creates all tables from scratch.
        2. Old database with `transactions` table — renames to `issues`
           and adds the new `fine_status` column.
        3. Already-migrated database — no-ops on all IF NOT EXISTS guards.
        """
        with self.get_connection() as conn:
            # ------------------------------------------------------------------
            # Migration: rename old `transactions` → `issues` if needed
            # ------------------------------------------------------------------
            tables = {
                row[0]
                for row in conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                ).fetchall()
            }

            if "transactions" in tables and "issues" not in tables:
                # Step 1: rename
                conn.execute("ALTER TABLE transactions RENAME TO issues")
                # Step 2: add fine_status column (may error if already exists — ignore)
                try:
                    conn.execute(
                        "ALTER TABLE issues ADD COLUMN fine_status TEXT DEFAULT 'NONE'"
                    )
                except sqlite3.OperationalError:
                    pass
                # Step 3: rename transaction_id → issue_id is not supported by SQLite
                # directly, so we recreate the table only if the old column name exists.
                cols = {
                    row[1]
                    for row in conn.execute("PRAGMA table_info(issues)").fetchall()
                }
                if "transaction_id" in cols:
                    conn.executescript(
                        """
                        CREATE TABLE issues_new (
                            issue_id        INTEGER PRIMARY KEY AUTOINCREMENT,
                            book_id         INTEGER NOT NULL,
                            student_id      INTEGER NOT NULL,
                            issue_date      TEXT    NOT NULL,
                            due_date        TEXT    NOT NULL,
                            return_date     TEXT,
                            fine_amount     REAL    DEFAULT 0.0,
                            fine_status     TEXT    DEFAULT 'NONE',
                            status          TEXT    NOT NULL,
                            FOREIGN KEY(book_id)    REFERENCES books(book_id),
                            FOREIGN KEY(student_id) REFERENCES students(student_id)
                        );
                        INSERT INTO issues_new
                            (issue_id, book_id, student_id, issue_date, due_date,
                             return_date, fine_amount, fine_status, status)
                        SELECT transaction_id, book_id, student_id, issue_date, due_date,
                               return_date, fine_amount,
                               CASE WHEN fine_amount > 0 AND status = 'RETURNED'
                                    THEN 'DUE' ELSE 'NONE' END,
                               status
                        FROM issues;
                        DROP TABLE issues;
                        ALTER TABLE issues_new RENAME TO issues;
                        """
                    )

            # ------------------------------------------------------------------
            # Create tables (fresh install or already migrated)
            # ------------------------------------------------------------------
            ddl_statements = [
                # Books catalog
                """
                CREATE TABLE IF NOT EXISTS books (
                    book_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    title           TEXT    NOT NULL,
                    author          TEXT    NOT NULL,
                    total_copies    INTEGER NOT NULL CHECK(total_copies >= 1),
                    available_copies INTEGER NOT NULL CHECK(available_copies >= 0)
                )
                """,

                # Student / member records
                """
                CREATE TABLE IF NOT EXISTS students (
                    student_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    name        TEXT    NOT NULL,
                    email       TEXT    UNIQUE NOT NULL
                )
                """,

                # Book issue log (issuance & returns) with fine payment tracking
                """
                CREATE TABLE IF NOT EXISTS issues (
                    issue_id        INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id         INTEGER NOT NULL,
                    student_id      INTEGER NOT NULL,
                    issue_date      TEXT    NOT NULL,
                    due_date        TEXT    NOT NULL,
                    return_date     TEXT,
                    fine_amount     REAL    DEFAULT 0.0,
                    fine_status     TEXT    NOT NULL DEFAULT 'NONE'
                                    CHECK(fine_status IN ('NONE', 'DUE', 'PAID')),
                    status          TEXT    NOT NULL
                                    CHECK(status IN ('ISSUED', 'RETURNED')),
                    FOREIGN KEY(book_id)    REFERENCES books(book_id),
                    FOREIGN KEY(student_id) REFERENCES students(student_id)
                )
                """,

                # Indexes for faster lookups
                """
                CREATE INDEX IF NOT EXISTS idx_books_title
                ON books(title)
                """,
                """
                CREATE INDEX IF NOT EXISTS idx_books_author
                ON books(author)
                """,
                """
                CREATE INDEX IF NOT EXISTS idx_issues_status
                ON issues(status)
                """,
                """
                CREATE INDEX IF NOT EXISTS idx_issues_fine_status
                ON issues(fine_status)
                """,
                """
                CREATE INDEX IF NOT EXISTS idx_issues_book_student
                ON issues(book_id, student_id, status)
                """,
            ]

            for statement in ddl_statements:
                conn.execute(statement)

            conn.commit()
