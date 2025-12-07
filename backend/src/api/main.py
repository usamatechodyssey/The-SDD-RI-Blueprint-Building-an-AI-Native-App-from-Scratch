#backend/src/api/main.py
from fastapi import FastAPI
from backend.src.api.middleware.rate_limiter import RateLimitMiddleware
from backend.src.api.endpoints import book_generation, book_deployment

app = FastAPI()

app.add_middleware(RateLimitMiddleware)

app.include_router(book_generation.router)
app.include_router(book_deployment.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Generated Docusaurus Book API!"}
