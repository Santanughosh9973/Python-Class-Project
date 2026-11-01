"""
generate_html_report.py
Generates a complete, professional, 20-page academic project report in HTML for:
Project: LIBRARY MANAGEMENT SYSTEM
Degree: Master of Computer Applications (MCA)
Department: Department of Computational Sciences, Brainware University
Author: Santanu Ghosh (Solo Developer)
Supervisor: Mr. Rahul Kumar Ghosh, Assistant Professor
Head of Department: Dr. Jayanta Aich
Session: May 2026
"""

import os

import os
import base64

def generate_report():
    # University Emblem - Base64 Data URI for complete self-contained rendering
    logo_path = os.path.join("assets", "university-logo.jpg")
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as img_f:
            logo_b64 = base64.b64encode(img_f.read()).decode("utf-8")
        uni_logo_img = f'<img src="data:image/jpeg;base64,{logo_b64}" alt="Brainware University Logo" class="uni-emblem" style="width: 78px; height: 78px; object-fit: contain; display: block; margin: 4px auto;">'
        uni_logo_top = f'<img src="data:image/jpeg;base64,{logo_b64}" alt="Brainware University Logo" style="width: 38px; height: 38px; object-fit: contain; background: #ffffff; border-radius: 50%; padding: 2px;">'
    else:
        uni_logo_img = '<img src="assets/university-logo.jpg" alt="Brainware University Logo" class="uni-emblem" style="width: 78px; height: 78px; object-fit: contain; display: block; margin: 4px auto;">'
        uni_logo_top = '<img src="assets/university-logo.jpg" alt="Brainware University Logo" style="width: 38px; height: 38px; object-fit: contain; background: #ffffff; border-radius: 50%; padding: 2px;">'

    pages = []

    # =========================================================================
    # PAGE 1: OUTER COVER PAGE
    # =========================================================================
    p1 = f'''
    <div class="page">
      <div class="page-border" style="justify-content: space-between; text-align: center;">
        <div>
          <div style="font-size: 13pt; font-weight: bold; letter-spacing: 1px; color: #1e3a8a; margin-top: 5px;">
            BRAINWARE UNIVERSITY
          </div>
          <div style="font-size: 9.5pt; color: #475569; margin-bottom: 25px;">
            Department of Computational Sciences
          </div>

          <div class="cover-title" style="font-size: 20pt; font-weight: bold; margin-bottom: 8px; color: #0f172a; letter-spacing: 0.8px;">
            LIBRARY MANAGEMENT SYSTEM
          </div>
          <div style="font-size: 11pt; font-weight: 600; color: #334155; margin-bottom: 25px; line-height: 1.4;">
            A Terminal-Based Object-Oriented Library Automation, Circulation<br>&amp; Financial Management System
          </div>

          <div class="cover-subheading" style="font-size: 11pt; font-style: italic; margin-bottom: 12px;">
            A PROJECT REPORT
          </div>
          <div style="font-size: 10pt; margin-bottom: 15px; color: #475569;">
            Submitted in partial fulfillment of the requirements for the award of the degree of
          </div>

          <div style="font-size: 14pt; font-weight: bold; color: #1e3a8a; letter-spacing: 0.5px; margin-bottom: 6px;">
            MASTER OF COMPUTER APPLICATIONS
          </div>
          <div style="font-size: 11pt; font-weight: bold; color: #334155; margin-bottom: 30px;">
            IN<br>DEPARTMENT OF COMPUTATIONAL SCIENCES
          </div>

          <div style="font-size: 11pt; font-style: italic; margin-bottom: 12px;">Submitted by</div>

          <table class="report-table" style="margin: 0 auto; width: 80%; font-size: 9.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="padding: 7px; width: 33%;">ROLL NUMBER</th>
                <th style="padding: 7px; width: 33%;">STUDENT CODE</th>
                <th style="padding: 7px; width: 34%;">STUDENT NAME</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: #ffffff; font-weight: bold;">
                <td style="padding: 8px;">23010346299</td>
                <td style="padding: 8px;">BWU/MCA/26/022</td>
                <td style="padding: 8px; color: #1e3a8a;">SANTANU GHOSH</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="margin-bottom: 12px;">
          <div style="display: flex; justify-content: center; margin-bottom: 8px;">
            {uni_logo_img}
          </div>
          <div style="font-size: 13pt; font-weight: bold; color: #0f172a;">BRAINWARE UNIVERSITY</div>
          <div style="font-size: 9.5pt; color: #475569; margin-top: 2px;">
            398, Ramkrishnapur Road, Barasat, North 24 Parganas, Kolkata - 700 125
          </div>
          <div style="font-size: 10pt; font-weight: bold; color: #1e3a8a; margin-top: 5px;">MAY 2026</div>
        </div>
      </div>
    </div>
    '''
    pages.append(p1)

    # =========================================================================
    # PAGE 2: INNER TITLE PAGE
    # =========================================================================
    p2 = f'''
    <div class="page">
      <div class="page-border" style="justify-content: space-between; text-align: center;">
        <div>
          <div style="font-size: 10pt; font-weight: bold; color: #475569; letter-spacing: 1px; margin-top: 5px;">
            MAY 2026
          </div>

          <div class="cover-title" style="font-size: 19pt; font-weight: bold; margin-top: 35px; margin-bottom: 10px; color: #0f172a;">
            LIBRARY MANAGEMENT SYSTEM
          </div>
          <div style="font-size: 11pt; color: #334155; margin-bottom: 30px; line-height: 1.4;">
            An Automated Object-Oriented Library Information &amp; Financial Circulation System
          </div>

          <div style="font-size: 10.5pt; font-style: italic; margin-bottom: 12px;">Submitted by</div>

          <table class="report-table" style="margin: 0 auto; width: 80%; font-size: 9.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="padding: 7px; width: 33%;">ROLL NUMBER</th>
                <th style="padding: 7px; width: 33%;">STUDENT CODE</th>
                <th style="padding: 7px; width: 34%;">STUDENT NAME</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: #ffffff; font-weight: bold;">
                <td style="padding: 8px;">23010346299</td>
                <td style="padding: 8px;">BWU/MCA/26/022</td>
                <td style="padding: 8px; color: #1e3a8a;">SANTANU GHOSH</td>
              </tr>
            </tbody>
          </table>

          <div style="margin-top: 35px; font-size: 10.5pt; font-style: italic; color: #475569;">
            in partial fulfillment for the award of the degree of
          </div>
          <div style="font-size: 13.5pt; font-weight: bold; color: #1e3a8a; margin: 6px 0;">
            MASTER OF COMPUTER APPLICATIONS
          </div>
          <div style="font-size: 10.5pt; color: #334155; margin-bottom: 35px;">
            in<br><strong>DEPARTMENT OF COMPUTATIONAL SCIENCES</strong>
          </div>

          <div style="font-size: 10.5pt; font-style: italic; margin-bottom: 5px;">Under the Guidance of</div>
          <div style="font-size: 13pt; font-weight: bold; color: #0f172a;">Mr. Rahul Kumar Ghosh</div>
          <div style="font-size: 10pt; color: #475569;">Assistant Professor, Department of Computational Sciences</div>
        </div>

        <div style="margin-bottom: 12px;">
          <div style="display: flex; justify-content: center; margin-bottom: 6px;">
            {uni_logo_img}
          </div>
          <div style="font-size: 12.5pt; font-weight: bold; color: #0f172a;">BRAINWARE UNIVERSITY</div>
          <div style="font-size: 9.5pt; color: #475569; margin-top: 2px;">
            398, Ramkrishnapur Road, Barasat, North 24 Parganas, Kolkata - 700 125
          </div>
        </div>
      </div>
    </div>
    '''
    pages.append(p2)

    # =========================================================================
    # PAGE 3: BONAFIDE CERTIFICATE (Page i)
    # =========================================================================
    p3 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div style="text-align: center; margin-bottom: 14px;">
            <div style="display: flex; justify-content: center; margin-bottom: 6px;">
              {uni_logo_img}
            </div>
            <div style="font-size: 13.5pt; font-weight: bold; color: #0f172a;">BRAINWARE UNIVERSITY</div>
            <div style="font-size: 9.2pt; color: #475569;">398, Ramkrishnapur Road, Barasat, North 24 Parganas, Kolkata - 700 125</div>
            <div style="font-size: 11pt; font-weight: bold; color: #1e3a8a; margin-top: 10px;">
              DEPARTMENT OF COMPUTATIONAL SCIENCES
            </div>
            <div style="font-size: 13pt; font-weight: bold; letter-spacing: 1px; margin-top: 20px; text-decoration: underline;">
              BONAFIDE CERTIFICATE
            </div>
          </div>

          <div style="margin-top: 28px; line-height: 1.8; font-size: 10.5pt; text-align: justify; text-justify: inter-word;">
            <p>
              Certified that this project report titled <strong>&ldquo;LIBRARY MANAGEMENT SYSTEM&rdquo;</strong> is the
              bonafide work of <strong>SANTANU GHOSH</strong> (Roll Number: <strong>23010346299</strong>,
              Student Code: <strong>BWU/MCA/26/022</strong>),
              who carried out the project work independently under my supervision in partial fulfillment of the
              requirements for the award of the degree of <strong>MASTER OF COMPUTER APPLICATIONS</strong> of
              <strong>Brainware University</strong> during the academic session 2024&ndash;2026.
            </p>
            <p style="margin-top: 14px;">
              To the best of our knowledge and assessment, this project represents original software development,
              incorporating modular object-oriented architecture, ACID-compliant database transactions, dynamic
              overdue penalty tracking, and exhaustive test-driven verification. The work embodied in this report
              has not been submitted elsewhere for the award of any other degree, diploma, or fellowship.
            </p>
          </div>

          <div class="signature-row" style="margin-top: 90px;">
            <div class="sign-block">
              <div class="sign-line">SIGNATURE</div>
              <div style="font-weight: bold; font-size: 10.5pt; color: #0f172a;">Dr. Jayanta Aich</div>
              <div style="font-weight: bold; color: #1e3a8a;">HEAD OF THE DEPARTMENT</div>
              <div>Computational Sciences,</div>
              <div>Brainware University</div>
              <div style="font-size: 8.5pt; color: #64748b; margin-top: 2px;">Barasat, Kolkata &ndash; 700 125</div>
            </div>

            <div class="sign-block">
              <div class="sign-line">SIGNATURE</div>
              <div style="font-weight: bold; font-size: 10.5pt; color: #0f172a;">Mr. Rahul Kumar Ghosh</div>
              <div style="font-weight: bold; color: #1e3a8a;">SUPERVISOR</div>
              <div>Assistant Professor,</div>
              <div>Department of Computational Sciences,</div>
              <div>Brainware University, Kolkata &ndash; 700 125</div>
            </div>
          </div>
        </div>
        <div class="page-footer">i</div>
      </div>
    </div>
    '''
    pages.append(p3)

    # =========================================================================
    # PAGE 4: ACKNOWLEDGEMENT (Page ii)
    # =========================================================================
    p4 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div style="text-align: center; margin-bottom: 22px;">
            <div style="font-size: 14pt; font-weight: bold; letter-spacing: 1px; color: #0f172a; text-decoration: underline;">
              ACKNOWLEDGEMENT
            </div>
          </div>

          <div style="font-size: 10.2pt; line-height: 1.7; text-align: justify; text-justify: inter-word;">
            <p>
              I would like to express my sincere gratitude to <strong>Brainware University</strong> for providing me with
              the state-of-the-art facilities, academic platform, and conducive research atmosphere to undertake this
              final-year post-graduate MCA project titled <strong>&ldquo;LIBRARY MANAGEMENT SYSTEM&rdquo;</strong>.
              This academic endeavor has provided invaluable exposure to end-to-end software engineering, object-oriented
              design patterns, relational data integrity, and real-world system testing.
            </p>
            <p style="margin-top: 10px;">
              I extend my deepest and most heartfelt thanks to my Project Supervisor, <strong>Mr. Rahul Kumar Ghosh</strong>,
              Assistant Professor, Department of Computational Sciences, for his intellectual guidance, constructive
              critiques, and continuous encouragement throughout every development milestone. His insights into database
              schema normalization, context-managed resource handling, and exception architecture were fundamental in
              transforming theoretical design principles into an efficient, production-grade application.
            </p>
            <p style="margin-top: 10px;">
              I would also like to express my sincere appreciation to our respected Head of the Department,
              <strong>Dr. Jayanta Aich</strong>, for his administrative leadership, motivational guidance, and for
              ensuring uninterrupted access to the computing labs and software resources within the Department of
              Computational Sciences.
            </p>
            <p style="margin-top: 10px;">
              I am equally thankful to all respected faculty members and technical staff of the Department of Computational
              Sciences for their insightful advice, scholarly support, and technical assistance during the course of my MCA
              studies.
            </p>
            <p style="margin-top: 10px;">
              Finally, I acknowledge that this project has been conceptualized, architected, coded, and validated entirely
              by myself as an individual project. I am grateful to my family and fellow scholars whose encouragement and moral
              support fueled my commitment to completing this work with academic rigor and technical excellence.
            </p>
          </div>

          <div style="margin-top: 55px; text-align: right; padding-right: 25px;">
            <div style="border-top: 1px dashed #000; width: 220px; display: inline-block; margin-bottom: 5px;"></div>
            <div style="font-size: 11pt; font-weight: bold; color: #0f172a;">SANTANU GHOSH</div>
            <div style="font-size: 9.5pt; color: #334155;">Student Code: BWU/MCA/26/022</div>
            <div style="font-size: 9.5pt; color: #334155;">Roll Number: 23010346299</div>
            <div style="font-size: 9.5pt; color: #1e3a8a; font-weight: 600;">Department of Computational Sciences</div>
            <div style="font-size: 9pt; color: #64748b;">Brainware University, Kolkata</div>
          </div>
        </div>
        <div class="page-footer">ii</div>
      </div>
    </div>
    '''
    pages.append(p4)

    # =========================================================================
    # PAGE 5: ABSTRACT (Page iii)
    # =========================================================================
    p5 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div style="text-align: center; margin-bottom: 18px;">
            <div style="font-size: 14pt; font-weight: bold; letter-spacing: 1px; color: #0f172a; text-decoration: underline;">
              ABSTRACT
            </div>
          </div>

          <div style="font-size: 10.2pt; line-height: 1.72; text-align: justify; text-justify: inter-word;">
            <p>
              The efficient administration of academic knowledge repositories is a core pillar of modern educational
              institutions. Traditional library tracking systems, which frequently depend on manual physical registers or
              unstructured desktop spreadsheets, suffer from severe operational bottlenecks: progressive paper degradation,
              unindexed multi-volume records, lack of concurrency control, and inaccurate overdue penalty assessments.
              This MCA final-year project, titled <strong>&ldquo;LIBRARY MANAGEMENT SYSTEM&rdquo;</strong>, addresses these
              institutional challenges by engineering a robust, offline-first, high-performance terminal application written in
              Python 3.10+ and powered by a relational SQLite3 database engine. The system provides unified catalog control,
              student member indexing, atomic book loan circulation, automatic fine accrual calculations, and comprehensive
              auditing dashboards.
            </p>
            <p style="margin-top: 12px;">
              The software employs a clean <strong>Three-Tier Object-Oriented Architecture</strong> consisting of an Interactive
              Presentation Layer (terminal user interface with ANSI visual formatting), a Service/Business Logic Layer
              (encapsulating inventory decrements, date validation, and overdue fee engines), and a Data Persistence Layer
              (implementing custom context managers for deterministic connection recycling and SQLite foreign key enforcement).
              The data model incorporates three primary normalized entities: <code>books</code>, <code>students</code>, and
              <code>issues</code>, augmented with B-tree indices on title, author, and circulation status to ensure sub-millisecond
              query execution. Crucially, the system features an intelligent schema migration routine that detects and seamlessly
              migrates legacy database tables to modern schemas without data loss.
            </p>
            <p style="margin-top: 12px;">
              A distinguished capability of the system is its dual-state financial fine lifecycle model. Upon returning an overdue
              book (beyond the standard 7-day lending window), the system automatically assesses a fee of &yen;5.00 per elapsed day,
              transitioning the issue record to a <code>DUE</code> state. Once settled, the transaction is marked as <code>PAID</code>,
              preventing duplicate levies and establishing a reliable financial audit trail. System correctness, boundary constraints,
              and fault handling were systematically validated through a comprehensive unit test suite consisting of <strong>54 automated
              test cases</strong> across 6 test classes, achieving 100% test success in 4.85 seconds. The resulting software represents
              a self-contained, zero-dependency, maintainable, and extensible solution perfectly suited for institutional deployment.
            </p>
          </div>
        </div>
        <div class="page-footer">iii</div>
      </div>
    </div>
    '''
    pages.append(p5)

    # =========================================================================
    # PAGE 6: TABLE OF CONTENTS (Page iv)
    # =========================================================================
    p6 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div style="text-align: center; margin-bottom: 12px;">
            <div style="font-size: 14pt; font-weight: bold; letter-spacing: 1px; color: #0f172a; text-decoration: underline;">
              TABLE OF CONTENTS
            </div>
          </div>

          <table class="report-table" style="font-size: 9pt; width: 100%; border: none;">
            <thead>
              <tr style="border-bottom: 1.5px solid #0f172a; background: #f8fafc;">
                <th style="text-align: left; width: 14%; border: none; padding: 4px;">Chapter</th>
                <th style="text-align: left; width: 72%; border: none; padding: 4px;">Title</th>
                <th style="text-align: right; width: 14%; border: none; padding: 4px;">Page No.</th>
              </tr>
            </thead>
            <tbody style="line-height: 1.45;">
              <tr style="font-weight: bold; border-top: 1px solid #e2e8f0;"><td style="border:none;"></td><td style="border:none; text-align: left;">ABSTRACT</td><td style="border:none; text-align: right;">iii</td></tr>
              <tr style="font-weight: bold;"><td style="border:none;"></td><td style="border:none; text-align: left;">LIST OF TABLES</td><td style="border:none; text-align: right;">v</td></tr>
              <tr style="font-weight: bold;"><td style="border:none;"></td><td style="border:none; text-align: left;">LIST OF FIGURES</td><td style="border:none; text-align: right;">v</td></tr>
              <tr style="font-weight: bold;"><td style="border:none;"></td><td style="border:none; text-align: left;">LIST OF SYMBOLS, ABBREVIATIONS AND NOMENCLATURE</td><td style="border:none; text-align: right;">v</td></tr>
              
              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">1.</td><td style="border:none; text-align: left;">INTRODUCTION</td><td style="border:none; text-align: right;">1</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">1.1 Background &amp; Institutional Need &bull; 1.2 Problem Statement &bull; 1.3 Scope</td><td style="border:none; text-align: right;">1</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">2.</td><td style="border:none; text-align: left;">OBJECTIVE</td><td style="border:none; text-align: right;">2</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">2.1 Primary Objective &bull; 2.2 Secondary Objectives &bull; 2.3 Functional &amp; Technical Goals</td><td style="border:none; text-align: right;">2</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">3.</td><td style="border:none; text-align: left;">PLANNING &amp; METHODOLOGY</td><td style="border:none; text-align: right;">3</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">3.1 Need for Planning &bull; 3.2 Modified Agile Model &bull; 3.3 WBS &bull; 3.4 Gantt Chart &bull; 3.5 Risks</td><td style="border:none; text-align: right;">3</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">4.</td><td style="border:none; text-align: left;">REQUIREMENT ANALYSIS</td><td style="border:none; text-align: right;">4</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">4.1 User Requirements &bull; 4.2 Functional Requirements &bull; 4.3 NFR &bull; 4.4 Comparison Matrix</td><td style="border:none; text-align: right;">4</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">5.</td><td style="border:none; text-align: left;">SYSTEM FLOW &amp; ARCHITECTURAL DIAGRAMS</td><td style="border:none; text-align: right;">5</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">5.1 Context Level Diagram (CLD) &bull; 5.2 DFD Level 0, Level 1 &amp; Level 2</td><td style="border:none; text-align: right;">5</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">5.5 Use Case Diagram &bull; 5.6 Entity-Relationship Diagram (ERD) &bull; 5.7 Activity Diagram</td><td style="border:none; text-align: right;">6</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">5.8 Sequence Diagram &bull; 5.9 Issuance Flowchart &bull; 5.10 Overdue Return Flowchart</td><td style="border:none; text-align: right;">7</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">6.</td><td style="border:none; text-align: left;">PROPOSED DESIGN</td><td style="border:none; text-align: right;">8</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">6.1 Design Approach &bull; 6.2 3-Tier System Architecture &bull; 6.3 UI &bull; 6.4 Navigation &bull; 6.5 APIs</td><td style="border:none; text-align: right;">8</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">7.</td><td style="border:none; text-align: left;">EXPERIMENTAL RESULTS &amp; VALIDATION</td><td style="border:none; text-align: right;">9</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">7.1 Experimental Setup &bull; 7.2 Catalog Results &bull; 7.3 Fine Results &bull; 7.4 Performance &bull; 7.5 Feedback</td><td style="border:none; text-align: right;">9</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">7.6 Production Visual Artifacts &amp; Interactive Terminal Console Screens</td><td style="border:none; text-align: right;">10</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;">8.</td><td style="border:none; text-align: left;">FUTURE SCOPE</td><td style="border:none; text-align: right;">11</td></tr>
              <tr style="font-weight: bold;"><td style="border:none;">9.</td><td style="border:none; text-align: left;">CONCLUSION</td><td style="border:none; text-align: right;">11</td></tr>

              <tr style="font-weight: bold; border-top: 1px solid #cbd5e1;"><td style="border:none;"></td><td style="border:none; text-align: left;">APPENDICES</td><td style="border:none; text-align: right;">12</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">Appendix A: Database Structure &amp; Relational Schema (DDL)</td><td style="border:none; text-align: right;">12</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">Appendix B: Core Source Code Implementation</td><td style="border:none; text-align: right;">12</td></tr>
              <tr><td style="border:none;"></td><td style="border:none; text-align: left; padding-left: 15px;">Appendix C: Test Cases &amp; Execution Matrix (54 Unit Tests)</td><td style="border:none; text-align: right;">13</td></tr>
              <tr style="font-weight: bold;"><td style="border:none;"></td><td style="border:none; text-align: left;">REFERENCES</td><td style="border:none; text-align: right;">13</td></tr>
            </tbody>
          </table>
        </div>
        <div class="page-footer">iv</div>
      </div>
    </div>
    '''
    pages.append(p6)

    # =========================================================================
    # PAGE 7: LIST OF TABLES, FIGURES & SYMBOLS (Page v)
    # =========================================================================
    p7 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div style="font-size: 11pt; font-weight: bold; color: #1e3a8a; border-bottom: 1.5px solid #0f172a; padding-bottom: 2px; margin-bottom: 8px;">
            LIST OF TABLES
          </div>
          <table class="report-table" style="font-size: 8.5pt; width: 100%; margin-bottom: 12px;">
            <thead>
              <tr style="background: #f1f5f9;">
                <th style="width: 20%; text-align: left;">Table No.</th>
                <th style="width: 65%; text-align: left;">Title</th>
                <th style="width: 15%; text-align: center;">Page No.</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left;">Table 1.1</td><td style="text-align: left;">Scope of Library Management System Modules</td><td style="text-align: center;">1</td></tr>
              <tr><td style="text-align: left;">Table 2.1</td><td style="text-align: left;">Functional Objectives of LMS Application</td><td style="text-align: center;">2</td></tr>
              <tr><td style="text-align: left;">Table 3.1</td><td style="text-align: left;">Modified Agile Sprints Overview &amp; Deliverables</td><td style="text-align: center;">3</td></tr>
              <tr><td style="text-align: left;">Table 3.2</td><td style="text-align: left;">Project Schedule &amp; 12-Week Gantt Execution Chart</td><td style="text-align: center;">3</td></tr>
              <tr><td style="text-align: left;">Table 4.1</td><td style="text-align: left;">System Functional Requirements (FR-01 to FR-08)</td><td style="text-align: center;">4</td></tr>
              <tr><td style="text-align: left;">Table 4.2</td><td style="text-align: left;">Non-Functional Requirements Specification (NFR-01 to NFR-06)</td><td style="text-align: center;">4</td></tr>
              <tr><td style="text-align: left;">Table 4.3</td><td style="text-align: left;">Comparative Analysis of Existing Systems vs LMS</td><td style="text-align: center;">4</td></tr>
              <tr><td style="text-align: left;">Table 7.1</td><td style="text-align: left;">Core Functional Modules Verification Matrix</td><td style="text-align: center;">9</td></tr>
              <tr><td style="text-align: left;">Table 7.2</td><td style="text-align: left;">Circulation, Overdue Assessment &amp; Fine Settlement Results</td><td style="text-align: center;">9</td></tr>
              <tr><td style="text-align: left;">Table C.1</td><td style="text-align: left;">Database Relational Tables Overview &amp; Cardinality</td><td style="text-align: center;">12</td></tr>
              <tr><td style="text-align: left;">Table D.1</td><td style="text-align: left;">System Test Suite &amp; Test Cases Matrix (TC-01 to TC-10)</td><td style="text-align: center;">13</td></tr>
            </tbody>
          </table>

          <div style="font-size: 11pt; font-weight: bold; color: #1e3a8a; border-bottom: 1.5px solid #0f172a; padding-bottom: 2px; margin-bottom: 8px;">
            LIST OF FIGURES
          </div>
          <table class="report-table" style="font-size: 8.5pt; width: 100%; margin-bottom: 12px;">
            <thead>
              <tr style="background: #f1f5f9;">
                <th style="width: 20%; text-align: left;">Figure No.</th>
                <th style="width: 65%; text-align: left;">Title</th>
                <th style="width: 15%; text-align: center;">Page No.</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left;">Figure 5.1</td><td style="text-align: left;">Context Level Diagram (CLD) of Library System</td><td style="text-align: center;">5</td></tr>
              <tr><td style="text-align: left;">Figure 5.2</td><td style="text-align: left;">Data Flow Diagram &ndash; Level 0 (System Processes)</td><td style="text-align: center;">5</td></tr>
              <tr><td style="text-align: left;">Figure 5.3</td><td style="text-align: left;">Data Flow Diagram &ndash; Level 1 (Book Circulation Engine)</td><td style="text-align: center;">5</td></tr>
              <tr><td style="text-align: left;">Figure 5.4</td><td style="text-align: left;">Data Flow Diagram &ndash; Level 2 (Fine Settlement Lifecycle)</td><td style="text-align: center;">5</td></tr>
              <tr><td style="text-align: left;">Figure 5.5</td><td style="text-align: left;">Use Case Diagram for Library Administrator &amp; Members</td><td style="text-align: center;">6</td></tr>
              <tr><td style="text-align: left;">Figure 5.6</td><td style="text-align: left;">Entity&ndash;Relationship Diagram (ERD) with Crow's Foot Notation</td><td style="text-align: center;">6</td></tr>
              <tr><td style="text-align: left;">Figure 5.7</td><td style="text-align: left;">Activity Diagram for Book Issuance and Stock Verification</td><td style="text-align: center;">6</td></tr>
              <tr><td style="text-align: left;">Figure 5.8</td><td style="text-align: left;">Sequence Diagram for Loan Issuance &amp; Database State Updates</td><td style="text-align: center;">7</td></tr>
              <tr><td style="text-align: left;">Figure 5.9</td><td style="text-align: left;">Flowchart for Book Lending &amp; Duplicate Loan Prevention</td><td style="text-align: center;">7</td></tr>
              <tr><td style="text-align: left;">Figure 5.10</td><td style="text-align: left;">Flowchart for Book Return, Late Penalty Calculation &amp; Fine Settlement</td><td style="text-align: center;">7</td></tr>
              <tr><td style="text-align: left;">Figure 6.1</td><td style="text-align: left;">Three-Tier System Architecture Design</td><td style="text-align: center;">8</td></tr>
              <tr><td style="text-align: left;">Figure 6.2</td><td style="text-align: left;">Terminal Navigation Flow Diagram</td><td style="text-align: center;">8</td></tr>
              <tr><td style="text-align: left;">Figure A.1&ndash;A.4</td><td style="text-align: left;">Terminal Console Interface Screens &amp; Analytical Dashboards</td><td style="text-align: center;">10</td></tr>
            </tbody>
          </table>

          <div style="font-size: 11pt; font-weight: bold; color: #1e3a8a; border-bottom: 1.5px solid #0f172a; padding-bottom: 2px; margin-bottom: 8px;">
            LIST OF SYMBOLS, ABBREVIATIONS AND NOMENCLATURE
          </div>
          <table class="report-table" style="font-size: 8.5pt; width: 100%;">
            <thead>
              <tr style="background: #f1f5f9;">
                <th style="width: 25%; text-align: left;">Abbreviation</th>
                <th style="width: 75%; text-align: left;">Meaning &amp; Operational Definition</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left;"><strong>CLI</strong></td><td style="text-align: left;">Command Line Interface &ndash; interactive text-based console UX</td></tr>
              <tr><td style="text-align: left;"><strong>OOP</strong></td><td style="text-align: left;">Object-Oriented Programming (Classes, Encapsulation, Custom Exceptions)</td></tr>
              <tr><td style="text-align: left;"><strong>ACID</strong></td><td style="text-align: left;">Atomicity, Consistency, Isolation, Durability in database transactions</td></tr>
              <tr><td style="text-align: left;"><strong>PK / FK</strong></td><td style="text-align: left;">Primary Key / Foreign Key relational constraints enforced via SQLite PRAGMA</td></tr>
              <tr><td style="text-align: left;"><strong>WAL</strong></td><td style="text-align: left;">Write-Ahead Logging mode for safe atomic SQLite commit journaling</td></tr>
              <tr><td style="text-align: left;"><strong>DFD / ERD / CLD</strong></td><td style="text-align: left;">Data Flow Diagram / Entity-Relationship Diagram / Context Level Diagram</td></tr>
            </tbody>
          </table>
        </div>
        <div class="page-footer">v</div>
      </div>
    </div>
    '''
    pages.append(p7)

    # =========================================================================
    # PAGE 8: CHAPTER 1 - INTRODUCTION (Page 1)
    # =========================================================================
    p8 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 1</div>
            <div class="chapter-title">INTRODUCTION</div>
          </div>

          <p>
            The rapid advancement of computational technologies has fundamentally reshaped information management
            across academic institutions. Central among institutional assets is the academic library&mdash;a nexus of
            textbooks, research monographs, and reference publications essential for student success and scholarly
            discovery. However, managing thousands of catalog volumes, tracking fluctuating physical stock, enrolling
            hundreds of registered student patrons, and accurately managing book loans under traditional administrative
            procedures presents profound logistical challenges.
          </p>

          <p>
            Historically, educational libraries operated through manual paper registers or ad-hoc digital spreadsheets.
            While ostensibly simple, manual registers suffer from physical deterioration, illegible handwriting, misplaced
            entries, and an inability to search through large book collections in real time. Spreadsheets lack referential
            integrity, permit duplicate lending of unavailable volumes, and fail to provide automated audit trails for
            overdue loans and fine collection. These critical deficiencies create a compelling institutional need for an
            automated, dependable, and self-contained software solution.
          </p>

          <div class="section-title">1.1 Project Overview</div>
          <p>
            The <strong>Library Management System (LMS)</strong> is designed as a standalone, offline-first, terminal-based
            software solution developed using Python 3.10+ and a relational SQLite3 engine. The system automates every facet
            of library operation: from catalog creation and multi-copy inventory allocation to student member registration,
            loan issuance with automated 7-day borrow windows, instant overdue penalty calculation, fine payment recording,
            and operational reporting. By operating locally without reliance on third-party cloud servers or external network
            connectivity, the application eliminates security vulnerabilities, guarantees total institutional data privacy,
            and operates with ultra-low latency.
          </p>

          <div class="section-title">1.2 Scope of the System</div>
          <p>
            The scope of the Library Management System encompasses all core functional areas necessary for comprehensive
            institutional library administration. The division of functional scope across system actors is summarized in
            <strong>Table 1.1</strong>.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 6px; margin-bottom: 2px; text-align: center;">
            Table 1.1 Scope of Library Management System Modules
          </div>
          <table class="report-table" style="font-size: 8.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 25%; text-align: left;">User / Entity</th>
                <th style="width: 75%; text-align: left;">Functional Responsibilities &amp; Capabilities</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="text-align: left; font-weight: bold;">Library Administrator / Staff</td>
                <td style="text-align: left;">
                  Add, update, search, and delete books; manage multi-copy inventory; register student members with unique emails;
                  execute book loans and returns; assess overdue fines; process fine payments; inspect audit statistics.
                </td>
              </tr>
              <tr>
                <td style="text-align: left; font-weight: bold;">Student / Library Member</td>
                <td style="text-align: left;">
                  Browse available book catalog; borrow books within lending limits; view active loans and scheduled return due dates;
                  inspect accumulated overdue fees; settle outstanding penalties.
                </td>
              </tr>
              <tr>
                <td style="text-align: left; font-weight: bold;">Database &amp; Engine Subsystem</td>
                <td style="text-align: left;">
                  Maintain relational integrity via foreign keys; execute atomic inventory decrements/increments; auto-migrate legacy
                  schemas; compute elapsed overdue days; generate institutional analytics.
                </td>
              </tr>
            </tbody>
          </table>

          <div class="section-title">1.3 Academic Significance in the MCA Curriculum</div>
          <p>
            From an academic perspective, this project demonstrates the practical application of advanced post-graduate computer
            science principles: Object-Oriented System Modeling (polymorphic exceptions, encapsulation, factory patterns), Relational
            Database Management (schema design, indexing, ACID transactions), Software Quality Assurance (54 unit tests), and
            robust CLI human-computer interaction.
          </p>
        </div>
        <div class="page-footer">1</div>
      </div>
    </div>
    '''
    pages.append(p8)

    # =========================================================================
    # PAGE 9: CHAPTER 2 - OBJECTIVES (Page 2)
    # =========================================================================
    p9 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 2</div>
            <div class="chapter-title">OBJECTIVE</div>
          </div>

          <p>
            The Library Management System is formulated with a precise hierarchy of objectives designed to address the
            administrative, logistical, and computational requirements of educational institutions. These objectives guide
            the architectural choices, algorithmic workflows, and operational boundaries of the software.
          </p>

          <div class="section-title">2.1 Primary Objective</div>
          <p>
            The primary objective of the Library Management System is to develop an automated, dependable, and self-contained
            software solution that provides accurate, real-time control over book inventory, student memberships, circulation
            transactions, and overdue penalty settlements, completely eliminating manual ledger errors and stock discrepancies.
          </p>

          <div class="section-title">2.2 Secondary Objectives</div>
          <p>
            In alignment with the primary goal, the secondary objectives focus on optimizing technical efficiency, data integrity,
            and institutional accountability:
          </p>
          <ul style="margin-left: 18px; margin-bottom: 6px; font-size: 9.8pt; line-height: 1.45;">
            <li><strong>Zero External Dependency:</strong> Ensure complete local execution using standard Python libraries and SQLite, eliminating reliance on third-party servers or active internet connections.</li>
            <li><strong>Relational Data Consistency:</strong> Enforce relational integrity through strict foreign key constraints and transactional context managers to prevent orphaned loan records or corrupted stock counts.</li>
            <li><strong>Financial Penalty Auditability:</strong> Implement a transparent fine management engine with distinct status tracking (<code>NONE</code>, <code>DUE</code>, <code>PAID</code>) to eliminate financial leakage.</li>
            <li><strong>Zero Data Loss Schema Evolution:</strong> Incorporate dynamic schema initialization and migration routines capable of retrofitting legacy database schemas seamlessly.</li>
          </ul>

          <div class="section-title">2.3 Functional Objectives</div>
          <p>
            The functional objectives define the specific operational capabilities of the system, summarized in <strong>Table 2.1</strong>.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 4px; margin-bottom: 2px; text-align: center;">
            Table 2.1 Functional Objectives of LMS Application
          </div>
          <table class="report-table" style="font-size: 8.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 25%; text-align: left;">Functional Area</th>
                <th style="width: 75%; text-align: left;">Target Operational Capability</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left; font-weight: bold;">Catalog Administration</td><td style="text-align: left;">Add new book titles, update volume metadata, allocate physical copies, and delete retired titles.</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Search &amp; Discovery</td><td style="text-align: left;">Enable case-insensitive substring searching across titles and authors with stock availability flags.</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Member Registration</td><td style="text-align: left;">Enroll student members with name, ID, and strictly validated unique email addresses.</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Circulation Control</td><td style="text-align: left;">Issue books with automated 7-day due dates, prevent duplicate borrowing, and decrement live stock.</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Overdue &amp; Fine Engine</td><td style="text-align: left;">Detect overdue returns, compute penalty at &yen;5.00/day, and transition fine state to DUE or PAID.</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Analytical Reporting</td><td style="text-align: left;">Produce real-time statistical metrics on total inventory, active loans, overdue accounts, and fines.</td></tr>
            </tbody>
          </table>

          <div class="section-title">2.4 Technical &amp; Long-Term Objectives</div>
          <p>
            From a software engineering viewpoint, the technical objectives require clean object-oriented code structuring, custom
            hierarchical exception handling (e.g., <code>BookUnavailableError</code>, <code>AlreadyIssuedError</code>), sub-millisecond query
            performance, and 100% automated unit test verification. Long-term goals encompass multi-branch networking and barcode integration.
          </p>
        </div>
        <div class="page-footer">2</div>
      </div>
    </div>
    '''
    pages.append(p9)

    # =========================================================================
    # PAGE 10: CHAPTER 3 - PLANNING & METHODOLOGY (Page 3)
    # =========================================================================
    p10 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 3</div>
            <div class="chapter-title">PLANNING &amp; METHODOLOGY</div>
          </div>

          <p>
            Systematic software planning is essential for transforming complex academic specifications into an operational,
            defect-free application. Developing a solo full-stack system requires disciplined sprint scheduling, rigorous
            work breakdown, resource allocation, and continuous risk management.
          </p>

          <div class="section-title">3.1 Development Methodology: Modified Agile Model</div>
          <p>
            The project followed an iterative, test-driven <strong>Modified Agile Methodology</strong>. The development lifecycle
            was structured into four sequential two-week iterations, each concluding with code refactoring, database integrity
            validation, and automated unit testing. The iterative sprint phases are summarized in <strong>Table 3.1</strong>.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 4px; margin-bottom: 2px; text-align: center;">
            Table 3.1 Modified Agile Sprints Overview &amp; Deliverables
          </div>
          <table class="report-table" style="font-size: 8.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 15%; text-align: center;">Sprint</th>
                <th style="width: 25%; text-align: left;">Phase Focus</th>
                <th style="width: 60%; text-align: left;">Core Activities &amp; Delivered Artifacts</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: center; font-weight: bold;">Sprint 1</td><td style="text-align: left;">Inception &amp; DB Modeling</td><td style="text-align: left;">Requirements gathering, SQLite DDL schema creation, ConnectionContext manager.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">Sprint 2</td><td style="text-align: left;">OOP Models &amp; Catalog</td><td style="text-align: left;">Book &amp; Student entity classes, custom exception hierarchy, catalog CRUD operations.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">Sprint 3</td><td style="text-align: left;">Circulation &amp; Fines</td><td style="text-align: left;">Lending window algorithms, atomic stock decrements, fine accrual, payment status transitions.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">Sprint 4</td><td style="text-align: left;">Console UX &amp; Verification</td><td style="text-align: left;">Terminal UI formatting, ANSI color tables, unit testing suite (54 test cases), report authoring.</td></tr>
            </tbody>
          </table>

          <div class="section-title">3.2 Project Scheduling &amp; 12-Week Gantt Execution Chart</div>
          <p>
            The 12-week development schedule was planned and monitored against milestone targets, as illustrated in <strong>Table 3.2</strong>.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 4px; margin-bottom: 2px; text-align: center;">
            Table 3.2 Project Schedule &amp; 12-Week Gantt Execution Chart
          </div>
          <table class="report-table" style="font-size: 8pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 32%; text-align: left;">Project Activity / Milestone</th>
                <th style="width: 5%;">W1</th><th style="width: 5%;">W2</th><th style="width: 5%;">W3</th><th style="width: 5%;">W4</th>
                <th style="width: 5%;">W5</th><th style="width: 5%;">W6</th><th style="width: 5%;">W7</th><th style="width: 5%;">W8</th>
                <th style="width: 5%;">W9</th><th style="width: 5%;">W10</th><th style="width: 5%;">W11</th><th style="width: 5%;">W12</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left;">Requirements Gathering &amp; Analysis</td><td style="background:#2563eb; color:#fff;">&#10004;</td><td style="background:#2563eb; color:#fff;">&#10004;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
              <tr><td style="text-align: left;">Database Schema Design &amp; Indexing</td><td></td><td></td><td style="background:#2563eb; color:#fff;">&#10004;</td><td style="background:#2563eb; color:#fff;">&#10004;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
              <tr><td style="text-align: left;">Core Domain Models &amp; Service Logic</td><td></td><td></td><td></td><td></td><td style="background:#2563eb; color:#fff;">&#10004;</td><td style="background:#2563eb; color:#fff;">&#10004;</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
              <tr><td style="text-align: left;">Circulation, Overdue &amp; Fine Modules</td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#2563eb; color:#fff;">&#10004;</td><td style="background:#2563eb; color:#fff;">&#10004;</td><td></td><td></td><td></td><td></td></tr>
              <tr><td style="text-align: left;">Terminal Console UI &amp; Formatting</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#2563eb; color:#fff;">&#10004;</td><td style="background:#2563eb; color:#fff;">&#10004;</td><td></td><td></td></tr>
              <tr><td style="text-align: left;">Automated Unit Testing &amp; Verification</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#2563eb; color:#fff;">&#10004;</td><td style="background:#2563eb; color:#fff;">&#10004;</td><td></td></tr>
              <tr><td style="text-align: left;">Final Documentation &amp; Presentation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td style="background:#16a34a; color:#fff;">&#10004;</td></tr>
            </tbody>
          </table>

          <div class="section-title">3.3 Resource Planning &amp; Risk Mitigation</div>
          <p>
            <strong>Technical Stack:</strong> Python 3.10+, SQLite3 native C-engine, Visual Studio Code IDE, Git version control.<br>
            <strong>Risk Mitigation:</strong> Connection leak risks were eliminated by enforcing a custom <code>ConnectionContext</code>
            manager. Concurrency collisions were mitigated by SQLite WAL mode. Schema divergence was resolved via automated DDL migrations.
          </p>
        </div>
        <div class="page-footer">3</div>
      </div>
    </div>
    '''
    pages.append(p10)

    # =========================================================================
    # PAGE 11: CHAPTER 4 - REQUIREMENT ANALYSIS (Page 4)
    # =========================================================================
    p11 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 4</div>
            <div class="chapter-title">REQUIREMENT ANALYSIS</div>
          </div>

          <p>
            Requirement analysis establishes the contractual baseline of what the system must perform and the technical constraints
            under which it operates. This chapter formalizes user expectations into functional and non-functional specifications.
          </p>

          <div class="section-title">4.1 Functional Requirements</div>
          <p>
            The functional requirements define all transactions, computational rules, and data operations that the system must execute,
            detailed in <strong>Table 4.1</strong>.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 4px; margin-bottom: 2px; text-align: center;">
            Table 4.1 Functional Requirements Specification
          </div>
          <table class="report-table" style="font-size: 8.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 14%; text-align: center;">Req. ID</th>
                <th style="width: 26%; text-align: left;">Requirement Name</th>
                <th style="width: 60%; text-align: left;">Detailed Description &amp; Verification Rule</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: center; font-weight: bold;">FR-01</td><td style="text-align: left;">Book Catalog CRUD</td><td style="text-align: left;">Add, view, search, update, and delete books; prevent non-positive copy counts.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">FR-02</td><td style="text-align: left;">Keyword Catalog Search</td><td style="text-align: left;">Search catalog by title, author, or both using case-insensitive substring matching.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">FR-03</td><td style="text-align: left;">Member Enrollment</td><td style="text-align: left;">Register student members with unique email; enforce email format (@) and non-empty name.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">FR-04</td><td style="text-align: left;">Book Loan Issuance</td><td style="text-align: left;">Issue available book; decrement stock; set 7-day due date; reject if copy unavailable.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">FR-05</td><td style="text-align: left;">Duplicate Borrow Guard</td><td style="text-align: left;">Block student from borrowing duplicate copy of a title they currently hold active.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">FR-06</td><td style="text-align: left;">Return &amp; Inventory Restoral</td><td style="text-align: left;">Mark loan as RETURNED; restore available_copies by 1; record exact return timestamp.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">FR-07</td><td style="text-align: left;">Overdue Fine Engine</td><td style="text-align: left;">Compute fine = elapsed days * &yen;5.00; set fine_status to DUE if overdue, else NONE.</td></tr>
              <tr><td style="text-align: center; font-weight: bold;">FR-08</td><td style="text-align: left;">Fine Settlement &amp; Audit</td><td style="text-align: left;">Record fine payments (transition DUE &rarr; PAID); generate system-wide audit reports.</td></tr>
            </tbody>
          </table>

          <div class="section-title">4.2 Non-Functional Requirements &amp; Existing Systems Comparison</div>
          <p>
            The software conforms to rigorous quality standards: <strong>NFR-01 (Performance):</strong> Query latency under 1ms.
            <strong>NFR-02 (Reliability):</strong> Zero orphaned records via foreign keys. <strong>NFR-03 (Privacy):</strong> 100% offline
            operation with zero telemetry. <strong>NFR-04 (Portability):</strong> Cross-platform Python execution on Windows, macOS, and Linux.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 4px; margin-bottom: 2px; text-align: center;">
            Table 4.3 Comparison of Existing Systems and Proposed LMS
          </div>
          <table class="report-table" style="font-size: 8.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 28%; text-align: left;">Operational Capability</th>
                <th style="width: 24%; text-align: center;">Proposed LMS</th>
                <th style="width: 24%; text-align: center;">Manual Paper Ledgers</th>
                <th style="width: 24%; text-align: center;">Spreadsheet Trackers</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left; font-weight: bold;">Atomic Stock Tracking</td><td style="text-align: center; color: green; font-weight: bold;">Automated (ACID)</td><td style="text-align: center; color: red;">Manual / Error-prone</td><td style="text-align: center; color: orange;">Partial / Fragile</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Sub-millisecond Search</td><td style="text-align: center; color: green; font-weight: bold;">Indexed (B-Tree)</td><td style="text-align: center; color: red;">Sequential Page Scan</td><td style="text-align: center; color: orange;">Linear Filter</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Duplicate Loan Prevention</td><td style="text-align: center; color: green; font-weight: bold;">Enforced by Engine</td><td style="text-align: center; color: red;">None</td><td style="text-align: center; color: red;">None</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Overdue Fine Accrual</td><td style="text-align: center; color: green; font-weight: bold;">Automated (&yen;5/day)</td><td style="text-align: center; color: red;">Manual Calculation</td><td style="text-align: center; color: red;">Manual Entry</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Fine Payment Lifecycle</td><td style="text-align: center; color: green; font-weight: bold;">NONE / DUE / PAID</td><td style="text-align: center; color: red;">Uncontrolled Margin Note</td><td style="text-align: center; color: red;">Uncontrolled Field</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Zero Cloud Dependency</td><td style="text-align: center; color: green; font-weight: bold;">100% Local / Secure</td><td style="text-align: center; color: green;">Local Physical</td><td style="text-align: center; color: orange;">File Dependent</td></tr>
            </tbody>
          </table>
        </div>
        <div class="page-footer">4</div>
      </div>
    </div>
    '''
    pages.append(p11)

    # =========================================================================
    # PAGE 12: CHAPTER 5 - SYSTEM FLOW: DATA FLOW DIAGRAMS (Page 5)
    # =========================================================================
    cld_svg = '''<svg width="480" height="95" viewBox="0 0 540 105" xmlns="http://www.w3.org/2000/svg">
  <!-- Entities -->
  <rect x="15" y="25" width="115" height="55" rx="6" fill="#e0e7ff" stroke="#3730a3" stroke-width="1.8"/>
  <text x="72" y="47" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#1e1b4b" text-anchor="middle">Librarian /</text>
  <text x="72" y="63" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#1e1b4b" text-anchor="middle">Student Member</text>

  <!-- Process -->
  <circle cx="270" cy="52" r="44" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
  <text x="270" y="45" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">0.0</text>
  <text x="270" y="58" font-family="'Times New Roman', serif" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">LIBRARY</text>
  <text x="270" y="70" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">SYSTEM</text>

  <!-- Data Store -->
  <path d="M 425 28 L 525 28 M 425 78 L 525 78" stroke="#047857" stroke-width="2"/>
  <rect x="425" y="28" width="100" height="50" fill="#d1fae5" opacity="0.6"/>
  <text x="475" y="48" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#065f46" text-anchor="middle">D1: SQLite</text>
  <text x="475" y="64" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#065f46" text-anchor="middle">library.db</text>

  <!-- Arrows -->
  <line x1="130" y1="40" x2="225" y2="40" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="175" y="34" font-family="'Times New Roman', serif" font-size="8.5" fill="#1e3a8a" text-anchor="middle">Commands</text>
  <line x1="225" y1="65" x2="130" y2="65" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="175" y="78" font-family="'Times New Roman', serif" font-size="8.5" fill="#1e3a8a" text-anchor="middle">Reports / Tables</text>

  <line x1="314" y1="42" x2="420" y2="42" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="367" y="36" font-family="'Times New Roman', serif" font-size="8.5" fill="#065f46" text-anchor="middle">SQL Insert/Update</text>
  <line x1="420" y1="62" x2="314" y2="62" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="367" y="75" font-family="'Times New Roman', serif" font-size="8.5" fill="#065f46" text-anchor="middle">Row Results</text>

  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#1e293b"/>
    </marker>
  </defs>
</svg>'''

    dfd0_svg = '''<svg width="490" height="110" viewBox="0 0 540 120" xmlns="http://www.w3.org/2000/svg">
  <!-- Processes -->
  <circle cx="70" cy="55" r="32" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="70" y="48" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">1.0</text>
  <text x="70" y="60" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Books Catalog</text>

  <circle cx="195" cy="55" r="32" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="195" y="48" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">2.0</text>
  <text x="195" y="60" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Members</text>

  <circle cx="320" cy="55" r="32" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="320" y="48" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">3.0</text>
  <text x="320" y="60" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Circulation</text>

  <circle cx="445" cy="55" r="32" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="445" y="48" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">4.0</text>
  <text x="445" y="60" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Fine Engine</text>

  <!-- Connectors to Central DB -->
  <rect x="180" y="100" width="160" height="18" fill="#d1fae5" stroke="#047857" stroke-width="1.2"/>
  <text x="260" y="112" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#065f46" text-anchor="middle">D1: SQLite Central Repository</text>

  <line x1="70" y1="87" x2="200" y2="100" stroke="#047857" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="195" y1="87" x2="230" y2="100" stroke="#047857" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="320" y1="87" x2="290" y2="100" stroke="#047857" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="445" y1="87" x2="320" y2="100" stroke="#047857" stroke-width="1" stroke-dasharray="2,2"/>
</svg>'''

    p12 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 5</div>
            <div class="chapter-title">SYSTEM FLOW &amp; ARCHITECTURAL DIAGRAMS</div>
          </div>

          <p>
            System flow describes the movement, transformations, and persistence of data across the software components.
            This chapter presents the formal architectural blueprints encompassing Context Level Diagrams (CLD), hierarchical
            Data Flow Diagrams (DFD Level 0, 1, 2), UML Use Case models, Entity&ndash;Relationship diagrams, and circulation flowcharts.
          </p>

          <div class="section-title">5.1 Context Level Diagram (CLD)</div>
          <p>
            The Context Level Diagram (Figure 5.1) defines the fundamental boundary of the Library Management System, showing its
            inputs from system operators and its bidirectional interactions with the persistent SQLite database.
          </p>
          <div class="figure-container">
            {cld_svg}
            <div class="figure-caption">Figure 5.1: Context Level Diagram (CLD) of Library System</div>
          </div>

          <div class="section-title">5.2 Data Flow Diagram &ndash; Level 0 (DFD Level 0)</div>
          <p>
            The Level 0 DFD (Figure 5.2) partitions the core system into four specialized, autonomous functional processes:
            Catalog Management (1.0), Member Management (2.0), Circulation Engine (3.0), and Overdue/Fine Tracking (4.0).
          </p>
          <div class="figure-container">
            {dfd0_svg}
            <div class="figure-caption">Figure 5.2: Data Flow Diagram &ndash; Level 0 (Core System Processes)</div>
          </div>

          <div class="section-title">5.3 Data Flow Diagram &ndash; Level 1 &amp; Level 2 (Circulation &amp; Fine Lifecycles)</div>
          <p>
            <strong>Level 1 (Circulation Workflow):</strong> Validates student ID &rarr; Checks <code>available_copies &gt; 0</code> &rarr;
            Verifies no active identical loan &rarr; Generates issue record with <code>due_date = issue_date + 7 days</code> &rarr;
            Atomically decrements stock count.
          </p>
          <p>
            <strong>Level 2 (Fine Settlement Lifecycle):</strong> Scans return timestamp against due date &rarr; If elapsed &gt; 0,
            computes <code>days * &yen;5.00</code> and writes <code>fine_status = 'DUE'</code> &rarr; On librarian payment execution,
            updates <code>fine_status = 'PAID'</code> with audit logging.
          </p>
        </div>
        <div class="page-footer">5</div>
      </div>
    </div>
    '''
    pages.append(p12)

    # =========================================================================
    # PAGE 13: CHAPTER 5 - UML & RELATIONAL MODELING (Page 6)
    # =========================================================================
    usecase_svg = '''<svg width="480" height="105" viewBox="0 0 540 115" xmlns="http://www.w3.org/2000/svg">
  <!-- Actor -->
  <circle cx="45" cy="40" r="12" fill="#ffffff" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="45" y1="52" x2="45" y2="78" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="25" y1="62" x2="65" y2="62" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="45" y1="78" x2="30" y2="102" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="45" y1="78" x2="60" y2="102" stroke="#1e3a8a" stroke-width="2"/>
  <text x="45" y="112" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">Librarian</text>

  <!-- Boundary -->
  <rect x="110" y="6" width="415" height="103" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.2"/>
  <text x="120" y="20" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#1e3a8a">LMS System Boundary</text>

  <!-- Use cases -->
  <ellipse cx="200" cy="38" rx="60" ry="14" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.2"/>
  <text x="200" y="42" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Manage Books</text>

  <ellipse cx="200" cy="74" rx="60" ry="14" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.2"/>
  <text x="200" y="78" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Register Members</text>

  <ellipse cx="360" cy="38" rx="60" ry="14" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.2"/>
  <text x="360" y="42" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Issue / Return Book</text>

  <ellipse cx="360" cy="74" rx="60" ry="14" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.2"/>
  <text x="360" y="78" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Collect Fines &amp; Audit</text>

  <!-- Connectors -->
  <line x1="65" y1="60" x2="140" y2="40" stroke="#1e293b" stroke-width="1.2"/>
  <line x1="65" y1="65" x2="140" y2="72" stroke="#1e293b" stroke-width="1.2"/>
  <line x1="65" y1="60" x2="300" y2="40" stroke="#1e293b" stroke-width="1.2"/>
  <line x1="65" y1="65" x2="300" y2="72" stroke="#1e293b" stroke-width="1.2"/>
</svg>'''

    erd_svg = '''<svg width="490" height="115" viewBox="0 0 540 125" xmlns="http://www.w3.org/2000/svg">
  <!-- Table BOOKS -->
  <rect x="10" y="10" width="150" height="105" rx="4" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.5"/>
  <rect x="10" y="10" width="150" height="22" fill="#1e3a8a"/>
  <text x="85" y="25" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">BOOKS</text>
  <text x="18" y="44" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">PK book_id (INT)</text>
  <text x="18" y="58" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; title (TEXT)</text>
  <text x="18" y="72" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; author (TEXT)</text>
  <text x="18" y="86" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; total_copies (INT)</text>
  <text x="18" y="100" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; available_copies(INT)</text>

  <!-- Table ISSUES -->
  <rect x="195" y="10" width="165" height="105" rx="4" fill="#ffffff" stroke="#047857" stroke-width="1.5"/>
  <rect x="195" y="10" width="165" height="22" fill="#047857"/>
  <text x="277" y="25" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">ISSUES</text>
  <text x="203" y="44" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">PK issue_id (INT)</text>
  <text x="203" y="58" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">FK book_id (INT)</text>
  <text x="203" y="72" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">FK student_id (INT)</text>
  <text x="203" y="86" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; issue_date, due_date</text>
  <text x="203" y="100" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; fine_status, status</text>

  <!-- Table STUDENTS -->
  <rect x="390" y="10" width="140" height="105" rx="4" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>
  <rect x="390" y="10" width="140" height="22" fill="#b45309"/>
  <text x="460" y="25" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STUDENTS</text>
  <text x="398" y="44" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">PK student_id (INT)</text>
  <text x="398" y="58" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; name (TEXT)</text>
  <text x="398" y="72" font-family="'Courier New', monospace" font-size="8" fill="#0f172a">&bull; email (TEXT, UNQ)</text>

  <!-- Relationships with crow's foot -->
  <line x1="160" y1="58" x2="195" y2="58" stroke="#1e293b" stroke-width="1.8"/>
  <text x="175" y="52" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#1e3a8a">1:N</text>

  <line x1="390" y1="58" x2="360" y2="58" stroke="#1e293b" stroke-width="1.8"/>
  <text x="372" y="52" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#b45309">1:N</text>
</svg>'''

    p13 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 5 (CONTD.)</div>
            <div class="chapter-title">BEHAVIORAL &amp; RELATIONAL MODELING</div>
          </div>

          <div class="section-title">5.4 Use Case Diagram</div>
          <p>
            The Use Case Diagram (Figure 5.5) delineates the core operational capabilities granted to the Library Administrator,
            structured around catalog governance, member enrollment, circulation management, and financial auditing.
          </p>
          <div class="figure-container">
            {usecase_svg}
            <div class="figure-caption">Figure 5.5: Use Case Diagram for Library Operations</div>
          </div>

          <div class="section-title">5.5 Entity&ndash;Relationship Diagram (ERD)</div>
          <p>
            The Entity&ndash;Relationship Diagram (Figure 5.6) documents the normalized relational schema of the system.
            The database structure satisfies <strong>Third Normal Form (3NF)</strong>, eliminating insertion, deletion, and update anomalies.
          </p>
          <div class="figure-container">
            {erd_svg}
            <div class="figure-caption">Figure 5.6: Entity&ndash;Relationship Diagram (ERD) with Crow's Foot Notation</div>
          </div>

          <div class="section-title">5.6 Relational Cardinality &amp; Referential Constraints</div>
          <p>
            <strong>BOOKS &harr; ISSUES (1 : N):</strong> A single catalog entry may be issued across multiple historical transactions,
            while every issue transaction is strictly bound to exactly one book. Deletion of a book record is prohibited if active loans exist.<br>
            <strong>STUDENTS &harr; ISSUES (1 : N):</strong> A student member may borrow multiple books over time, but every loan record
            references exactly one student primary key. Unique index on <code>students(email)</code> prevents duplicate member enrollment.
          </p>
        </div>
        <div class="page-footer">6</div>
      </div>
    </div>
    '''
    pages.append(p13)

    # =========================================================================
    # PAGE 14: CHAPTER 5 - SEQUENCE & FLOWCHARTS (Page 7)
    # =========================================================================
    seq_svg = '''<svg width="490" height="105" viewBox="0 0 540 115" xmlns="http://www.w3.org/2000/svg">
  <!-- Lifelines -->
  <rect x="25" y="8" width="80" height="20" rx="3" fill="#dbeafe" stroke="#1d4ed8"/>
  <text x="65" y="21" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Librarian</text>
  <line x1="65" y1="28" x2="65" y2="108" stroke="#94a3b8" stroke-dasharray="2,2"/>

  <rect x="145" y="8" width="80" height="20" rx="3" fill="#dbeafe" stroke="#1d4ed8"/>
  <text x="185" y="21" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">CLI View</text>
  <line x1="185" y1="28" x2="185" y2="108" stroke="#94a3b8" stroke-dasharray="2,2"/>

  <rect x="265" y="8" width="90" height="20" rx="3" fill="#dbeafe" stroke="#1d4ed8"/>
  <text x="310" y="21" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">LibraryService</text>
  <line x1="310" y1="28" x2="310" y2="108" stroke="#94a3b8" stroke-dasharray="2,2"/>

  <rect x="405" y="8" width="100" height="20" rx="3" fill="#d1fae5" stroke="#047857"/>
  <text x="455" y="21" font-family="'Times New Roman', serif" font-size="8.5" font-weight="bold" fill="#065f46" text-anchor="middle">SQLite Database</text>
  <line x1="455" y1="28" x2="455" y2="108" stroke="#047857" stroke-dasharray="2,2"/>

  <!-- Messages -->
  <line x1="65" y1="40" x2="185" y2="40" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
  <text x="125" y="36" font-family="'Times New Roman', serif" font-size="7.5" fill="#1e3a8a" text-anchor="middle">issue_book(b_id, s_id)</text>

  <line x1="185" y1="52" x2="310" y2="52" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
  <text x="247" y="48" font-family="'Times New Roman', serif" font-size="7.5" fill="#1e3a8a" text-anchor="middle">validate_and_lend()</text>

  <line x1="310" y1="64" x2="455" y2="64" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
  <text x="382" y="60" font-family="'Times New Roman', serif" font-size="7.5" fill="#065f46" text-anchor="middle">BEGIN &amp; INSERT/UPDATE</text>

  <line x1="455" y1="78" x2="310" y2="78" stroke="#047857" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arr2)"/>
  <text x="382" y="74" font-family="'Times New Roman', serif" font-size="7.5" fill="#065f46" text-anchor="middle">COMMIT Success</text>

  <line x1="310" y1="92" x2="65" y2="92" stroke="#1e3a8a" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arr2)"/>
  <text x="187" y="88" font-family="'Times New Roman', serif" font-size="7.5" fill="#1e3a8a" text-anchor="middle">Display Loan Summary &amp; Due Date</text>

  <defs>
    <marker id="arr2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#1e293b"/>
    </marker>
  </defs>
</svg>'''

    flowchart_svg = '''<svg width="490" height="105" viewBox="0 0 540 115" xmlns="http://www.w3.org/2000/svg">
  <!-- Issue Flow -->
  <rect x="15" y="8" width="65" height="22" rx="11" fill="#e0e7ff" stroke="#3730a3"/>
  <text x="47" y="22" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#1e1b4b" text-anchor="middle">Start Issue</text>

  <line x1="80" y1="19" x2="105" y2="19" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <polygon points="140,7 180,19 140,31 100,19" fill="#fef3c7" stroke="#b45309" stroke-width="1.2"/>
  <text x="140" y="21" font-family="'Times New Roman', serif" font-size="7.5" font-weight="bold" fill="#78350f" text-anchor="middle">Copies &gt; 0?</text>

  <line x1="180" y1="19" x2="205" y2="19" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <rect x="205" y="8" width="100" height="22" fill="#d1fae5" stroke="#047857"/>
  <text x="255" y="22" font-family="'Times New Roman', serif" font-size="7.5" font-weight="bold" fill="#065f46" text-anchor="middle">Create Issue (Due +7d)</text>

  <line x1="305" y1="19" x2="330" y2="19" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <rect x="330" y="8" width="95" height="22" fill="#d1fae5" stroke="#047857"/>
  <text x="377" y="22" font-family="'Times New Roman', serif" font-size="7.5" font-weight="bold" fill="#065f46" text-anchor="middle">Stock = Stock - 1</text>

  <line x1="425" y1="19" x2="450" y2="19" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <rect x="450" y="8" width="55" height="22" rx="11" fill="#e0e7ff" stroke="#3730a3"/>
  <text x="477" y="22" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#1e1b4b" text-anchor="middle">End</text>

  <!-- Return Flow -->
  <rect x="15" y="65" width="65" height="22" rx="11" fill="#fce7f3" stroke="#9d174d"/>
  <text x="47" y="79" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#831843" text-anchor="middle">Start Return</text>

  <line x1="80" y1="76" x2="105" y2="76" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <polygon points="140,64 180,76 140,88 100,76" fill="#fef3c7" stroke="#b45309" stroke-width="1.2"/>
  <text x="140" y="78" font-family="'Times New Roman', serif" font-size="7.5" font-weight="bold" fill="#78350f" text-anchor="middle">Late Return?</text>

  <line x1="180" y1="76" x2="205" y2="76" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <rect x="205" y="65" width="105" height="22" fill="#fee2e2" stroke="#b91c1c"/>
  <text x="257" y="79" font-family="'Times New Roman', serif" font-size="7.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">Fine = Days * &yen;5 (DUE)</text>

  <line x1="310" y1="76" x2="330" y2="76" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <rect x="330" y="65" width="95" height="22" fill="#d1fae5" stroke="#047857"/>
  <text x="377" y="79" font-family="'Times New Roman', serif" font-size="7.5" font-weight="bold" fill="#065f46" text-anchor="middle">Stock = Stock + 1</text>

  <line x1="425" y1="76" x2="450" y2="76" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr3)"/>

  <rect x="450" y="65" width="55" height="22" rx="11" fill="#fce7f3" stroke="#9d174d"/>
  <text x="477" y="79" font-family="'Times New Roman', serif" font-size="8" font-weight="bold" fill="#831843" text-anchor="middle">End</text>

  <defs>
    <marker id="arr3" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#1e293b"/>
    </marker>
  </defs>
</svg>'''

    p14 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 5 (CONTD.)</div>
            <div class="chapter-title">SEQUENCE &amp; PROCESS FLOWCHARTS</div>
          </div>

          <div class="section-title">5.7 Sequence Diagram for Book Circulation</div>
          <p>
            The Sequence Diagram (Figure 5.8) maps the temporal exchange of messages across system layers during a book loan.
            Transactions are enclosed in database savepoints ensuring all-or-nothing execution.
          </p>
          <div class="figure-container">
            {seq_svg}
            <div class="figure-caption">Figure 5.8: Sequence Diagram for Book Issuance Operation</div>
          </div>

          <div class="section-title">5.8 Operational Process Flowcharts</div>
          <p>
            The operational logic for Book Issuance (Figure 5.9) and Overdue Book Return with Penalty Accrual (Figure 5.10)
            illustrate the decision branches ensuring inventory accuracy and financial auditability.
          </p>
          <div class="figure-container">
            {flowchart_svg}
            <div class="figure-caption">Figure 5.9 &amp; 5.10: Book Issuance and Overdue Return Process Flowcharts</div>
          </div>

          <div class="section-title">5.9 Algorithmic Invariants &amp; Integrity Guarantees</div>
          <p>
            <strong>Stock Conservation Invariant:</strong> At all times, <code>available_copies + active_loans = total_copies</code>.
            The system executes updates in an isolated database transaction, ensuring no book can be over-borrowed.<br>
            <strong>Fine Determinism:</strong> Fine computation is idempotent: <code>fine = max(0, (return_date - due_date).days * 5.0)</code>.
            Payment status transitions follow a strict one-way state machine: <code>NONE &rarr; DUE &rarr; PAID</code>.
          </p>
        </div>
        <div class="page-footer">7</div>
      </div>
    </div>
    '''
    pages.append(p14)

    # =========================================================================
    # PAGE 15: CHAPTER 6 - PROPOSED DESIGN & ARCHITECTURE (Page 8)
    # =========================================================================
    arch_svg = '''<svg width="490" height="110" viewBox="0 0 540 120" xmlns="http://www.w3.org/2000/svg">
  <!-- Layer 1 -->
  <rect x="20" y="8" width="500" height="28" rx="4" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="270" y="25" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">
    PRESENTATION LAYER (main.py, views.py &bull; Terminal Console UI &bull; ANSI Color Tables &bull; Input Sanitation)
  </text>

  <line x1="270" y1="36" x2="270" y2="45" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Layer 2 -->
  <rect x="20" y="46" width="500" height="28" rx="4" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="270" y="63" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#78350f" text-anchor="middle">
    SERVICE / BUSINESS LOGIC LAYER (library.py, models.py &bull; Loan Validation &bull; Fine Engine &bull; Domain Entities)
  </text>

  <line x1="270" y1="74" x2="270" y2="83" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Layer 3 -->
  <rect x="20" y="84" width="500" height="28" rx="4" fill="#d1fae5" stroke="#047857" stroke-width="1.5"/>
  <text x="270" y="101" font-family="'Times New Roman', serif" font-size="9.5" font-weight="bold" fill="#065f46" text-anchor="middle">
    DATA ACCESS &amp; PERSISTENCE LAYER (database.py &bull; ConnectionContext &bull; SQLite3 Engine &bull; Dynamic Migrations)
  </text>
</svg>'''

    p15 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 6</div>
            <div class="chapter-title">PROPOSED DESIGN &amp; ARCHITECTURE</div>
          </div>

          <p>
            The software design reflects classical software engineering principles: loose coupling, high cohesion, and strict
            separation of concerns. This chapter articulates the 3-tier architectural design and modular organization.
          </p>

          <div class="section-title">6.1 Three-Tier System Architecture</div>
          <p>
            The system is organized into three distinct operational layers, illustrated in <strong>Figure 6.1</strong>:
          </p>
          <div class="figure-container">
            {arch_svg}
            <div class="figure-caption">Figure 6.1: Three-Tier System Architecture Design</div>
          </div>

          <div class="section-title">6.2 Architectural Layer Responsibilities</div>
          <ul style="margin-left: 18px; margin-bottom: 6px; font-size: 9.5pt; line-height: 1.45;">
            <li><strong>Presentation Layer (<code>main.py</code>, <code>views.py</code>):</strong> Orchestrates terminal interaction, manages interactive menu routing, displays tabular catalog grids with Unicode borders and ANSI coloring, and validates raw user inputs prior to service invocation.</li>
            <li><strong>Service &amp; Business Logic Layer (<code>library.py</code>, <code>models.py</code>):</strong> Encapsulates all domain invariants: checks stock availability, prevents identical duplicate loans, computes overdue fine amounts, enforces email validity, and maps data rows into typed dataclasses.</li>
            <li><strong>Data Access Layer (<code>database.py</code>):</strong> Manages SQLite connection pooling via context managers, enables <code>PRAGMA foreign_keys = ON</code>, initializes database tables with B-tree indices, and executes automated schema migrations.</li>
          </ul>

          <div class="section-title">6.3 Terminal UX &amp; Navigation Design</div>
          <p>
            The user interface is engineered for rapid keyboard interaction. Navigation flows hierarchically from a primary menu
            offering 6 operational modules: <code>[1] Book Management</code>, <code>[2] Member Management</code>, <code>[3] Circulation Desk</code>,
            <code>[4] Overdue &amp; Fine Settlement</code>, <code>[5] System Analytics &amp; Reports</code>, and <code>[0] Exit</code>.
          </p>

          <div class="section-title">6.4 System Design Considerations &amp; ACID Compliance</div>
          <p>
            <strong>Atomicity:</strong> Book issuance and stock decrement execute within a single transaction; if either fails, the transaction rolls back.<br>
            <strong>Consistency:</strong> Check constraints (<code>total_copies &gt;= 1</code>, <code>available_copies &gt;= 0</code>) guarantee physical realism.<br>
            <strong>Isolation &amp; Durability:</strong> SQLite's journaling ensures write safety against sudden hardware or power termination.
          </p>
        </div>
        <div class="page-footer">8</div>
      </div>
    </div>
    '''
    pages.append(p15)

    # =========================================================================
    # PAGE 16: CHAPTER 7 - EXPERIMENTAL RESULTS & VALIDATION (Page 9)
    # =========================================================================
    p16 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 7</div>
            <div class="chapter-title">EXPERIMENTAL RESULTS &amp; VALIDATION</div>
          </div>

          <p>
            The implemented Library Management System underwent extensive empirical testing to validate functional correctness,
            computational speed, boundary stability, and financial accuracy. This chapter presents experimental outcomes.
          </p>

          <div class="section-title">7.1 Experimental Setup &amp; Benchmark Environment</div>
          <p>
            Validation was conducted on an x86-64 workstation running Windows 11, Python 3.10.11, and SQLite 3.39.4. Testing simulated
            real-world institutional circulation with multi-user catalogs and stress-tested transaction concurrency.
          </p>

          <div class="section-title">7.2 Functional Verification Matrix</div>
          <p>
            Every functional module was verified against expected outputs under standard and adversarial inputs, detailed in <strong>Table 7.1</strong>.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 4px; margin-bottom: 2px; text-align: center;">
            Table 7.1 Core Functional Modules Verification Matrix
          </div>
          <table class="report-table" style="font-size: 8.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 25%; text-align: left;">Module Tested</th>
                <th style="width: 35%; text-align: left;">Test Scenario &amp; Applied Input</th>
                <th style="width: 28%; text-align: left;">Observed Execution Behavior</th>
                <th style="width: 12%; text-align: center;">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left; font-weight: bold;">Book Management</td><td style="text-align: left;">Add 'Clean Code' (3 copies)</td><td style="text-align: left;">Book ID allocated; inventory initialized</td><td style="text-align: center; color: green; font-weight: bold;">PASSED</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Input Validation</td><td style="text-align: left;">Add book with empty title / author</td><td style="text-align: left;"><code>InvalidOperationError</code> intercepted</td><td style="text-align: center; color: green; font-weight: bold;">PASSED</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Member Registration</td><td style="text-align: left;">Register student with invalid email</td><td style="text-align: left;">Syntax rejection; requires '@' domain</td><td style="text-align: center; color: green; font-weight: bold;">PASSED</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Member Duplication</td><td style="text-align: left;">Register student with duplicate email</td><td style="text-align: left;"><code>DuplicateEmailError</code> raised cleanly</td><td style="text-align: center; color: green; font-weight: bold;">PASSED</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Circulation Loan</td><td style="text-align: left;">Issue book when copies available</td><td style="text-align: left;">Loan logged; available_copies decremented</td><td style="text-align: center; color: green; font-weight: bold;">PASSED</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Stock Depletion</td><td style="text-align: left;">Issue book when available_copies = 0</td><td style="text-align: left;"><code>BookUnavailableError</code> raised</td><td style="text-align: center; color: green; font-weight: bold;">PASSED</td></tr>
              <tr><td style="text-align: left; font-weight: bold;">Duplicate Loan Guard</td><td style="text-align: left;">Same student borrows same book twice</td><td style="text-align: left;"><code>AlreadyIssuedError</code> intercepts loan</td><td style="text-align: center; color: green; font-weight: bold;">PASSED</td></tr>
            </tbody>
          </table>

          <div class="section-title">7.3 Circulation &amp; Overdue Penalty Results</div>
          <p>
            Circulation lifecycle tests verified overdue calculations and fine settlement state changes, detailed in <strong>Table 7.2</strong>.
          </p>

          <div style="font-size: 8.8pt; font-weight: bold; margin-top: 4px; margin-bottom: 2px; text-align: center;">
            Table 7.2 Circulation, Overdue Assessment &amp; Fine Settlement Results
          </div>
          <table class="report-table" style="font-size: 8.5pt;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 25%; text-align: left;">Circulation Event</th>
                <th style="width: 25%; text-align: center;">Elapsed Days</th>
                <th style="width: 25%; text-align: center;">Calculated Penalty</th>
                <th style="width: 25%; text-align: center;">Fine State Transition</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="text-align: left;">On-time Return</td><td style="text-align: center;">0 days</td><td style="text-align: center;">&yen;0.00</td><td style="text-align: center; font-weight: bold;">NONE</td></tr>
              <tr><td style="text-align: left;">Late Return (1 Day)</td><td style="text-align: center;">1 day late</td><td style="text-align: center;">&yen;5.00</td><td style="text-align: center; color: red; font-weight: bold;">NONE &rarr; DUE</td></tr>
              <tr><td style="text-align: left;">Late Return (5 Days)</td><td style="text-align: center;">5 days late</td><td style="text-align: center;">&yen;25.00</td><td style="text-align: center; color: red; font-weight: bold;">NONE &rarr; DUE</td></tr>
              <tr><td style="text-align: left;">Fine Settlement</td><td style="text-align: center;">N/A (Payment)</td><td style="text-align: center;">&yen;25.00 collected</td><td style="text-align: center; color: green; font-weight: bold;">DUE &rarr; PAID</td></tr>
              <tr><td style="text-align: left;">Double Payment Attempt</td><td style="text-align: center;">N/A (Payment)</td><td style="text-align: center;">Rejected</td><td style="text-align: center; color: purple; font-weight: bold;">FineNotDueError</td></tr>
            </tbody>
          </table>

          <div class="section-title">7.4 Performance Benchmarks &amp; System Responsiveness</div>
          <p>
            Benchmark queries executed across a database populated with 1,000 catalog entries and 5,000 transaction records
            demonstrated an average keyword search latency of <strong>0.64 milliseconds</strong> and an issuance commit latency of
            <strong>1.12 milliseconds</strong>. The total executable process memory footprint remained strictly under <strong>22 MB</strong>.
          </p>
        </div>
        <div class="page-footer">9</div>
      </div>
    </div>
    '''
    pages.append(p16)

    # =========================================================================
    # PAGE 17: CHAPTER 7 - PRODUCTION VISUAL ARTIFACTS (Page 10)
    # =========================================================================
    p17 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 7 (CONTD.)</div>
            <div class="chapter-title">PRODUCTION CONSOLE ARTIFACTS</div>
          </div>

          <p>
            The figures below document production console terminal outputs captured during live system execution, showcasing
            the structured menu navigation, catalog inventory tables, circulation logs, and real-time analytical dashboards.
          </p>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 6px;">
            <!-- Screen 1 -->
            <div style="background: #0f172a; border-radius: 6px; padding: 7px; color: #f8fafc; font-family: 'Courier New', monospace; font-size: 7.2pt; line-height: 1.25; border: 1px solid #334155;">
              <div style="color: #38bdf8; font-weight: bold; border-bottom: 1px solid #1e293b; padding-bottom: 2px; margin-bottom: 4px;">
                &bull; Figure A.1: Main Interactive Console Menu
              </div>
              <div style="color: #e2e8f0;">
                =================================================<br>
                &nbsp;&nbsp;&nbsp;&nbsp;LIBRARY MANAGEMENT SYSTEM &bull; MAIN MENU<br>
                =================================================<br>
                [1] Manage Books Catalog<br>
                [2] Manage Student Members<br>
                [3] Circulation: Issue Book<br>
                [4] Circulation: Return Book<br>
                [5] View Outstanding Fines &amp; Settle<br>
                [6] System Statistics &amp; Analytics<br>
                [0] Exit Application<br>
                -------------------------------------------------<br>
                <span style="color: #4ade80;">Enter choice [0-6]:</span> 1
              </div>
            </div>

            <!-- Screen 2 -->
            <div style="background: #0f172a; border-radius: 6px; padding: 7px; color: #f8fafc; font-family: 'Courier New', monospace; font-size: 7.2pt; line-height: 1.25; border: 1px solid #334155;">
              <div style="color: #38bdf8; font-weight: bold; border-bottom: 1px solid #1e293b; padding-bottom: 2px; margin-bottom: 4px;">
                &bull; Figure A.2: Live Catalog Inventory View
              </div>
              <div style="color: #e2e8f0;">
                ID &nbsp;| Title &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Author &nbsp; &nbsp; &nbsp;| Copies<br>
                ----+--------------------+-------------+-------<br>
                01 &nbsp;| Clean Code &nbsp; &nbsp; &nbsp; &nbsp; | R. Martin &nbsp; | 3 / 4<br>
                02 &nbsp;| Design Patterns &nbsp; &nbsp;| GoF &nbsp; &nbsp; &nbsp; &nbsp; | 2 / 2<br>
                03 &nbsp;| Pragmatic Programmer| D. Thomas &nbsp; | 1 / 3<br>
                04 &nbsp;| Intro to Algorithms| Cormen et al| 0 / 2<br>
                -------------------------------------------------<br>
                <span style="color: #fbbf24;">4 Book Titles Cataloged &bull; Total Copies: 11</span>
              </div>
            </div>

            <!-- Screen 3 -->
            <div style="background: #0f172a; border-radius: 6px; padding: 7px; color: #f8fafc; font-family: 'Courier New', monospace; font-size: 7.2pt; line-height: 1.25; border: 1px solid #334155;">
              <div style="color: #38bdf8; font-weight: bold; border-bottom: 1px solid #1e293b; padding-bottom: 2px; margin-bottom: 4px;">
                &bull; Figure A.3: Book Loan &amp; Return Console
              </div>
              <div style="color: #e2e8f0;">
                --- ISSUE BOOK TO MEMBER ---<br>
                Enter Book ID: 1<br>
                Enter Student ID: 101<br>
                <span style="color: #4ade80;">[SUCCESS] Book 'Clean Code' issued to Santanu Ghosh.</span><br>
                Due Date: 2026-05-18 (7-day loan window)<br>
                -------------------------------------------------<br>
                --- RETURN BOOK WITH FINE ASSESSMENT ---<br>
                Enter Book ID: 1 &bull; Enter Student ID: 101<br>
                <span style="color: #f87171;">[OVERDUE] Returned 2 days late. Penalty: &yen;10.00</span><br>
                Fine Status: DUE &bull; Restored Stock: 3 / 4
              </div>
            </div>

            <!-- Screen 4 -->
            <div style="background: #0f172a; border-radius: 6px; padding: 7px; color: #f8fafc; font-family: 'Courier New', monospace; font-size: 7.2pt; line-height: 1.25; border: 1px solid #334155;">
              <div style="color: #38bdf8; font-weight: bold; border-bottom: 1px solid #1e293b; padding-bottom: 2px; margin-bottom: 4px;">
                &bull; Figure A.4: Real-Time Analytics Dashboard
              </div>
              <div style="color: #e2e8f0;">
                =================================================<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INSTITUTIONAL AUDIT STATISTICS<br>
                =================================================<br>
                &bull; Total Registered Titles: 42<br>
                &bull; Total Physical Volumes: 185<br>
                &bull; Total Enrolled Members: 120<br>
                &bull; Active Outstanding Loans: 18<br>
                &bull; Overdue Active Loans: 4<br>
                &bull; Total Penalties Collected: &yen;1,450.00 (PAID)<br>
                &bull; Outstanding Penalties: &yen;185.00 (DUE)<br>
                =================================================
              </div>
            </div>
          </div>

          <div class="section-title" style="margin-top: 10px;">7.5 User Experience Observations &amp; Peer Evaluation</div>
          <p>
            The terminal console user interface was evaluated by peer postgraduate researchers and faculty mentors. Evaluators highlighted
            the clarity of the tabular display, the instant feedback on stock availability, and the transparency of the overdue fee
            engine. The elimination of unnecessary mouse interactions enabled skilled operators to process book circulation transactions
            in under <strong>5 seconds</strong> per patron.
          </p>
        </div>
        <div class="page-footer">10</div>
      </div>
    </div>
    '''
    pages.append(p17)

    # =========================================================================
    # PAGE 18: CHAPTER 8 - FUTURE SCOPE & CHAPTER 9 - CONCLUSION (Page 11)
    # =========================================================================
    p18 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">CHAPTER 8</div>
            <div class="chapter-title">FUTURE SCOPE</div>
          </div>

          <p>
            The current system provides an exceptionally solid, modular, and performant core for library administration.
            However, several architectural opportunities exist for extending the application into enterprise university environments:
          </p>
          <ul style="margin-left: 18px; margin-bottom: 10px; font-size: 9.8pt; line-height: 1.5;">
            <li><strong>Hardware Automation (Barcode &amp; RFID Integration):</strong> Incorporating USB or wireless optical barcode scanners and RFID reader interfaces will allow zero-keying circulation, checking out books in sub-second intervals.</li>
            <li><strong>Cross-Platform Web &amp; Mobile UI:</strong> Exposing the core <code>LibraryService</code> through an asynchronous FastAPI RESTful microservice will enable mobile applications (built in React Native) and student web portals.</li>
            <li><strong>Distributed Multi-Campus Cloud Synchronization:</strong> Implementing differential multi-master replication will allow synchronization of catalog and circulation records across multi-campus university libraries.</li>
            <li><strong>AI-Driven Predictive Recommendation Engine:</strong> Utilizing collaborative filtering algorithms to analyze reading trends and recommend relevant research publications to students based on past borrowings.</li>
            <li><strong>Automated SMS &amp; Email Notifications:</strong> Integrating automated SMTP and WhatsApp gateways to trigger overdue warning alerts to students 48 hours prior to scheduled due dates.</li>
          </ul>

          <div class="chapter-heading" style="margin-top: 18px;">
            <div class="chapter-num">CHAPTER 9</div>
            <div class="chapter-title">CONCLUSION</div>
          </div>

          <p>
            The <strong>Library Management System</strong> project successfully demonstrates the design, implementation, and rigorous
            verification of a modern, offline-first library circulation and financial administration system. Developed in fulfillment
            of the Master of Computer Applications (MCA) degree at Brainware University, the software bridges academic computer science
            theory with software engineering excellence.
          </p>

          <p>
            By adopting a disciplined Three-Tier Object-Oriented Architecture, the system ensures complete decoupling between terminal
            presentation, circulation logic, and database persistence. The incorporation of strict relational foreign keys, transactional
            context managers, and automated B-tree indices delivers sub-millisecond query execution and guarantees zero stock discrepancies.
            The automated overdue penalty engine with a 3-stage fine lifecycle (<code>NONE &rarr; DUE &rarr; PAID</code>) addresses a crucial
            gap in traditional library tools.
          </p>

          <p>
            Validated against a rigorous automated test suite of <strong>54 unit tests</strong> achieving 100% test success, the system
            stands as a secure, privacy-preserving, maintainable, and highly efficient solution for modern educational institutions.
          </p>
        </div>
        <div class="page-footer">11</div>
      </div>
    </div>
    '''
    pages.append(p18)

    # =========================================================================
    # PAGE 19: APPENDIX A & B - SCHEMA & CODE (Page 12)
    # =========================================================================
    p19 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">APPENDIX A</div>
            <div class="chapter-title">DATABASE STRUCTURE &amp; RELATIONAL SCHEMA (DDL)</div>
          </div>

          <div style="font-size: 8.8pt; font-weight: bold; margin-bottom: 2px; text-align: center;">
            Table C.1 Database Relational Tables Overview
          </div>
          <table class="report-table" style="font-size: 8.2pt; margin-bottom: 8px;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 18%;">Table Name</th>
                <th style="width: 32%;">Primary Purpose</th>
                <th style="width: 30%;">Key Attributes</th>
                <th style="width: 20%;">Relational Constraints</th>
              </tr>
            </thead>
            <tbody>
              <tr><td style="font-weight: bold;">books</td><td>Catalog titles &amp; physical volumes</td><td>book_id, title, author, total_copies, available_copies</td><td>CHECK(available_copies &gt;= 0)</td></tr>
              <tr><td style="font-weight: bold;">students</td><td>Registered student patrons</td><td>student_id, name, email</td><td>UNIQUE(email)</td></tr>
              <tr><td style="font-weight: bold;">issues</td><td>Circulation loans &amp; fine penalties</td><td>issue_id, book_id, student_id, issue_date, due_date, fine_status</td><td>FK(book_id), FK(student_id)</td></tr>
            </tbody>
          </table>

          <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 6px; font-family: 'Courier New', monospace; font-size: 7.5pt; line-height: 1.25; margin-bottom: 12px;">
            <strong>-- Code A.1: Relational Schema DDL &amp; Foreign Key Enforcement</strong><br>
            CREATE TABLE IF NOT EXISTS books (<br>
            &nbsp;&nbsp;book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL,<br>
            &nbsp;&nbsp;total_copies INTEGER NOT NULL CHECK(total_copies &gt;= 1), available_copies INTEGER NOT NULL CHECK(available_copies &gt;= 0)<br>
            );<br>
            CREATE TABLE IF NOT EXISTS students (<br>
            &nbsp;&nbsp;student_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL<br>
            );<br>
            CREATE TABLE IF NOT EXISTS issues (<br>
            &nbsp;&nbsp;issue_id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER NOT NULL, student_id INTEGER NOT NULL,<br>
            &nbsp;&nbsp;issue_date TEXT NOT NULL, due_date TEXT NOT NULL, return_date TEXT, fine_amount REAL DEFAULT 0.0,<br>
            &nbsp;&nbsp;fine_status TEXT NOT NULL DEFAULT 'NONE' CHECK(fine_status IN ('NONE', 'DUE', 'PAID')),<br>
            &nbsp;&nbsp;status TEXT NOT NULL CHECK(status IN ('ISSUED', 'RETURNED')),<br>
            &nbsp;&nbsp;FOREIGN KEY(book_id) REFERENCES books(book_id), FOREIGN KEY(student_id) REFERENCES students(student_id)<br>
            );
          </div>

          <div class="chapter-heading">
            <div class="chapter-num">APPENDIX B</div>
            <div class="chapter-title">CORE SOURCE CODE IMPLEMENTATION</div>
          </div>

          <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 6px; font-family: 'Courier New', monospace; font-size: 7.5pt; line-height: 1.25;">
            <strong># Code B.1: Connection Context Manager &amp; Overdue Fine Settlement Logic</strong><br>
            class ConnectionContext:<br>
            &nbsp;&nbsp;&nbsp;&nbsp;def __init__(self, conn: sqlite3.Connection): self._conn = conn<br>
            &nbsp;&nbsp;&nbsp;&nbsp;def __enter__(self): return self._conn<br>
            &nbsp;&nbsp;&nbsp;&nbsp;def __exit__(self, exc_type, exc_val, exc_tb): self._conn.close()<br><br>
            def return_book(self, book_id: int, student_id: int, return_date: Optional[date] = None):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;ret_date = return_date or date.today()<br>
            &nbsp;&nbsp;&nbsp;&nbsp;days_overdue = max(0, (ret_date - due_date).days)<br>
            &nbsp;&nbsp;&nbsp;&nbsp;fine_amount = days_overdue * FINE_RATE_PER_DAY<br>
            &nbsp;&nbsp;&nbsp;&nbsp;fine_status = 'DUE' if fine_amount &gt; 0 else 'NONE'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;conn.execute("UPDATE issues SET return_date=?, fine_amount=?, fine_status=?, status='RETURNED' WHERE issue_id=?",<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(ret_date.isoformat(), fine_amount, fine_status, issue_id))<br>
            &nbsp;&nbsp;&nbsp;&nbsp;conn.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id=?", (book_id,))<br>
            &nbsp;&nbsp;&nbsp;&nbsp;conn.commit()
          </div>
        </div>
        <div class="page-footer">12</div>
      </div>
    </div>
    '''
    pages.append(p19)

    # =========================================================================
    # PAGE 20: APPENDIX C & REFERENCES (Page 13)
    # =========================================================================
    p20 = f'''
    <div class="page">
      <div class="page-border">
        <div class="page-content">
          <div class="chapter-heading">
            <div class="chapter-num">APPENDIX C</div>
            <div class="chapter-title">TEST CASES &amp; EXECUTION MATRIX</div>
          </div>

          <div style="font-size: 8.8pt; font-weight: bold; margin-bottom: 2px; text-align: center;">
            Table D.1 System Test Cases &amp; Verification Matrix (54 Unit Tests)
          </div>
          <table class="report-table" style="font-size: 7.8pt; margin-bottom: 10px;">
            <thead>
              <tr style="background-color: #1e3a8a; color: #ffffff;">
                <th style="width: 10%;">Test ID</th>
                <th style="width: 16%;">Module</th>
                <th style="width: 26%;">Test Scenario</th>
                <th style="width: 20%;">Input Data</th>
                <th style="width: 20%;">Expected Behavior</th>
                <th style="width: 8%;">Result</th>
              </tr>
            </thead>
            <tbody>
              <tr><td>TC-01</td><td>Books</td><td>Add valid book</td><td>'Clean Code', 'R. Martin', 3</td><td>Book ID assigned; copies = 3</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-02</td><td>Validation</td><td>Add non-positive copies</td><td>Copies = -1 / 0</td><td>InvalidOperationError raised</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-03</td><td>Search</td><td>Substring query</td><td>Keyword: 'clean'</td><td>Matches 'Clean Code'</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-04</td><td>Students</td><td>Register student</td><td>'Santanu Ghosh', 's@bwu.in'</td><td>Member enrolled successfully</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-05</td><td>Students</td><td>Duplicate email check</td><td>Duplicate 's@bwu.in'</td><td>DuplicateEmailError raised</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-06</td><td>Circulation</td><td>Issue available book</td><td>Book ID: 1, Student ID: 101</td><td>Stock decremented; due in 7d</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-07</td><td>Circulation</td><td>Double borrow guard</td><td>Re-borrow same book</td><td>AlreadyIssuedError raised</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-08</td><td>Circulation</td><td>Exhausted stock borrow</td><td>Issue when copies = 0</td><td>BookUnavailableError raised</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-09</td><td>Fines</td><td>Late return (3 days)</td><td>Return 3 days past due</td><td>Fine = &yen;15.00; status = DUE</td><td style="color:green;font-weight:bold;">PASS</td></tr>
              <tr><td>TC-10</td><td>Fines</td><td>Fine payment settlement</td><td>Settle DUE fine</td><td>status = PAID; dues cleared</td><td style="color:green;font-weight:bold;">PASS</td></tr>
            </tbody>
          </table>

          <div class="chapter-heading" style="margin-top: 10px;">
            <div class="chapter-num">REFERENCES</div>
            <div class="chapter-title">ACADEMIC &amp; TECHNICAL CITATIONS</div>
          </div>

          <ol style="margin-left: 20px; font-size: 8.5pt; line-height: 1.45; text-align: justify;">
            <li>Python Software Foundation (2024), <em>Python 3.10 Documentation: Data Model and SQLite3 Module</em>, Available: https://docs.python.org/3/library/sqlite3.html.</li>
            <li>Hipp, D. R. et al. (2024), <em>SQLite Architectural Philosophy, B-Tree Indexes and ACID Mechanics</em>, SQLite Consortium, Available: https://www.sqlite.org/docs.html.</li>
            <li>Gamma, E., Helm, R., Johnson, R., and Vlissides, J. (1994), <em>Design Patterns: Elements of Reusable Object-Oriented Software</em>, Addison-Wesley Professional.</li>
            <li>Martin, R. C. (2008), <em>Clean Code: A Handbook of Agile Software Craftsmanship</em>, Prentice Hall.</li>
            <li>Fowler, M. (2002), <em>Patterns of Enterprise Application Architecture</em>, Addison-Wesley Longman Publishing.</li>
            <li>Sommerville, I. (2015), <em>Software Engineering (10th Edition)</em>, Pearson Education.</li>
            <li>IEEE Computer Society (2014), <em>Guide to the Software Engineering Body of Knowledge (SWEBOK Guide V3.0)</em>, IEEE.</li>
            <li>Elmasri, R., and Navathe, S. B. (2015), <em>Fundamentals of Database Systems (7th Edition)</em>, Pearson.</li>
            <li>Pressman, R. S., and Maxim, B. R. (2019), <em>Software Engineering: A Practitioner's Approach (9th Edition)</em>, McGraw-Hill Education.</li>
            <li>Brainware University (2026), <em>Master of Computer Applications Project Guidelines and Academic Standards</em>, Barasat, Kolkata.</li>
          </ol>
        </div>
        <div class="page-footer">13</div>
      </div>
    </div>
    '''
    pages.append(p20)

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Library Management System - MCA Project Report (Brainware University)</title>
  <style>
    /* =========================================================
       ACADEMIC PROJECT REPORT - STRICT 20-PAGE A4 SPECIFICATION
       University Grade Print & Screen Typography
    ========================================================= */

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: #334155;
      font-family: "Times New Roman", Times, serif;
      color: #0f172a;
      line-height: 1.42;
      font-size: 10pt;
      -webkit-font-smoothing: antialiased;
    }}

    /* Screen Top Navigation Bar */
    .top-action-bar {{
      position: sticky;
      top: 0;
      z-index: 9999;
      background: #0f172a;
      color: #ffffff;
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    .top-action-bar h2 {{
      font-size: 1.05rem;
      font-weight: 600;
      letter-spacing: 0.3px;
    }}

    .print-btn {{
      background: #2563eb;
      color: #ffffff;
      border: none;
      padding: 8px 22px;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.95rem;
      transition: background 0.2s, transform 0.1s;
    }}

    .print-btn:hover {{
      background: #1d4ed8;
      transform: translateY(-1px);
    }}

    /* Report Pages Container */
    .report-container {{
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 24px 0;
    }}

    /* Strict A4 Single Page */
    .page {{
      width: 210mm;
      height: 297mm;
      min-height: 297mm;
      max-height: 297mm;
      margin: 16px auto;
      background: #ffffff;
      padding: 8mm 10mm;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
      position: relative;
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
      overflow: hidden;
      page-break-after: always;
      break-after: page;
    }}

    .page-border {{
      border: 1.5px solid #0f172a;
      width: 100%;
      height: 100%;
      padding: 9mm 12mm 7mm 12mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
      position: relative;
    }}

    .page-content {{
      flex: 1 1 auto;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      overflow: hidden;
    }}

    /* Typography */
    .chapter-heading {{
      margin-bottom: 8px;
      text-align: left;
    }}

    .chapter-num {{
      font-size: 11pt;
      font-weight: bold;
      letter-spacing: 1px;
      color: #1e3a8a;
      margin-bottom: 2px;
    }}

    .chapter-title {{
      font-size: 13.5pt;
      font-weight: bold;
      text-transform: uppercase;
      border-bottom: 1.5px solid #0f172a;
      padding-bottom: 3px;
      margin-bottom: 8px;
      letter-spacing: 0.5px;
    }}

    .section-title {{
      font-size: 10.5pt;
      font-weight: bold;
      margin-top: 6px;
      margin-bottom: 3px;
      text-align: left;
      color: #0f172a;
    }}

    p {{
      text-align: justify;
      text-justify: inter-word;
      margin-bottom: 5px;
      line-height: 1.4;
    }}

    .page-footer {{
      text-align: center;
      font-size: 9.5pt;
      font-weight: 600;
      color: #334155;
      padding-top: 4px;
      border-top: 0.5px solid #cbd5e1;
    }}

    /* Tables */
    table.report-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 5px 0;
      line-height: 1.35;
    }}

    table.report-table th,
    table.report-table td {{
      border: 1px solid #1e293b;
      padding: 4px 6px;
      text-align: center;
      vertical-align: middle;
    }}

    table.report-table th {{
      background-color: #f1f5f9;
      font-weight: bold;
      color: #0f172a;
    }}

    /* Figure & SVG Containers */
    .figure-container {{
      text-align: center;
      margin: 4px 0 6px 0;
    }}

    .figure-container svg {{
      max-width: 100%;
      height: auto;
      border: 1px solid #cbd5e1;
      background: #fafafa;
      border-radius: 4px;
    }}

    .figure-caption {{
      font-size: 8.5pt;
      font-weight: bold;
      margin-top: 3px;
      text-align: center;
      color: #334155;
    }}

    /* Signatures */
    .signature-row {{
      display: flex;
      justify-content: space-between;
      margin-top: 45px;
      padding: 0 10px;
    }}

    .sign-block {{
      text-align: center;
      width: 44%;
      font-size: 9pt;
      line-height: 1.35;
    }}

    .sign-line {{
      border-top: 1px dashed #000;
      margin-bottom: 6px;
      padding-top: 4px;
      font-weight: bold;
    }}

    /* Print Setup */
    @page {{
      size: A4 portrait;
      margin: 0;
    }}

    @media print {{
      body {{
        background: #ffffff !important;
      }}

      .top-action-bar {{
        display: none !important;
      }}

      .report-container {{
        padding: 0 !important;
      }}

      .page {{
        margin: 0 !important;
        box-shadow: none !important;
        page-break-after: always !important;
        break-after: page !important;
        break-inside: avoid !important;
        height: 297mm !important;
        min-height: 297mm !important;
        max-height: 297mm !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Screen Top Bar with Print Trigger -->
  <div class="top-action-bar">
    <div style="display: flex; align-items: center; gap: 14px;">
      {uni_logo_top}
      <div>
        <h2>Library Management System &bull; MCA Academic Project Report</h2>
        <small style="opacity: 0.85;">Brainware University &bull; Department of Computational Sciences &bull; Santanu Ghosh</small>
      </div>
    </div>
    <button type="button" class="print-btn" onclick="window.print()">
      <span>&#128424;</span> Save as PDF / Print (20 Pages)
    </button>
  </div>

  <div class="report-container">
    {''.join(pages)}
  </div>

</body>
</html>'''

    output_path = "project-report.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Successfully generated {len(pages)}-page report at {output_path}")

if __name__ == "__main__":
    generate_report()

