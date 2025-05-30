from app.schemas.task import TaskBase, TaskCreate, TaskUpdate, TaskResponse
from app.schemas.jsonplaceholder import PostBase, PostRequest, PostResponse, UserResponse, UserAddress, UserCompany, GeoLocation

__all__ = [
    # Task schemas
    "TaskBase", "TaskCreate", "TaskUpdate", "TaskResponse",
    # JSONPlaceholder schemas
    "PostBase", "PostRequest", "PostResponse", "UserResponse", 
    "UserAddress", "UserCompany", "GeoLocation"
]
