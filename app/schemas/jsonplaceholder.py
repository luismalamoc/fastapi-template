from pydantic import BaseModel, Field
from typing import Optional, Dict


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


class GeoLocation(BaseModel):
    """Schema for geographic location data"""
    lat: str = Field(..., description="Latitude")
    lng: str = Field(..., description="Longitude")


class UserAddress(BaseModel):
    """Schema for user address from JSONPlaceholder API"""
    street: str = Field(..., description="Street name")
    suite: str = Field(..., description="Suite or apartment number")
    city: str = Field(..., description="City name")
    zipcode: str = Field(..., description="Postal code")
    geo: GeoLocation = Field(..., description="Geographic coordinates")


class UserCompany(BaseModel):
    """Schema for user company from JSONPlaceholder API"""
    name: str = Field(..., description="Company name")
    catchPhrase: str = Field(..., description="Company catch phrase")
    bs: str = Field(..., description="Company business strategy")


class UserResponse(BaseModel):
    """Schema for user response from JSONPlaceholder API"""
    id: int = Field(..., description="User ID")
    name: str = Field(..., description="Full name")
    username: str = Field(..., description="Username")
    email: str = Field(..., description="Email address")
    address: UserAddress = Field(..., description="User address information")
    phone: str = Field(..., description="Phone number")
    website: str = Field(..., description="Website URL")
    company: UserCompany = Field(..., description="Company information")
