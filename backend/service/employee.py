from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from typing import List, Dict, Any, Union

from repository.employee import EmployeeRepo

class EmployeeService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.business_repo = EmployeeRepo(session)
    
    async def create_employee(self, employee: Dict[str, Any]) -> bool:
        employee = await self.business_repo.create_employee(employee)
        return employee
    
    async def get_employees(self):
        employees = await self.business_repo.get_employees()
        return employees
    
    async def update_employee(self, employee: Dict[str, Any]) -> Union[Dict, bool]:
        employee = await self.business_repo.update_employee(employee)
        return employee
    
    async def delete_employee(self, employee_id: int) -> bool:
        employee = await self.business_repo.delete_employee(employee_id)
        return employee
    
    async def get_employee_by_business_id(self, business_id: int) -> bool:
        employee = await self.business_repo.get_employee_by_business_id(business_id)
        return employee

    
   