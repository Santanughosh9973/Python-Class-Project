"""
main.py — Application entry point for the Library Management System CLI.
Runs an interactive continuous terminal loop presenting a menu of operations.
"""

import sys

from library import Library
from models import LibraryError, InvalidOperationError
from views import (
    clear_screen,
    display_menu,
    display_header,
    display_error,
    display_separator,
    view_available_books,
    view_search_books,
    view_add_book,
    view_register_student,
    view_list_students,
    view_issue_book,
    view_return_book,
    view_active_issues,
    view_all_issues,
    view_all_dues,
    view_dues_by_student,
    view_pay_fine,
    view_all_payments,
    view_payments_by_student,
    view_statistics,
)


# ==============================================================================
# Menu Action Dispatch Map
# ==============================================================================

def get_action_map(library: Library) -> dict:
    """
    Builds the mapping of menu choice strings to their handler callables.

    Args:
        library (Library): Shared Library service instance.

    Returns:
        dict: Mapping of choice -> callable view function.
    """
    return {
        "1":  lambda: view_available_books(library),
        "2":  lambda: view_search_books(library),
        "3":  lambda: view_add_book(library),
        "4":  lambda: view_register_student(library),
        "5":  lambda: view_list_students(library),
        "6":  lambda: view_issue_book(library),
        "7":  lambda: view_return_book(library),
        "8":  lambda: view_active_issues(library),
        "9":  lambda: view_all_issues(library),
        "10": lambda: view_all_dues(library),
        "11": lambda: view_dues_by_student(library),
        "12": lambda: view_pay_fine(library),
        "13": lambda: view_all_payments(library),
        "14": lambda: view_payments_by_student(library),
        "15": lambda: view_statistics(library),
    }


# ==============================================================================
# Main Application Loop
# ==============================================================================

def main_loop() -> None:
    """
    Runs the main interactive CLI loop.

    Initializes the Library service, displays a menu on each iteration,
    reads the user's choice (0–13), dispatches to the appropriate view,
    and loops until the user chooses to exit (option 0).
    """
    library = Library(db_path="library.db")
    action_map = get_action_map(library)

    clear_screen()
    print()
    print("  ╔══════════════════════════════════════════════════════════════╗")
    print("  ║        Welcome to the Library Management System!            ║")
    print("  ║        Powered by SQLite3  |  Built with Python OOP         ║")
    print("  ╚══════════════════════════════════════════════════════════════╝")

    while True:
        display_menu()

        try:
            choice = input("  Enter your choice (0–15): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n")
            display_header("Goodbye!")
            print("  Thank you for using the Library Management System.\n")
            sys.exit(0)

        print()

        if choice == "0":
            try:
                confirm = input("  Are you sure you want to exit? [y/N]: ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                confirm = "y"

            if confirm in ("y", "yes"):
                print()
                display_separator()
                print("  Thank you for using the Library Management System.")
                print("  Goodbye! 👋")
                display_separator()
                print()
                sys.exit(0)
            else:
                continue

        elif choice in action_map:
            try:
                action_map[choice]()
            except LibraryError as e:
                display_error(str(e))
                input("\n  Press [Enter] to continue...")
            except Exception as e:
                display_error(f"An unexpected error occurred: {e}")
                input("\n  Press [Enter] to continue...")

        else:
            display_error(
                f"'{choice}' is not a valid option. Please enter a number between 0 and 15."
            )
            input("\n  Press [Enter] to continue...")


# ==============================================================================
# Script Entry Point
# ==============================================================================

if __name__ == "__main__":
    main_loop()
