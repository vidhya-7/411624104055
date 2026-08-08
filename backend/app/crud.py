# ==========================================
# Import Required Libraries
# ==========================================

from sqlalchemy.orm import Session

from app import models, schemas


# ==========================================
# CREATE TASK
# ==========================================

def create_task(
        db: Session,
        task: schemas.TaskCreate
):

    new_task = models.Task(
        task=task.task
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task



# ==========================================
# GET ALL TASKS
# ==========================================

def get_tasks(db: Session):

    return db.query(models.Task).all()



# ==========================================
# GET SINGLE TASK
# ==========================================

def get_task(
        db: Session,
        task_id: int
):

    return (
        db.query(models.Task)
        .filter(models.Task.id == task_id)
        .first()
    )



# ==========================================
# UPDATE TASK
# ==========================================

def update_task(
        db: Session,
        task_id: int,
        task_data: schemas.TaskCreate
):

    existing_task = get_task(
        db,
        task_id
    )


    if existing_task:

        existing_task.task = task_data.task

        db.commit()

        db.refresh(existing_task)


    return existing_task



# ==========================================
# DELETE TASK
# ==========================================

def delete_task(
        db: Session,
        task_id: int
):

    existing_task = get_task(
        db,
        task_id
    )


    if existing_task:

        db.delete(existing_task)

        db.commit()


    return existing_task