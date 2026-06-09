"""
Pydantic schemas for request/response validation
"""
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class HealthCheck(BaseModel):
    """Health check response"""
    status: str
    service: str
    version: str


class CodeGenerationRequest(BaseModel):
    """Code generation request"""
    prompt: str = Field(..., min_length=1, max_length=5000)
    language: str = Field(default="python")
    context: Optional[str] = None


class CodeGenerationResponse(BaseModel):
    """Code generation response"""
    id: str
    prompt: str
    language: str
    code: str
    created_at: str


class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema"""
    password: str = Field(..., min_length=8)


class UserResponse(UserBase):
    """User response schema"""
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Token response"""
    access_token: str
    token_type: str = "bearer"


class ErrorResponse(BaseModel):
    """Error response"""
    detail: str
    error_code: Optional[str] = None
