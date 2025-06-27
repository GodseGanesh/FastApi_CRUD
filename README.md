# FastApi_CRUD

# Book Review API

This is a simple Book Review API built with FastAPI. It uses PostgreSQL to store book and review data, and Redis to cache the book list for faster reads. SQLAlchemy is used as the ORM to interact with the database, and Alembic handles database migrations. Pydantic is used for data validation. This API allows you to list books, add new books, and add reviews for books.

## Features

- List all books
- Create new books
- Add reviews for books
- Fetch reviews for a specific book
- Redis-based caching for faster book listing
- Alembic migrations for managing database schema

## Technologies Used

- FastAPI (web framework)
- SQLAlchemy (ORM)
- PostgreSQL (database)
- Alembic (migrations)
- Redis (caching)
- Pydantic (data validation)

## Project Structure

app/
routes/
books.py # API endpoints for books and reviews
models.py # SQLAlchemy models
schemas.py # Pydantic schemas
crud.py # CRUD database operations
db.py # database session and engine
cache.py # Redis cache helper functions
alembic/
versions/ # Alembic migration scripts
alembic.ini
main.py # FastAPI app entry point




## How to Run

1. Clone this repository:
git clone <your-repo-url>
cd <your-repo-folder>

2. Create a virtual environment and activate it:
python -m venv .venv
.venv\Scripts\activate # on Windows
source .venv/bin/activate # on Linux/Mac

3. Install dependencies:
pip install -r requirements.txt

4. Configure your environment variables:
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/mydb
Add this line in a `.env` file in the project root.

5. Apply migrations:

6. Start Redis:
- using Docker:
  docker run -p 6379:6379 redis

7. Run the FastAPI server:
uvicorn main:app --reload

8. Open your browser at:
http://127.0.0.1:8000/docs
to access the Swagger UI.







## How Caching Works

When you request the list of books, the API first checks Redis for cached data. If the cache is available (cache hit), it returns the books from Redis. If the cache is empty (cache miss), it queries the PostgreSQL database, returns the data, and stores it in Redis for future requests. When a new book is added, the Redis cache is cleared to ensure fresh data on the next request.

## Short Explanation of Files

- **models.py** defines the tables for books and reviews.
- **schemas.py** contains Pydantic schemas for request/response validation.
- **crud.py** handles database logic for creating and retrieving books and reviews.
- **db.py** configures the SQLAlchemy connection and session.
- **cache.py** handles Redis get, set, and clear functions.
- **routes/books.py** contains the API routes and integrates caching.
- **main.py** is the entry point where the FastAPI app is initialized and routes are registered.

## Notes

- PostgreSQL must be running on port 5432
- Redis must be running on port 6379
- Alembic migrations must be applied before starting the API
