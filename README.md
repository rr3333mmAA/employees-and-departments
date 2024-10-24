# Employee Department Structure

## Overview

This project is a Django web application that displays a tree-like structure of departments, each containing a list of employees. The application utilizes Bootstrap for styling and interactive components, allowing users to expand departments to view associated employees.

## Features

- **Hierarchical Department Structure**: Visual representation of departments and sub-departments up to 5 levels deep.
- **Employee List**: Displays detailed information about employees, including:
  - Full Name
  - Position
  - Hire Date
  - Salary
- **Expandable Sections**: Clickable department names to expand associated sub-departments.
- **CRUD Operations**: Manage departments and employees through Django's admin interface.

## Requirements

- Python 3.12
- Django 4.2.16
- PostgreSQL
- Bootstrap 5

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rr3333mmAA/employees-and-departments
    cd employees-and-departments
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL**:
   - Ensure PostgreSQL is installed and running.
   - Run the PostgreSQL interactive terminal:
     ```bash
     psql
     ```
   - Create a database:
     ```sql
     CREATE DATABASE database_name;
     ```
   - Quit the PostgreSQL terminal:
     ```sql
     \q
     ```
   - Create a `.env` file in the project root directory and add the following environment variables:
     ```bash
     # .env
     DB_NAME=<your_db_name>
     DB_USER=<your_db_user>
     DB_PASSWORD=<your_db_password>
     DB_HOST=<your_db_host>
     DB_PORT=<your_db_port>
     ```

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```
   
7. **Generate data** (optional):
    ```bash
    python manage.py generate_data   
    # It generates 25 departments and 50000 employees.
    # P.S. It may take a while :)
    ```

8. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

9. **Access the application**:
   - Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

- **Admin Interface**: Log in to the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to manage departments and employees.
- **Expanding Sections**: Click on department names to expand sections.

## Technologies Used

- Django
- PostgreSQL
- Bootstrap 5
- HTML/CSS/JavaScript
