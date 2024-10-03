from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

# Enum for task categories
class TaskCategory(str, Enum):
    work = "Work"
    personal = "Personal"
    study = "Study"
    shopping = "Shopping"

# User models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    password: str

# Token models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Task models
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str = "pending"
    due_date: Optional[datetime] = None
    category: TaskCategory = TaskCategory.work
    assigned_to: str
