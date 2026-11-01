"""
generate_pptx.py
Generates a professional 15-slide PowerPoint (.pptx) presentation
for the Python Class Project: Library Management System.
Complies with all 14 required academic components and Brainware University guidelines.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation(output_path="Python_Class_Project_Presentation.pptx"):
    prs = Presentation()
    # 16:9 widescreen format
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    NAVY = RGBColor(15, 23, 42)        # Slate 900
    DEEP_BLUE = RGBColor(30, 58, 138)   # Blue 900
    PRIMARY_BLUE = RGBColor(37, 99, 235)# Blue 600
    ACCENT_CYAN = RGBColor(14, 165, 233)# Sky 500
    GOLD = RGBColor(217, 119, 6)        # Amber 600
    LIGHT_BG = RGBColor(248, 250, 252)  # Slate 50
    CARD_BG = RGBColor(255, 255, 255)   # White
    BORDER_COLOR = RGBColor(203, 213, 225) # Slate 300
    TEXT_DARK = RGBColor(15, 23, 42)
    TEXT_MUTED = RGBColor(71, 85, 105)
    SUCCESS_GREEN = RGBColor(22, 163, 74)

    def add_header(slide, title_text, category_text, slide_num):
        # Header banner container
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.9))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = category_text.upper()
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = PRIMARY_BLUE

        p1 = tf.add_paragraph()
        p1.text = title_text
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = NAVY

        # Slide Number Badge
        num_box = slide.shapes.add_textbox(Inches(11.5), Inches(0.4), Inches(1.0), Inches(0.5))
        ntf = num_box.text_frame
        np = ntf.paragraphs[0]
        np.text = f"{slide_num:02d} / 15"
        np.alignment = PP_ALIGN.RIGHT
        np.font.size = Pt(11)
        np.font.bold = True
        np.font.color.rgb = TEXT_MUTED

        # Thin divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(226, 232, 240)
        line.line.color.rgb = RGBColor(226, 232, 240)

    def add_card(slide, left, top, width, height, title, items, bg_color=CARD_BG, border_color=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)

        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)
        tf.margin_bottom = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = DEEP_BLUE
        p.space_after = Pt(8)

        for item in items:
            p = tf.add_paragraph()
            p.text = f"•  {item}"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(4)
        return shape

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Component 1)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = RGBColor(15, 23, 42)
    bg1.line.fill.background()

    # Inner decorative border
    in_border = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.5), Inches(12.133), Inches(6.5))
    in_border.fill.background()
    in_border.line.color.rgb = RGBColor(51, 65, 85)
    in_border.line.width = Pt(2)

    title_box = slide1.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.333), Inches(2.2))
    tf1 = title_box.text_frame
    tf1.word_wrap = True

    p_inst = tf1.paragraphs[0]
    p_inst.text = "BRAINWARE UNIVERSITY • DEPARTMENT OF COMPUTATIONAL SCIENCES"
    p_inst.alignment = PP_ALIGN.CENTER
    p_inst.font.size = Pt(12)
    p_inst.font.bold = True
    p_inst.font.color.rgb = ACCENT_CYAN

    p_proj = tf1.add_paragraph()
    p_proj.text = "LIBRARY MANAGEMENT SYSTEM"
    p_proj.alignment = PP_ALIGN.CENTER
    p_proj.font.size = Pt(32)
    p_proj.font.bold = True
    p_proj.font.color.rgb = CARD_BG
    p_proj.space_before = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "A Modular Python OOP & Relational SQLite Circulation Engine with Contextual CLI & Web Architecture"
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.font.size = Pt(13)
    p_sub.font.italic = True
    p_sub.font.color.rgb = RGBColor(203, 213, 225)
    p_sub.space_before = Pt(4)

    # Info Grid: Left = Course/Dept/Supervisors, Right = Student Group Matrix
    info_box_l = slide1.shapes.add_textbox(Inches(1.2), Inches(3.2), Inches(5.0), Inches(3.2))
    tfl = info_box_l.text_frame
    tfl.word_wrap = True

    p = tfl.paragraphs[0]
    p.text = "ACADEMIC DETAILS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = GOLD

    rows_left = [
        ("Degree Course:", "Master of Computer Applications (MCA)"),
        ("Subject Name:", "Advanced Python & Database Engineering"),
        ("Project Mode:", "Individual Project (Solo Development)"),
        ("Project Supervisor:", "Mr. Rahul Kumar Ghosh (Asst. Prof.)"),
        ("Head of Department:", "Dr. Jayanta Aich (HOD, Comp. Sciences)"),
        ("Academic Session:", "2024 – 2026 (May 2026)"),
    ]
    for lbl, val in rows_left:
        p = tfl.add_paragraph()
        p.text = f"{lbl} {val}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = CARD_BG
        p.space_after = Pt(2)

    # Student team box (Right)
    team_table_shape = slide1.shapes.add_table(2, 3, Inches(6.5), Inches(3.2), Inches(6.0), Inches(1.5))
    tbl = team_table_shape.table
    tbl.columns[0].width = Inches(2.3)
    tbl.columns[1].width = Inches(1.8)
    tbl.columns[2].width = Inches(1.9)

    headers = ["Student Name", "Roll Number", "Student Code"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = DEEP_BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = CARD_BG
        p.alignment = PP_ALIGN.CENTER

    students = [
        ("SANTANU GHOSH", "23010346299", "BWU/MCA/26/022"),
    ]
    for r_idx, (name, roll, code) in enumerate(students, start=1):
        for c_idx, val in enumerate([name, roll, code]):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(30, 41, 59)
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = ACCENT_CYAN
            p.alignment = PP_ALIGN.CENTER

    # University Logo on Slide 1
    logo_file = os.path.join("assets", "university-logo.jpg")
    if os.path.exists(logo_file):
        slide1.shapes.add_picture(logo_file, Inches(9.0), Inches(4.9), width=Inches(1.5), height=Inches(1.5))

    # =========================================================================
    # SLIDE 2: INTRODUCTION (Component 2)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Introduction & Project Background", "Project Overview", 2)

    add_card(slide2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Institutional Need for Digitalization", [
                 "Educational institutions require dependable systems to oversee catalog expansion, member privileges, and circulation accountability.",
                 "Traditional manual registers suffer from paper wear, misplaced ledger pages, and error-prone overdue penalty assessments.",
                 "Modern software demands rapid sub-millisecond querying, zero external network dependency, and automated schema migrations.",
                 "Python provides clean object-oriented syntax, dynamic typing with type hinting, and seamless native C-level SQLite3 integration.",
                 "The Library Management System (LMS) bridges academic theory with production-grade engineering principles."
             ])

    add_card(slide2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Architectural Overview & Core Paradigms", [
                 "Encapsulated Domain Models: Standalone Book and Student domain classes with complete input validation.",
                 "Service-Oriented Design: Central Library manager coordinating circulation logic and business rules.",
                 "Autonomous Database Manager: Context-managed SQLite3 connections with automated DDL schema migrations.",
                 "Predictive Contextual Terminal UI: Live entity preview rendering before every user input prompt.",
                 "Dual-History Circulation Ledger: Real-time separation of active loans from historical returns.",
                 "Granular 3-State Fine Lifecycle: Complete tracking of overdue fines across NONE, DUE, and PAID states."
             ])

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT (Component 3)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Problem Statement & Real-World Challenges", "Problem Formulation", 3)

    add_card(slide3, Inches(0.8), Inches(1.6), Inches(5.6), Inches(2.5),
             "1. Human Calculation & Audit Errors", [
                 "Manual calculation of overdue penalties causes financial discrepancies and student disputes.",
                 "Failure to track partial vs settled fines leads to revenue loss in university departments.",
                 "Inconsistent due date calculations across holidays and semester breaks."
             ])

    add_card(slide3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.5),
             "2. The 'Blind Identifier' CLI Problem", [
                 "Standard terminal applications force operators to memorize numerical Book IDs and Student IDs prior to running operations.",
                 "Entering incorrect IDs causes accidental issuance or runtime crashes.",
                 "Operators must repeatedly switch between 'view all' and 'issue' menus."
             ])

    add_card(slide3, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.5),
             "3. Concurrency & Inventory Inconsistency", [
                 "Books are frequently marked available on shelves while already lent out on paper.",
                 "Simultaneous loans on single-copy reserves cause duplicate issuance conflicts.",
                 "Lack of ACID transactions results in orphaned borrower records."
             ])

    add_card(slide3, Inches(6.8), Inches(4.3), Inches(5.7), Inches(2.5),
             "4. Cloud Dependency & Deployment Friction", [
                 "Heavy enterprise systems (e.g., Koha) require complex Linux server setups, MySQL, and constant internet.",
                 "Rural or lab campus workstations need an offline-first, portable database solution.",
                 "Zero complex prerequisites: must run instantly with standard Python 3.x libraries."
             ])

    # =========================================================================
    # SLIDE 4: OBJECTIVES (Component 4)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Project Aims & Specific Objectives", "Aims & Objectives", 4)

    add_card(slide4, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "Primary & Functional", [
                 "Automated Circulation Engine: Enable instantaneous issuance and check-in with atomic inventory updates.",
                 "Contextual Terminal UX: Render dynamic preview tables above every input to eliminate ID lookups.",
                 "Multi-Field Catalog Search: Implement case-insensitive sub-string queries across Titles and Authors.",
                 "Member Lifecycle Tracking: Manage student records with unique email constraints."
             ])

    add_card(slide4, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "Technical & Architectural", [
                 "Pure Python OOP: Strict separation of concerns across Models, Service, Database, and View layers.",
                 "Atomic SQLite3 Persistence: Connection context managers enforcing foreign key referential integrity.",
                 "Automated DDL Migrations: Self-healing database initialization without operator data loss.",
                 "100% Test Coverage: Comprehensive unittest suite validating 54 edge cases and exceptions."
             ])

    add_card(slide4, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "Financial & Usability", [
                 "3-State Fine Machine: Robust status lifecycle (NONE -> DUE -> PAID) for institutional accountability.",
                 "Automated Penalty Engine: Dynamic accrual at ₹5.00/day past the 7-day borrowing limit.",
                 "Financial Audit Dashboards: Real-time queries for outstanding dues and total fine revenue.",
                 "Dual User Interfaces: Unified business logic accessible via both Rich CLI and Flask Web GUI."
             ])

    # =========================================================================
    # SLIDE 5: SCOPE OF THE PROJECT (Component 5)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Scope, Target Users & Operational Boundaries", "Project Scope", 5)

    add_card(slide5, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Functional Coverage & Target Users", [
                 "Target Users: Academic librarians, department clerks, university students, and lab instructors.",
                 "Inventory Management: Real-time tracking of total copies, issued copies, and available stock.",
                 "Circulation Management: 7-day lending cycles, live overdue flags, and book availability guards.",
                 "Fine Settlement Desk: Direct fine payment interface with receipt reconciliation.",
                 "Reporting & Analytics: Top borrowed books, active borrower metrics, and financial summaries.",
                 "Target Environment: Departmental workstations, laboratory Linux/Windows terminals, LAN-based web access."
             ])

    add_card(slide5, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Operational Limitations & Assumptions", [
                 "Single-Node Deployment: Designed for departmental LAN or single-terminal circulation desks.",
                 "Offline-First Scope: Operates completely offline without external cloud database dependencies.",
                 "Cash / Desk Payment: Fine settlement is recorded administratively at the desk (digital payment integration planned).",
                 "User Assumptions: Operators possess basic computer literacy; student email addresses are unique across departments.",
                 "Scalability Scope: Optimized for departmental libraries with up to 50,000 catalog entries and 10,000 students."
             ])

    # =========================================================================
    # SLIDE 6: LITERATURE REVIEW & EXISTING SYSTEMS (Component 6)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Literature Review & Existing System Comparison", "Existing Systems", 6)

    # Comparison Table
    tbl_shape6 = slide6.shapes.add_table(6, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(3.6))
    t6 = tbl_shape6.table
    t6.columns[0].width = Inches(2.733)
    t6.columns[1].width = Inches(2.25)
    t6.columns[2].width = Inches(2.25)
    t6.columns[3].width = Inches(2.25)
    t6.columns[4].width = Inches(2.25)

    headers6 = ["Feature / Capability", "Manual Register", "Koha ILS", "Basic CLI Script", "Proposed Python LMS"]
    for c_idx, h in enumerate(headers6):
        cell = t6.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = DEEP_BLUE if c_idx < 4 else PRIMARY_BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = CARD_BG
        p.alignment = PP_ALIGN.CENTER

    data6 = [
        ("Setup Complexity", "None (Paper)", "Very High (Linux/Perl/SQL)", "Low (File based)", "Zero (Standard Python)"),
        ("Database Integrity", "Zero (Manual)", "High (MySQL RDBMS)", "Poor (Plain text/CSV)", "High (ACID SQLite3)"),
        ("Contextual Input Previews", "None", "Web search required", "None (Blind prompt)", "Built-in Dynamic ASCII"),
        ("Overdue Fine State Tracking", "Manual Math", "Complex Rules", "Binary or None", "3-State (NONE/DUE/PAID)"),
        ("Automated Unit Testing", "None", "Modular Perl/Ruby", "Rarely implemented", "54 Automated Tests (100%)"),
    ]
    for r_idx, row in enumerate(data6, start=1):
        for c_idx, val in enumerate(row):
            cell = t6.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(241, 245, 249) if r_idx % 2 == 1 else CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9.5)
            p.font.color.rgb = TEXT_DARK
            if c_idx == 4:
                p.font.bold = True
                p.font.color.rgb = PRIMARY_BLUE

    add_card(slide6, Inches(0.8), Inches(5.4), Inches(11.733), Inches(1.5),
             "Literature Review Synthesis", [
                 "Review of academic library systems demonstrates that heavy enterprise tools (Koha, Evergreen) impose excessive server administration costs for small-to-medium departments.",
                 "Conversely, introductory class projects often lack ACID persistence, exception hierarchies, and fine auditability.",
                 "The Proposed System fills this critical niche: production-grade engineering in an ultra-portable, self-contained architecture."
             ])

    # =========================================================================
    # SLIDE 7: PROPOSED SYSTEM (Component 7)
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Proposed System & Key Innovations", "System Proposition", 7)

    add_card(slide7, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "1. Contextual UX Engine", [
                 "Completely solves the CLI 'Blind ID' defect.",
                 "Before asking 'Enter Book ID', the system automatically queries and displays an aligned ASCII table of all available books.",
                 "Before asking 'Enter Student ID', it displays all registered active members.",
                 "Librarians can complete loans and returns without opening secondary search windows."
             ])

    add_card(slide7, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "2. 3-State Financial Machine", [
                 "Replaces naive binary overdue flags with a rigorous financial state machine.",
                 "NONE: Loan returned on time, or active loan within 7-day borrowing limit.",
                 "DUE: Book returned late; fine calculated at ₹5/day and tagged for collection.",
                 "PAID: Outstanding fine successfully collected at the circulation desk.",
                 "Guarantees financial auditability for institutional reporting."
             ])

    add_card(slide7, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "3. Dual Ledger Streams", [
                 "Active Circulation Ledger: Displays currently checked-out books with live DAYS OVERDUE and STATUS flags.",
                 "Historical Circulation Ledger: Permanent transactional archive containing timestamps, return dates, and collected fines.",
                 "Atomic Inventory Balancing: Increment and decrement operations protected by SQLite3 foreign keys and check constraints."
             ])

    # =========================================================================
    # SLIDE 8: PROJECT METHODOLOGY (Component 8)
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Development Methodology & Technology Stack", "Methodology", 8)

    add_card(slide8, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Modified Agile Iterative SDLC", [
                 "Sprint 1 — Requirement Analysis & Domain Modeling: Formulated entity classes (Book, Student, Issue) and custom exception hierarchy.",
                 "Sprint 2 — Relational Storage & Schema Migrations: Built DatabaseManager with context managers, FK enforcement, and DDL migrations.",
                 "Sprint 3 — Core Circulation Logic & Fine Engine: Developed lending, returns, dynamic ₹5/day fine calculation, and payment handlers.",
                 "Sprint 4 — Contextual CLI Views: Designed ANSI-styled ASCII table renderers and 15-choice menu dispatcher.",
                 "Sprint 5 — Test-Driven Verification & Web Extension: Engineered 54 unit tests and integrated Flask web dashboard."
             ])

    # Technology Stack Table
    tbl_shape8 = slide8.shapes.add_table(6, 3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    t8 = tbl_shape8.table
    t8.columns[0].width = Inches(1.8)
    t8.columns[1].width = Inches(1.7)
    t8.columns[2].width = Inches(2.2)

    tech_headers = ["Layer", "Technology", "Role & Rationale"]
    for c_idx, h in enumerate(tech_headers):
        cell = t8.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = DEEP_BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = CARD_BG

    tech_data = [
        ("Language", "Python 3.12+", "Core business logic, OOP encapsulation, type hints"),
        ("Database", "SQLite 3.49+", "ACID relational persistence, embedded, zero-config"),
        ("CLI Layer", "Custom View Engine", "Box-drawing Unicode tables, contextual previews"),
        ("Web Layer", "Flask 3.x / Jinja2", "Responsive web dashboard, template inheritance"),
        ("Verification", "unittest Framework", "54 automated unit tests, mock DB fixtures"),
    ]
    for r_idx, (layer, tech, role) in enumerate(tech_data, start=1):
        for c_idx, val in enumerate([layer, tech, role]):
            cell = t8.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(241, 245, 249) if r_idx % 2 == 1 else CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9)
            p.font.color.rgb = TEXT_DARK
            if c_idx == 1:
                p.font.bold = True

    # =========================================================================
    # SLIDE 9: INTERNAL STRUCTURE - ARCHITECTURE & DFD (Component 9, Part 1)
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Internal Structure: Architecture & Data Flow", "System Architecture", 9)

    add_card(slide9, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Layered Architectural Decomposition", [
                 "1. Presentation Layer:",
                 "   • Interactive Terminal CLI (views.py, main.py)",
                 "   • Responsive Flask Web GUI (app.py, templates/)",
                 "2. Service & Business Logic Layer (library.py):",
                 "   • Circulation Controller (issue_book, return_book)",
                 "   • Fine Assessment Engine (calculate_fine, pay_fine)",
                 "   • Catalog Query Engine (search_books, get_statistics)",
                 "3. Domain Model Layer (models.py):",
                 "   • Book & Student Data Classes",
                 "   • Domain Exception Hierarchy (BookNotFoundError, etc.)",
                 "4. Data Access Layer (database.py):",
                 "   • DatabaseManager with ConnectionContext",
                 "   • Automated Schema Migrator & Index Manager"
             ])

    add_card(slide9, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Data Flow & Context Boundary (CLD & DFD)", [
                 "Context Level Diagram (CLD):",
                 "   • External Entity: Librarian / Administrative User",
                 "   • System Entity: Python Library Circulation Engine",
                 "   • Inputs: Catalog entries, member registrations, loan requests",
                 "   • Outputs: Live previews, receipts, dues alerts, statistical reports",
                 "DFD Level 0 (Core Process Flow):",
                 "   • Process 1.0: Catalog & Member Registration",
                 "   • Process 2.0: Circulation & Inventory Check",
                 "   • Process 3.0: Overdue & Fine Lifecycle Management",
                 "   • Process 4.0: Financial & Audit Aggregation"
             ])

    # =========================================================================
    # SLIDE 10: INTERNAL STRUCTURE - ERD & STATE MACHINE (Component 9, Part 2)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Internal Structure: ERD & Finite State Machine", "Database & State Models", 10)

    add_card(slide10, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Entity-Relationship (ERD) Architecture", [
                 "Table 'books' (Catalog Entity):",
                 "   • PK: book_id (INTEGER AUTOINCREMENT)",
                 "   • title (TEXT), author (TEXT)",
                 "   • total_copies (INT >= 1), available_copies (INT >= 0)",
                 "Table 'students' (Member Entity):",
                 "   • PK: student_id (INTEGER AUTOINCREMENT)",
                 "   • name (TEXT), email (TEXT UNIQUE)",
                 "Table 'issues' (Circulation Junction Entity):",
                 "   • PK: issue_id (INTEGER AUTOINCREMENT)",
                 "   • FK: book_id -> books(book_id)",
                 "   • FK: student_id -> students(student_id)",
                 "   • issue_date, due_date, return_date",
                 "   • fine_amount (REAL), fine_status, status"
             ])

    add_card(slide10, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Circulation & Fine Finite State Machine", [
                 "State 1: ISSUED (Active Loan)",
                 "   • available_copies decremented by 1.",
                 "   • due_date = issue_date + 7 days.",
                 "   • fine_status initialized to 'NONE'.",
                 "State 2: RETURNED (Check-in Validation)",
                 "   • available_copies incremented by 1.",
                 "   • If return_date <= due_date: fine_status = 'NONE'.",
                 "   • If return_date > due_date: fine = (days * ₹5.00), fine_status = 'DUE'.",
                 "State 3: SETTLED (Fine Payment)",
                 "   • Librarian invokes pay_fine(issue_id).",
                 "   • fine_status transitions from 'DUE' to 'PAID'.",
                 "   • Transaction logged to payment audit trail."
             ])

    # =========================================================================
    # SLIDE 11: IMPLEMENTATION - CORE OOP & CLI (Component 10, Part 1)
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Implementation: OOP Models & Contextual CLI", "Module Implementation", 11)

    add_card(slide11, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Domain Modeling & Exception Hierarchy", [
                 "Python OOP Encapsulation:",
                 "   • Book and Student classes manage internal data validation.",
                 "   • Custom exception hierarchy rooted at LibraryError:",
                 "     - BookUnavailableError (guards zero stock)",
                 "     - AlreadyIssuedError (prevents duplicate loans)",
                 "     - BookNotIssuedError (guards invalid returns)",
                 "     - FineNotDueError (guards illegal payments)",
                 "Connection Context Manager:",
                 "   • Custom ConnectionContext class wraps sqlite3.",
                 "   • Ensures guaranteed connection closure even during unexpected runtime exceptions."
             ])

    add_card(slide11, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Contextual Terminal Interface Design", [
                 "Contextual Entity Resolution:",
                 "   • Implemented in views.py using view_issue_book().",
                 "   • Queries library.get_available_books() and prints a formatted Unicode table before prompting for Book ID.",
                 "   • Queries library.get_all_students() and displays student directory before prompting for Student ID.",
                 "Unicode Box-Drawing Aesthetics:",
                 "   • Clean ╔═══╦═══╗ tabular formatting with header separators.",
                 "   • Indian Rupee (₹) symbol support via stdout reconfiguration for Windows cp1252/cp437 terminals."
             ])

    # =========================================================================
    # SLIDE 12: IMPLEMENTATION - FINES & WEB GUI (Component 10, Part 2)
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Implementation: Fine Engine & Web Dashboard", "Module Implementation", 12)

    add_card(slide12, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Overdue Penalty Calculation Logic", [
                 "Algorithmic Implementation in library.py:",
                 "   loan_days = (return_date - issue_date).days",
                 "   overdue_days = max(0, loan_days - 7)",
                 "   fine_amount = overdue_days * 5.0",
                 "Transactional Integrity:",
                 "   • Database updates use parameterized SQL queries preventing SQL injection.",
                 "   • Schema check constraints enforce valid fine status values: CHECK(fine_status IN ('NONE', 'DUE', 'PAID')).",
                 "   • Atomic transactions ensure inventory copies and fine records update concurrently."
             ])

    add_card(slide12, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Flask Web GUI & Audit Dashboards", [
                 "Web Architecture (Library_Management_System/app.py):",
                 "   • Route '/': Dashboard with live metrics (total books, available, active loans, pending fines).",
                 "   • Route '/books': Catalog with search, add, and inventory filters.",
                 "   • Route '/issue': Dropdown-driven issue form preventing invalid ID entries.",
                 "   • Route '/return': Check-in modal displaying accrued fine calculations.",
                 "   • Route '/fines': Dedicated accounts ledger for collecting dues and auditing paid revenues."
             ])

    # =========================================================================
    # SLIDE 13: TESTING & RESULTS (Component 11)
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Testing, Verification & Empirical Results", "Verification & Testing", 13)

    # Test Case Table
    tbl_shape13 = slide13.shapes.add_table(6, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(3.4))
    t13 = tbl_shape13.table
    t13.columns[0].width = Inches(1.2)
    t13.columns[1].width = Inches(2.8)
    t13.columns[2].width = Inches(3.733)
    t13.columns[3].width = Inches(2.5)
    t13.columns[4].width = Inches(1.5)

    test_headers = ["Test ID", "Test Scenario", "Condition & Method Input", "Expected Result", "Status"]
    for c_idx, h in enumerate(test_headers):
        cell = t13.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = DEEP_BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = CARD_BG
        p.alignment = PP_ALIGN.CENTER

    test_data = [
        ("TC-01", "Stock Depletion Guard", "Issue book when available_copies == 0", "BookUnavailableError raised", "PASS"),
        ("TC-02", "Duplicate Loan Prevention", "Same student borrows identical book twice", "AlreadyIssuedError raised", "PASS"),
        ("TC-03", "Dynamic Fine Accrual", "Return book 3 days past 7-day due date", "fine=₹15.00, status='DUE'", "PASS"),
        ("TC-04", "Fine Payment Settlement", "Invoke pay_fine() on issue with fine_status='DUE'", "fine_status transitions to 'PAID'", "PASS"),
        ("TC-05", "Premature Payment Guard", "Invoke pay_fine() on issue with fine_status='NONE'", "FineNotDueError raised", "PASS"),
    ]
    for r_idx, (tid, scen, cond, exp, res) in enumerate(test_data, start=1):
        for c_idx, val in enumerate([tid, scen, cond, exp, res]):
            cell = t13.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(241, 245, 249) if r_idx % 2 == 1 else CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9)
            p.font.color.rgb = TEXT_DARK
            if c_idx == 0:
                p.font.bold = True
                p.alignment = PP_ALIGN.CENTER
            elif c_idx == 4:
                p.font.bold = True
                p.font.color.rgb = SUCCESS_GREEN
                p.alignment = PP_ALIGN.CENTER

    add_card(slide13, Inches(0.8), Inches(5.2), Inches(11.733), Inches(1.8),
             "Test Execution Summary & Benchmarks", [
                 "Test Suite Results: Ran 54 unit tests across 7 test suites in 4.239 seconds with 100% pass rate (0 failures, 0 errors).",
                 "Coverage Breadth: Book management, student registry, active loans, return inventory balancing, overdue fines, payment audit, and statistics.",
                 "Query Performance: Indexed lookups on books(title, author) and issues(status, fine_status) executed in under 2.5 milliseconds."
             ])

    # =========================================================================
    # SLIDE 14: CONCLUSION (Component 12)
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Conclusion & Project Achievements", "Project Evaluation", 14)

    add_card(slide14, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Fulfillment of Objectives", [
                 "Successful Automation: Completely eliminated manual register paper logs and arbitrary ledger calculations.",
                 "User-Centric Breakthrough: The Contextual Preview mechanism solved the CLI identifier memorization bottleneck.",
                 "Relational Rigor: Deployed an ACID-compliant SQLite3 schema with automatic migrations and foreign key cascades.",
                 "Financial Transparency: Established a robust 3-state fine lifecycle ensuring complete institutional revenue accountability.",
                 "Architectural Scalability: Decoupled service architecture allows simultaneous CLI and Flask web operation."
             ])

    add_card(slide14, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Educational & Academic Value", [
                 "Object-Oriented Design: Practical application of inheritance, encapsulation, custom exception hierarchies, and domain models.",
                 "Database Engineering: Hands-on mastery of relational normalization, compound indexes, constraints, and migration scripts.",
                 "Defensive Programming: Rigorous input validation, error handling, and 100% automated test verification.",
                 "Independent Engineering: Rigorous end-to-end design, implementation, and automated test suite verification in accordance with Brainware University MCA curriculum."
             ])

    # =========================================================================
    # SLIDE 15: FUTURE SCOPE & REFERENCES (Components 13 & 14)
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_header(slide15, "Future Scope & Academic References", "Roadmap & Citations", 15)

    add_card(slide15, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
             "Future Scope & Roadmap Enhancements", [
                 "Barcode & RFID Integration: Instant scanning of book ISBNs and student ID cards via USB/Bluetooth hardware.",
                 "Automated SMS & Email Alerts: Push notifications for upcoming loan due dates and overdue fine warnings.",
                 "UPI QR Code Fine Payments: Dynamic BharatQR generation on return screens for direct contactless fee settlement.",
                 "Cloud Synchronization & Multi-Branch: Optional REST API synchronization across multiple departmental libraries.",
                 "AI-Powered Book Recommendations: Collaborative filtering based on historical student borrowing trends."
             ])

    add_card(slide15, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
             "Academic & Technical References", [
                 "[1] Python Software Foundation (2026) 'sqlite3 — DB-API 2.0 interface for SQLite databases', Python 3.12 Documentation.",
                 "[2] Lutz, Mark (2013) 'Learning Python: Powerful Object-Oriented Programming', 5th Edition, O'Reilly Media.",
                 "[3] Pressman, R. S. and Maxim, B. R. (2020) 'Software Engineering: A Practitioner's Approach', 9th Edition, McGraw-Hill.",
                 "[4] Owens, M. and Allen, G. (2010) 'The Definitive Guide to SQLite', 2nd Edition, Apress.",
                 "[5] Brainware University (2026) 'Guidelines for MCA Academic Project Documentation & Presentation', Department of Computational Sciences.",
                 "[6] Pallets Projects (2024) 'Flask: A lightweight WSGI web application framework', Pallets Docs."
             ])

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
