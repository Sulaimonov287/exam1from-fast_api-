from sqlalchemy.orm import Session
from .schemas import *
from .models import Project, Employe, Task


def create_project(db: Session, data: ProjectCreate):
    project = Project(**data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_projects(db, Session):
    return db.query(Project).all()

def get_project_by_id(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id:int, data: ProjectUpdate):
    data = data.model_dump()
    project = db.get(Project, project_id)
    if project:
        project.name = data['name']
        project.descripton = data['description']
        db.commit()
        db.refresh(project)
    return project

def delete_project(db: Session, project):
    db.delete(project)
    db.commit() 

def create_employee(db: Session, data: EmployeCreate):
    employee = Employe(
        full_name = data.full_name,
        email=data.email,
        position=data.position,
        is_active=data.is_active
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employees(db:Session):
    return db.query(Employe).all()

def get_employee_by_id(db:Session, employeee_id: int):
    return db.query(Employe).filter(Employe.id == employeee_id).first()

def update_employee(db: Session, employee, data: EmployeUpdate):
    if data.full_name is not None:
        employee.full_name = data.full_name
    if data.email is not None:
        employee.email == data.email
    if data.position is not None:
        employee.position = data.position
    if data.is_active is not None:
        employee.is_active = data.is_active

    db.commit()
    db.refresh(employee)
    return employee

def delete_employee_db(db: Session, employee):
    db.delete(employee)
    db.commit()


def create_task_db(db: Session, data: TaskCreate):
    task = Task(
        title=data.title,
        description=data.description,
        status=data.status,
        priority=data.priority,
        deadline=data.deadline,
        project_id=data.project_id,
        employee_id=data.employee_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task, data: TaskUpdate):
    if data.title is not None:
        task.title = data.title
    if data.description is not None:
        task.description = data.description
    if data.status is not None:
        task.status = data.status
    if data.priority is not None:
        task.priority = data.priority
    if data.deadline is not None:
        task.deadline = data.deadline
    if data.project_id is not None:
        task.project_id = data.project_id
    if data.employee_id is not None:
        task.employee_id = data.employee_id

    db.commit()
    db.refresh()
    return task

def delete_task(db: Session, task):
    db.delete(task)
    db.commit()