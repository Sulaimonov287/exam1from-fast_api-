from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str = Field(max_length=120, min_length=1)
    description: str | None = Field(default=None)

class ProjectUpdate(BaseModel):
    name: str|None = Field(max_length=120, min_length=1, default= None)
    description: str|None = Field(default=None)

class ProjectResponce(ProjectCreate):
    id:int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class EmployeCreate(BaseModel):
    full_name: str = Field(max_length=150, min_length=2)
    email: str = Field(max_length=150)
    position: str = Field(max_length=100)
    is_active: bool = True

class EmployeUpdate(BaseModel):
    full_name: str|None = Field(max_length=150, min_length=2, default=None)
    email: str |None = Field(max_length=150, default=None)
    position: str| None = Field(max_length=100, default=None)
    is_active: bool| None = Field(default=None)


class EmployeResponse(EmployeCreate):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class TaskCreate(BaseModel):
    title: str = Field(max_length=200, min_length=1)
    description: str | None = Field(default=None)
    status: str = Field(max_length=20, default='todo')
    priority: int = Field(ge=1, le=5)
    deadline: datetime | None = Field(default=None)
    project_id: int
    employee_id: int | None = Field(default=None)


class TaskUpdate(BaseModel):
    title: str |None = Field(max_length=200, min_length=1, default=None)
    description: str|None = Field(default=None)
    status: str| None = Field(max_length=20, default=None)
    priority: int| None = Field(ge=1, le=5, default=None)
    deadline: datetime |None = Field(default=None)
    project_id: int| None = Field(default=None)
    employee_id: int| None = Field(default=None)


class TaskResponse(TaskCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)