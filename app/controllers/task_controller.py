from fastapi import Depends, Query, Path, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.task import TaskResponse, TaskCreate, TaskUpdate
from app.services.task_service import TaskService
from app.config.database import get_db

class TaskController:
    """
    Controller for handling task-related HTTP requests
    """
    
    @staticmethod
    async def get_tasks(
        skip: int = Query(0, ge=0, description="Number of tasks to skip"),
        limit: int = Query(100, ge=1, le=100, description="Maximum number of tasks to return"),
        db: Session = Depends(get_db)
    ) -> List[TaskResponse]:
        """
        Get all tasks with pagination
        """
        return await TaskService.get_tasks(db, skip, limit)
    
    @staticmethod
    async def get_task(
        task_id: int = Path(..., gt=0, description="The ID of the task to retrieve"),
        db: Session = Depends(get_db)
    ) -> TaskResponse:
        """
        Get a task by ID
        """
        return await TaskService.get_task(db, task_id)
    
    @staticmethod
    async def create_task(
        task_data: TaskCreate,
        db: Session = Depends(get_db)
    ) -> TaskResponse:
        """
        Create a new task
        """
        return await TaskService.create_task(db, task_data)
    
    @staticmethod
    async def update_task(
        task_id: int = Path(..., gt=0, description="The ID of the task to update"),
        task_data: TaskUpdate = ...,
        db: Session = Depends(get_db)
    ) -> TaskResponse:
        """
        Update an existing task
        """
        return await TaskService.update_task(db, task_id, task_data)
    
    @staticmethod
    async def delete_task(
        task_id: int = Path(..., gt=0, description="The ID of the task to delete"),
        db: Session = Depends(get_db)
    ) -> None:
        """
        Delete a task
        """
        await TaskService.delete_task(db, task_id)
