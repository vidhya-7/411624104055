# ==========================================
# Import Required Libraries
# ==========================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import Router
from app.routers.tasks import router as task_router

# Import Database
from app.database import engine
from app.database import Base

from app import models

# Import Models
from app.models import Base

# ==========================================
# Create Database Tables
# ==========================================

Base.metadata.create_all(bind=engine)

# ==========================================
# Create FastAPI Application
# ==========================================

app = FastAPI(
    title="Note App API",
    description="CRUD API using FastAPI and MySQL",
    version="1.0.0"
)

# ==========================================
# Enable CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],   # React Frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# Default Route
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Welcome to Note App API"
    }

# ==========================================
# Register Task Router
# ==========================================

app.include_router(task_router)