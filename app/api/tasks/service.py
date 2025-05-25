from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.task import Task
from app.api.tasks.schemas import TaskCreate, TaskUpdate, TaskResponse
from app.utils.exceptions import NotFoundException

class TaskService:
    """
    Service for handling task operations
    """
    
    @staticmethod
    def _to_response(task: Task) -> TaskResponse:
        """
        Convert Task ORM model to TaskResponse schema
        """
        return TaskResponse.model_validate(task)
    
    @staticmethod
    async def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[TaskResponse]:
        """
        Get all tasks with pagination
        """
        tasks = db.query(Task).offset(skip).limit(limit).all()
        return [TaskService._to_response(task) for task in tasks]
    
    @staticmethod
    async def get_task(db: Session, task_id: int) -> TaskResponse:
        """
        Get a task by ID
        """
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise NotFoundException(f"Task with ID {task_id} not found")
        return TaskService._to_response(task)
    
    @staticmethod
    async def create_task(db: Session, task_data: TaskCreate) -> TaskResponse:
        """
        Create a new task
        """
        task = Task(**task_data.model_dump())
        db.add(task)
        db.commit()
        db.refresh(task)
        return TaskService._to_response(task)
    
    @staticmethod
    async def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> TaskResponse:
        """
        Update an existing task
        """
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise NotFoundException(f"Task with ID {task_id} not found")
        
        # Update only provided fields
        update_data = task_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)
        
        db.commit()
        db.refresh(task)
        return TaskService._to_response(task)
    
    @staticmethod
    async def delete_task(db: Session, task_id: int) -> None:
        """
        Delete a task
        """
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise NotFoundException(f"Task with ID {task_id} not found")
        db.delete(task)
        db.commit()
