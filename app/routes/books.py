from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app import crud, schemas, cache
from typing import List
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books", response_model=List[schemas.BookOut])
async def read_books(db: Session = Depends(get_db)):
    cached, status = await cache.get_books()

    if cached:
        print(f"Cache {status.upper()} — Serving books from Redis")
        books = json.loads(cached)
        return books
        return cached
    
    print(f"Cache {status.upper()} — Fetching books from Database")
    books = crud.get_books(db)
    result = [schemas.BookOut.from_orm(book) for book in books]
    await cache.set_cached_books([book.dict() for book in result])
    return result


@router.post("/books", response_model=schemas.BookOut)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/books/{id}/reviews", response_model=List[schemas.ReviewOut])
def read_reviews(id: int, db: Session = Depends(get_db)):
    return crud.get_reviews(db, id)

@router.post("/books/{id}/reviews", response_model=schemas.ReviewOut)
def add_review(id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, id, review)
