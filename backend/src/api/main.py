from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- Yeh line add karein
from backend.src.api.endpoints import book_generation, book_deployment, admin_api

app = FastAPI(title="AI-Native Book CMS")

# --- CORS SETUP START ---
# Yeh aapki website ko backend se baat karne ki ijazat deta hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hackathon ke liye "*" best hai (Allow all)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- CORS SETUP END ---

app.include_router(book_generation.router)
app.include_router(book_deployment.router)
app.include_router(admin_api.router)

@app.get("/")
def root():
    return {"message": "Admin CMS is Live!"}