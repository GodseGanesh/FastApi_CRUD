from fastapi import FastAPI
from app.routes import books
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Review API")

app.include_router(books.router)
