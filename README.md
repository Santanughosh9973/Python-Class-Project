# Library Management System (Web Application)

A modern, web-based Library Management System built with **Python** and **Flask**.

---

## Features

- **Dashboard**: Real-time summary statistics, issued books, member count, and recent transactions.
- **Book Management**: Add, view, search, edit, and delete catalog books.
- **Student / Member Management**: Register and manage students/members.
- **Circulation System**: Issue books to students with due dates and handle book returns with automatic overdue fee calculation.
- **Transaction History**: Audit trail of all book issue and return transactions.
- **Analytics & Statistics**: Quick overview of library performance metrics.
- **Configurable Settings**: Fine rates, borrow limits, and institution details.

---

## Project Structure

```text
.
├── app.py                  # Core Flask web application and routing
├── main.py                 # Main entry point to launch the application
├── library.py              # Business logic tier (Library, Book, Student classes)
├── data/                   # Data storage layer (JSON)
│   ├── books.json          # Book records
│   ├── settings.json       # System configurations and fine settings
│   ├── students.json       # Registered student members
│   └── transactions.json   # Circulation transaction records
├── static/
│   └── style.css           # UI stylesheet
├── templates/              # Jinja2 HTML templates
│   ├── about.html
│   ├── add_book.html
│   ├── add_student.html
│   ├── base.html
│   ├── books.html
│   ├── dashboard.html
│   ├── issue.html
│   ├── return.html
│   ├── settings.html
│   ├── stats.html
│   ├── students.html
│   └── transactions.html
├── project-report.html     # Academic project report
├── requirements.txt        # Python package dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Documentation
```

---

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```
   *(Alternatively: `python app.py`)*

3. **Open in Browser**:
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.
