import httpx
from typing import List, Optional
from app.schemas.jsonplaceholder import PostRequest, PostResponse, UserResponse
from app.config.logger import logger


class JSONPlaceholderClient:
    """Client for interacting with the JSONPlaceholder API"""
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    @classmethod
    async def get_posts(cls) -> List[PostResponse]:
        """Get all posts from JSONPlaceholder API"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{cls.BASE_URL}/posts")
                response.raise_for_status()
                return [PostResponse(**post) for post in response.json()]
            except httpx.HTTPError as e:
                logger.error(f"Error fetching posts: {str(e)}")
                raise
    
    @classmethod
    async def get_post(cls, post_id: int) -> Optional[PostResponse]:
        """Get a specific post by ID from JSONPlaceholder API"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{cls.BASE_URL}/posts/{post_id}")
                response.raise_for_status()
                return PostResponse(**response.json())
            except httpx.HTTPError as e:
                logger.error(f"Error fetching post {post_id}: {str(e)}")
                raise
    
    @classmethod
    async def create_post(cls, post_data: PostRequest) -> PostResponse:
        """Create a new post on JSONPlaceholder API"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{cls.BASE_URL}/posts",
                    json=post_data.model_dump()
                )
                response.raise_for_status()
                return PostResponse(**response.json())
            except httpx.HTTPError as e:
                logger.error(f"Error creating post: {str(e)}")
                raise
    
    @classmethod
    async def get_user(cls, user_id: int) -> Optional[UserResponse]:
        """Get a specific user by ID from JSONPlaceholder API"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{cls.BASE_URL}/users/{user_id}")
                response.raise_for_status()
                return UserResponse(**response.json())
            except httpx.HTTPError as e:
                logger.error(f"Error fetching user {user_id}: {str(e)}")
                raise
