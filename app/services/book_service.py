from sqlalchemy.orm import Session
from app.repositories.book_repo import (
    create_book as repo_create_book,
    get_books as repo_get_books,
    get_book_by_id as repo_get_book_by_id,
    update_book as repo_update_book,
    delete_book as repo_delete_book,
)

class BookNotFoundError(Exception):
    pass

def create_book_service(db: Session, title: str, author: str, year: int, isbn: str):
    return repo_create_book(db, title, author, year, isbn)

def get_books_service(db: Session):
    return repo_get_books(db)

def get_book_by_id_service(db: Session, book_id: int):
    book = repo_get_book_by_id(db, book_id)
    if not book:
        raise BookNotFoundError(f"Book with id {book_id} not found.")
    return book

def update_book_service(db: Session, book_id: int, **kwargs):
    book = repo_update_book(db, book_id, **kwargs)
    if not book:
        raise BookNotFoundError(f"Book with id {book_id} not found.")
    return book

def delete_book_service(db: Session, book_id: int):
    book = repo_delete_book(db, book_id)
    if not book:
        raise BookNotFoundError(f"Book with id {book_id} not found.")
    return book
