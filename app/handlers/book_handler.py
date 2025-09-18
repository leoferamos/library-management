from fastapi import APIRouter, Request, Depends, Form, status, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.book_service import (
    create_book_service,
    get_books_service,
    get_book_by_id_service,
    update_book_service,
    delete_book_service,
    BookNotFoundError
)
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/books", response_class=HTMLResponse)
def list_books(request: Request, db: Session = Depends(get_db)):
    books = get_books_service(db)
    return templates.TemplateResponse("books/list.html", {"request": request, "books": books})

@router.get("/books/new", response_class=HTMLResponse)
def new_book_form(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})

@router.post("/books/new")
def create_book(request: Request, db: Session = Depends(get_db),
                title: str = Form(...), author: str = Form(...), year: int = Form(...), isbn: str = Form(...)):
    try:
        create_book_service(db, title, author, year, isbn)
        return RedirectResponse("/books", status_code=status.HTTP_303_SEE_OTHER)
    except Exception as e:
        return templates.TemplateResponse("books/new.html", {"request": request, "error": str(e)})

@router.get("/books/{book_id}/edit", response_class=HTMLResponse)
def edit_book_form(request: Request, book_id: int, db: Session = Depends(get_db)):
    try:
        book = get_book_by_id_service(db, book_id)
        return templates.TemplateResponse("books/edit.html", {"request": request, "book": book})
    except BookNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/books/{book_id}/edit")
def update_book(request: Request, book_id: int, db: Session = Depends(get_db),
                title: str = Form(...), author: str = Form(...), year: int = Form(...), isbn: str = Form(...)):
    try:
        update_book_service(db, book_id, title=title, author=author, year=year, isbn=isbn)
        return RedirectResponse("/books", status_code=status.HTTP_303_SEE_OTHER)
    except BookNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return templates.TemplateResponse("books/edit.html", {"request": request, "book_id": book_id, "error": str(e)})

@router.post("/books/{book_id}/delete")
def delete_book(request: Request, book_id: int, db: Session = Depends(get_db)):
    try:
        delete_book_service(db, book_id)
        return RedirectResponse("/books", status_code=status.HTTP_303_SEE_OTHER)
    except BookNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
