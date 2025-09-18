from sqlalchemy.orm import Session
from app.models.book import Book


def create_book(db: Session, title: str, author: str, year: int, isbn: str) -> Book:
    book = Book(title=title, author=author, year=year, isbn=isbn)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, **kwargs):
    book = get_book_by_id(db, book_id)
    if not book:
        return None
    for key, value in kwargs.items():
        if hasattr(book, key):
            setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book
