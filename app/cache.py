import redis.asyncio as redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

async def get_books():
    books = await r.get("books")
    status = "hit" if books else "miss"
    return books, status


async def set_cached_books(books: list):
    import json
    await r.set("books", json.dumps(books))
