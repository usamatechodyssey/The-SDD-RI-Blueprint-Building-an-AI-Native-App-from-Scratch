from fastapi import FastAPI
from backend.src.api.endpoints import book_generation, book_deployment, admin_api # <-- Naya import

app = FastAPI(title="AI-Native Book CMS")

# Routers
app.include_router(book_generation.router)
app.include_router(book_deployment.router)
app.include_router(admin_api.router) # <-- Register karein

@app.get("/")
def root():
    return {"message": "Admin CMS is Live!"}