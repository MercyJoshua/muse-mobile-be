from datetime import datetime

from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=255)

class UserLogin(BaseModel):
    email: EmailStr
    password: str    

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    full_name: str
    auth_provider: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str 
    token_type: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str
    