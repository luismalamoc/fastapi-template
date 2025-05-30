from pydantic import BaseModel, Field
from typing import Optional, List


class PostBase(BaseModel):
    """Base schema for post data from JSONPlaceholder API"""
    title: str = Field(..., description="Post title")
    body: str = Field(..., description="Post content")


class PostRequest(PostBase):
    """Schema for creating a new post request to JSONPlaceholder API"""
    userId: int = Field(..., description="User ID associated with the post")


class PostResponse(PostBase):
    """Schema for post response from JSONPlaceholder API"""
    id: int = Field(..., description="Post ID")
    userId: int = Field(..., description="User ID associated with the post")


class UserAddress(BaseModel):
    """Schema for user address from JSONPlaceholder API"""
    street: str
    suite: str
    city: str
    zipcode: str
    geo: dict


class UserCompany(BaseModel):
    """Schema for user company from JSONPlaceholder API"""
    name: str
    catchPhrase: str
    bs: str


class UserResponse(BaseModel):
    """Schema for user response from JSONPlaceholder API"""
    id: int
    name: str
    username: str
    email: str
    address: UserAddress
    phone: str
    website: str
    company: UserCompany
