# ==========================================
# Import Required Libraries
# ==========================================

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List


# Import Database
from app.database import get_db


# Import Schemas
from app import schemas


# Import CRUD Functions
from app import crud



# ==========================================
# Create Router
# ==========================================

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)



# ==========================================
# CREATE TASK
# POST /tasks
# ==========================================

@router.post(
    "/",
    response_model=schemas.TaskResponse
)
def create_task(
        task: schemas.TaskCreate,
        db: Session = Depends(get_db)
):

    return crud.create_task(
        db,
        task
    )



# ==========================================
# GET ALL TASKS
# GET /tasks
# ==========================================

@router.get(
    "/",
    response_model=List[schemas.TaskResponse]
)
def get_tasks(
        db: Session = Depends(get_db)
):

    return crud.get_tasks(db)



# ==========================================
# UPDATE TASK
# PUT /tasks/{task_id}
# ==========================================

@router.put(
    "/{task_id}",
    response_model=schemas.TaskResponse
)
def update_task(
        task_id: int,
        task: schemas.TaskCreate,
        db: Session = Depends(get_db)
):

    updated_task = crud.update_task(
        db,
        task_id,
        task
    )


    if updated_task is None:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


    return updated_task



# ==========================================
# DELETE TASK
# DELETE /tasks/{task_id}
# ==========================================

@router.delete(
    "/{task_id}"
)
def delete_task(
        task_id: int,
        db: Session = Depends(get_db)
):

    deleted_task = crud.delete_task(
        db,
        task_id
    )


    if deleted_task is None:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


    return {
        "message": "Task deleted successfully"
    }