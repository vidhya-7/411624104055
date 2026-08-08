# ==========================================
# Import Required Libraries
# ==========================================

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

# ==========================================
# Read Database Configuration
# ==========================================

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# ==========================================
# MySQL Database URL
# ==========================================

from urllib.parse import quote_plus
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}/{DB_NAME}"
)
# ==========================================
# Create SQLAlchemy Engine
# ==========================================

engine = create_engine(
    DATABASE_URL,
    echo=True
)

# ==========================================
# Create Session Factory
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ==========================================
# Base Class
# ==========================================

Base = declarative_base()

# ==========================================
# Dependency for FastAPI
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()