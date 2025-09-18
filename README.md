# 📚 Library Management System

A modern library management system built with FastAPI and Server-Side Rendering (SSR) using Jinja2 templates.

## Features

- **User Management**: Register and manage library users with validation
- **Book Catalog**: Add, edit, and organize book collections
- **Loan System**: Track book loans and returns
- **Authentication**: Secure login and session management
- **Modern UI**: Responsive design with Bootstrap
- **Server-Side Rendering**: Fast page loads with Jinja2 templates

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Templates**: Jinja2 (Server-Side Rendering)
- **Frontend**: Bootstrap 5 + Custom CSS/JS
- **Authentication**: Session-based with secure cookies
- **Development**: Uvicorn server

## 📋 Requirements

- Python 3.8+
- PostgreSQL
- pip or poetry


## 📁 Project Structure

```
library-management/
├── app/
│   ├── handlers/       # HTTP request handlers (controllers)
│   ├── services/       # Business logic layer
│   ├── repositories/   # Data access layer
│   ├── models/         # SQLAlchemy database models
│   ├── schemas/        # Pydantic validation schemas
│   ├── templates/      # Jinja2 HTML templates (SSR)
│   ├── static/         # CSS, JS, and images
│   ├── core/           # Configuration and database setup
│   └── main.py         # Application entry point
├── alembic/            # Database migrations (Alembic)
├── alembic.ini         # Alembic configuration file
├── tests/              # Automated tests (pytest)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # Project documentation
```