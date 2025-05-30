from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session

from app.controllers.task_controller import TaskController
from app.schemas.task import TaskResponse, TaskCreate, TaskUpdate
from app.config.database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get(
    "",
    response_model=List[TaskResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all tasks",
    description="Retrieve a list of all tasks with pagination"
)
async def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all tasks with pagination
    """
    return await TaskController.get_tasks(skip=skip, limit=limit, db=db)

@router.get(
    "/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a task by ID",
    description="Retrieve a specific task by its ID"
)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Get a task by ID
    """
    return await TaskController.get_task(task_id=task_id, db=db)

@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Create a new task with the provided data"
)
async def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task
    """
    return await TaskController.create_task(task_data=task_data, db=db)

@router.patch(
    "/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
    summary="Update a task",
    description="Update an existing task with the provided data"
)
async def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    """
    Update an existing task
    """
    return await TaskController.update_task(task_id=task_id, task_data=task_data, db=db)

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
    description="Delete a task by its ID"
)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task
    """
    await TaskController.delete_task(task_id=task_id, db=db)
