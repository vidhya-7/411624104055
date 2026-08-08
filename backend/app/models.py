# ==========================================
# Import Required Libraries
# ==========================================

from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.sql import func

# Import Base from database
from app.database import Base


# ==========================================
# Task Table Model
# ==========================================

class Task(Base):

    __tablename__ = "tasks"


    # Primary Key
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # Task content
    task = Column(
        String(255),
        nullable=False
    )


    # Created Time
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )