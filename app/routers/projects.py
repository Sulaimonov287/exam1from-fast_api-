from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import *
from ..crud import *

router = APIRouter(prefix='/projects', tags=['projects'])
DB = Annotated[Session, Depends(get_db)]

@router.post('/', response_model=ProjectResponce)
async def create_project(data: ProjectCreate, db: DB):
    existing = create_project(db, data)

@router.get('/', response_model=list[ProjectResponce])
async def get_project_route(db: DB):
    return get_projects(db)


@router.get('/{id}', response_model=ProjectResponce)
async def get_project_route(id: int, db: DB):
    project = get_project_by_id(db, id)
    if not project:
        raise HTTPException('Project bot found!')
    return project


@router.put('/{id}', response_model=ProjectResponce)
async def update_project_route(id: int, data: ProjectUpdate, db: DB):
    project = get_project_by_id(db, id)
    if not project:
        raise HTTPException('Project not found!')
    return update_project(db, db_project=project, project=data)


@router.delete('/{id}')
async def delete_project_route(id: int, db: DB):
    project = get_project_by_id(db, id)
    if not project:
        raise HTTPException('Project not found!')
    delete_project(db, db_project=project)
    return {'message': 'Project deleted!'}