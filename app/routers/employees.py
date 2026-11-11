from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import *
from ..crud import *

router = APIRouter(prefix='/employees', tags=['Employees'])
DB = Annotated[Session, Depends(get_db)]


@router.post('/', response_model=EmployeResponse)
async def create_employee_route(data: EmployeCreate, db: DB):
    return create_employee(db, data)


@router.get('/', response_model=list[EmployeResponse])
async def get_employees_route(db: DB):
    return get_employees(db)


@router.get('/{id}', response_model=EmployeResponse)
async def get_employee_route(id: int, db: DB):
    employee = get_employee_by_id(db, id)
    if not employee:
        raise HTTPException( 'Employee not found!')
    return employee


@router.put('/{id}', response_model=EmployeResponse)
async def update_employee_route(id: int, data: EmployeUpdate, db: DB):
    employee = get_employee_by_id(db, id)
    if not employee:
        raise HTTPException('Employee not found!')
    return update_employee(db, db_employee=employee, employee=data)


@router.delete('/{id}')
async def delete_employee_route(id: int, db: DB):
    employee = get_employee_by_id(db, id)
    if not employee:
        raise HTTPException(404, 'Employee not found!')
    delete_employee_db(db, db_employee=employee)
    return {'message': 'Employee deleted!'}