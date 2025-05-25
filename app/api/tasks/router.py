from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.api.tasks.schemas import TaskResponse, TaskCreate, TaskUpdate
from app.api.tasks.service import TaskService
from app.dependencies.database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get(
    "",
    response_model=List[TaskResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all tasks",
    description="Retrieve a list of all tasks with pagination"
)
async def get_tasks(
    skip: int = Query(0, ge=0, description="Number of tasks to skip"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of tasks to return"),
    db: Session = Depends(get_db)
):
    """
    Get all tasks with pagination
    """
    return await TaskService.get_tasks(db, skip, limit)

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
    return await TaskService.get_task(db, task_id)

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
    return await TaskService.create_task(db, task_data)

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
    return await TaskService.update_task(db, task_id, task_data)

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
    await TaskService.delete_task(db, task_id)
