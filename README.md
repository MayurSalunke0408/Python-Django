# Django Student Management App

A **Django-based web application** built to demonstrate core backend
development concepts using Python. This project implements Django's
**MVT (Model--View--Template) architecture** to create a simple student
data management system.

The application allows users to **submit student information through a
web form and store it in a database**, while administrators can manage
records through the Django admin panel.

## Key Highlights

-   Built using **Python and Django Framework**
-   Implements **Django ORM for database interaction**
-   Uses **ModelForm for efficient form handling**
-   Demonstrates **MVT architecture**
-   Integrated **Django Admin Panel**
-   Organized project structure following **best backend development
    practices**

## Features

-   Student registration form
-   Data validation using Django Forms
-   Database integration using Django Models
-   Dynamic HTML rendering with Templates
-   Static CSS styling
-   Admin interface for managing records

## Tech Stack

-   **Python**
-   **Django**
-   **HTML**
-   **CSS**
-   **SQLite (Default Django Database)**

## Project Structure

    student_info/
    │
    ├── students/
    │   ├── models.py
    │   ├── forms.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    │
    └── manage.py

## Setup Instructions

### 1. Create Virtual Environment

    python -m venv myenv

### 2. Activate Environment

    myenv\Scripts\activate

### 3. Install Dependencies

    pip install django

### 4. Run Database Migrations

    python manage.py makemigrations
    python manage.py migrate

### 5. Run Development Server

    python manage.py runserver

## Application URLs

Student Form:

    http://127.0.0.1:8000/students/new/

Admin Dashboard:

    http://127.0.0.1:8000/admin/

## Learning Outcomes

-   Understanding Django project and app architecture
-   Working with Django ORM and database models
-   Handling forms using ModelForms
-   Implementing views and templates for dynamic web pages
-   Managing application data using Django Admin
