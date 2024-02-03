from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db_config.session import get_async_session

from model.request.employee import EmployeeCreate, EmployeeUpdate, EmployeeRead
from model.data.user import User
from service.employee import EmployeeService
from auth.auth import current_user

from typing import Dict, List

router = APIRouter()

@router.post('/create_employee', response_model=EmployeeRead)
async def create_employee(employee: EmployeeCreate, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    employee_service = EmployeeService(session)
    employee = await employee_service.create_employee(employee.model_dump())
    if employee:
        return JSONResponse(status_code=200, content={'message': 'Employee created successfully', 'employee_id': employee})
    return JSONResponse(status_code=400, content={'message': 'Employee creation failed'})

@router.get('/get_employees', response_model=List[EmployeeRead])
async def get_employees(current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    employee_service = EmployeeService(session)
    employees = await employee_service.get_employees()
    if employees:
        return employees
    return JSONResponse(status_code=400, content={'message': 'Employees retrieval failed'})

@router.patch('/update_employee', response_model=EmployeeRead)
async def update_employee(employee: EmployeeUpdate, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    employee_service = EmployeeService(session)
    employee = await employee_service.update_employee(employee.model_dump(exclude_none=True, exclude_defaults=True))
    if employee:
        return JSONResponse(status_code=200, content={'message': 'Employee updated successfully', 'employee': employee})
    return JSONResponse(status_code=400, content={'message': 'Employee update failed'})

@router.delete('/delete_employee')  
async def delete_employee(employee_id: int, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    employee_service = EmployeeService(session)
    employee = await employee_service.delete_employee(employee_id)
    if employee:
        return JSONResponse(status_code=200, content={'message': 'Employee deleted successfully'})
    return JSONResponse(status_code=400, content={'message': 'Employee deletion failed'})

@router.get('/get_employee_by_business_id', response_model=List[EmployeeRead])
async def get_employee_by_business_id(business_id: int, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    employee_service = EmployeeService(session)
    employee = await employee_service.get_employee_by_business_id(business_id)
    if employee:
        return employee
    return JSONResponse(status_code=400, content={'message': 'Employee retrieval failed'})