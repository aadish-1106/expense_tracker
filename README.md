# Expense Tracker (Django Web Application)

A Django-based web application that allows users to manage daily expenses.
This project was built to apply and demonstrate core Django concepts such as
models, views, templates, URL routing, and database integration.

---

## Features
- Add new expense records
- View a list of all expenses
- Edit existing expenses
- Delete expenses
- Persistent data storage using SQLite

---

## Tech Stack
- Python
- Django
- SQLite
- HTML (Django Templates)

---

## Project Structure
expense_tracker/
├── manage.py
├── expense_tracker/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── expenses/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ └── expenses/
│ ├── list.html
│ ├── add.html
│ └── edit.html
└── db.sqlite3


---

## Purpose
This project was created as a learning-focused application to strengthen
understanding of Django fundamentals and CRUD-based web development.
