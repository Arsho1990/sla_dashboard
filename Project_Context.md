# Project Context
Version: 1.0

# Project Name

Bank SLA & License Dashboard

---

# Technology

Python 3.13

Flask

Oracle Database

HTML

Bootstrap 5

Chart.js

Javascript

Jinja2

---

# Database

Oracle

Connection is already implemented inside app.py

Always use

conn = get_connection()

Never change existing connection logic.

---

# Existing Pages

Login

Dashboard

License Dashboard

SLA Dashboard

Register User

Logout

Base Template

---

# User Roles

Admin

Viewer

Admin can

- Add records
- Edit records
- Update records

Viewer can only

- View
- Filter
- See charts

Never allow Viewer to edit.

---

# Important Rule

Do NOT modify existing working functionality unless specifically requested.

Whenever adding a feature:

- keep previous logic
- keep previous routes
- keep previous calculations
- keep previous UI

Never rewrite existing code unnecessarily.

---

# UI Standard

Theme color

Purple (#4B0082)

Background

White

Tables

Bootstrap

Headers

Purple

Buttons

Purple

Text

Keep formatting exactly same as existing pages.

Use base.html.

Never redesign pages.

---

# Navigation

Dashboard

Licenses

SLA

Logout

Must remain exactly same.

---

# Logo

Avanza logo

Location

static/avanza-logo.png

Bank logos

static/logos/

Logo filename is generated from BANK_NAME.

Do not change this logic.

---

# SLA Table

Table name

BANK_SLA

Columns

BANK_NAME

CURRENCY_MODE

SLA_YEAR

CURRENT_YEAR_COST

LAST_YEAR_COST

ADDITIONAL_ITEMS_COST

SLA_INCREMENT

SLA_INCREMENT_WITH_ADDITION

INCREMENT_PER

INCREMENT_PER_WITH_ADDITION

CREATED_AT

UPDATED_AT

---

# SLA Calculations

Increment

CURRENT_YEAR_COST
-
LAST_YEAR_COST

Increment With Addition

Increment
+
ADDITIONAL_ITEMS_COST

Increment %

((CURRENT_YEAR_COST
-
ADDITIONAL_ITEMS_COST)
/
LAST_YEAR_COST)
*
100

Increment % With Addition

((CURRENT_YEAR_COST
-
LAST_YEAR_COST)
/
LAST_YEAR_COST)
*
100

These formulas must never be changed.

---

# SLA Filters

Bank

comes from SLA table

Currency

comes from SLA table

Year

Static list

2023

2024

2025

2026

2027

Do NOT fetch year from database.

---

# SLA Add Record

Only Admin.

Fields

Bank

Currency

Year

Current Cost

Last Cost

Additional Items Cost

When saved

Automatically calculate

Increment

Increment With Addition

Increment %

Increment % With Addition

Store all values in BANK_SLA.

---

# SLA Grid

Viewer

Read Only

Admin

Editable

Editable fields

Currency

Year

Current Cost

Last Cost

Additional Items Cost

After edit

Automatically recalculate

Increment

Increment With Addition

Increment %

Increment % With Addition

Update Oracle immediately.

No page redesign.

---

# SLA Charts

Use Chart.js

Chart Type

Bar Chart

Never use Line Chart.

Charts automatically update using filters.

Charts required

1)

Increment %

Exclusive Additional

vs

Increment %

Inclusive Additional

Grouped Bar Chart

2)

Currency Totals

USD

PKR

Year Wise

Bar Chart

Fields

Current Cost

Last Cost

Additional Items Cost

Increment

Increment With Addition

---

# Graph Behaviour

If Bank filter is selected

Chart title must show

Selected Bank Name

Example

Meezan Bank (PKR)

above graph.

Bars should represent

2023

2024

2025

etc.

If All Banks selected

Show

All Banks

above chart.

---

# Editing Rules

Never make whole table editable.

Only specified fields.

Keep numeric formatting.

Thousands separator.

Percent with %

---

# Project Structure

app.py

templates/

static/

uploads/

base.html

Do not move files.

Do not rename routes.

---

# Existing Routes

/login

/logout

/dashboard

/licenses

/register

/sla

/add_sla

/update_sla

Keep route names unchanged.

---

# Coding Standard

Never duplicate routes.

Never duplicate JavaScript.

Never duplicate CSS.

Reuse existing code.

Use Flask best practices.

---

# Error Handling

Always use try/except.

Rollback Oracle transaction on failure.

Commit only after successful update.

Close cursor.

Close connection.

---

# Jinja Rules

Do not break existing template.

Use

{% extends "base.html" %}

Use blocks correctly.

Do not duplicate HTML tags.

---

# JavaScript Rules

Chart.js only.

Avoid duplicate chart creation.

Destroy existing chart before redraw.

Use fetch() for AJAX updates.

---

# Oracle Rules

Parameterized queries only.

Never use string concatenation.

---

# Formatting

Currency

1,234,567

Percent

12.34%

---

# Before Suggesting Any Change

Always:

Understand current implementation.

Modify only requested section.

Preserve existing functionality.

Avoid breaking routes.

Avoid breaking templates.

Avoid changing calculations unless explicitly requested.

Always explain where code should be inserted.

Never replace whole files when only a small modification is needed.
