# ==========================================
# Import Required Libraries
# ==========================================

from pydantic import BaseModel
from datetime import datetime


# ==========================================
# Base Task Schema
# ==========================================

class TaskBase(BaseModel):

    task: str



# ==========================================
# Schema For Creating Task
# ==========================================

class TaskCreate(TaskBase):

    pass



# ==========================================
# Schema For Response
# ==========================================

class TaskResponse(TaskBase):

    id: int
    created_at: datetime


    class Config:
        from_attributes = True