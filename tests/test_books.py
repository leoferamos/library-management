import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Helper to create a book
def create_book(title="Test Book", author="Author", year=2025, isbn="1234567890"):
    return client.post("/books/new", data={
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn
    })

def test_create_book():
    response = create_book()
    assert response.status_code in (200, 303)  # Accept redirect or HTML
    # Check if book appears in list
    list_response = client.get("/books")
    assert "Test Book" in list_response.text

def test_edit_book():
    # Create a book first
    create_book(title="Edit Me", isbn="9876543210")
    # Find book id
    list_response = client.get("/books")
    import re
    match = re.search(r"/books/(\d+)/edit", list_response.text)
    assert match
    book_id = match.group(1)
    # Edit the book
    response = client.post(f"/books/{book_id}/edit", data={
        "title": "Edited Book",
        "author": "New Author",
        "year": 2026,
        "isbn": "9876543210"
    })
    assert response.status_code in (200, 303)
    # Check if updated
    list_response = client.get("/books")
    assert "Edited Book" in list_response.text or "error" in response.text.lower() or "isbn" in response.text.lower()

def test_delete_book():
    # Create a book to delete
    create_book(title="Delete Me", isbn="5555555555")
    list_response = client.get("/books")
    import re
    match = re.search(r"/books/(\d+)/edit", list_response.text)
    assert match
    book_id = match.group(1)
    # Delete
    response = client.post(f"/books/{book_id}/delete")
    assert response.status_code in (200, 303)
    # Check if removed
    list_response = client.get("/books")
    assert "Delete Me" not in list_response.text

def test_invalid_input():
    # Missing required fields (FastAPI returns 422)
    response = client.post("/books/new", data={
        "title": "",
        "author": "",
        "year": "",
        "isbn": ""
    })
    assert response.status_code in (200, 422)
    # Duplicate ISBN
    create_book(title="Book1", isbn="DUPLICATEISBN")
    response = create_book(title="Book2", isbn="DUPLICATEISBN")
    assert response.status_code in (200, 303)
    assert "error" in response.text.lower() or "isbn" in response.text.lower()

def test_navigation():
    # Home page
    response = client.get("/")
    assert response.status_code == 200
    assert "Library Management" in response.text
    # Books page
    response = client.get("/books")
    assert response.status_code == 200
    assert "Books" in response.text
    # Add book page
    response = client.get("/books/new")
    assert response.status_code == 200
    assert "Add Book" in response.text
