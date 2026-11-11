from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, Optional
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Task, Project, Employe
from ..schemas import TaskCreate, TaskUpdate, TaskResponse
from ..crud import *

router = APIRouter(prefix='/tasks', tags=['Tasks'])
DB = Annotated[Session, Depends(get_db)]


@router.post('/', response_model=TaskResponse)
async def create_task_route(data: TaskCreate, db: DB):
    if not db.query(Project).filter(Project.id == data.project_id).first():
        raise HTTPException( 'Project not found!')
    if data.employee_id is not None:
        if not db.query(Employe).filter(Employe.id == data.employee_id).first():
            raise HTTPException(404, 'Employee not found!')
    return create_task_db(db, data)


@router.get('/{id}', response_model=TaskResponse)
async def get_task_route(id: int, db: DB):
    task = get_task_by_id(db, id)
    if not task:
        raise HTTPException( 'Task not found!')
    return task


@router.put('/{id}', response_model=TaskResponse)
async def update_task_put(id: int, data: TaskUpdate, db: DB):
    task = get_task_by_id(db, id)
    if not task:
        raise HTTPException( 'Task not found!')
    return update_task_put(db, db_task=task, task=data)


@router.patch('/{id}', response_model=TaskResponse)
async def update_task_patch(id: int, data: TaskUpdate, db: DB):
    task = get_task_by_id(db, id)
    if not task:
        raise HTTPException('Task not found!')
    return update_task_patch(db, db_task=task, task=data)


@router.delete('/{id}')
async def delete_task_route(id: int, db: DB):
    task = get_task_by_id(db, id)
    if not task:
        raise HTTPException('Task not found!')
    delete_task(db, db_task=task)
    return {'message': 'Task deleted!'}