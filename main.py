"""
main.py — Main entry point for the Library Management System (Flask Web UI).
Runs the local Flask development server.
"""

from app import app

if __name__ == "__main__":
    print("=" * 60)
    print("  Library Management System (Web Application)")
    print("  Starting local development server...")
    print("  Open http://127.0.0.1:5000 in your web browser.")
    print("=" * 60)
    app.run(host="127.0.0.1", port=5000, debug=True)
