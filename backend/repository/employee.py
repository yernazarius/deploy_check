from typing import Dict, Any, List, Union
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.employee import Employee
from sqlalchemy import update, delete, select, insert

class EmployeeRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_employee(self, employee: Dict[str, Any]) -> int:
        try:
            stmt = insert(Employee).values(**employee).returning(Employee.id)
            result = await self.session.execute(stmt)
            await self.session.flush()
            employee_id = result.fetchone()[0]
            await self.session.commit()            
            return employee_id
        except Exception as e:
            print('Exception in create_employee: ', e)
            return False
    
    async def get_employee(self, employee_id: int) -> Employee:
        try:
            stmt = select(Employee).where(Employee.id == employee_id)
            result = await self.session.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print('Exception in get_employee: ', e)
            return False
        
    async def get_employees(self) -> List[Employee]:
        try:
            stmt = select(Employee)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_employees: ', e)
            return False
        
    async def update_employee(self, employee: Dict[str, Any]) -> Dict:
        try:
            stmt = update(Employee).where(Employee.id == employee['id']).values(**employee)
            await self.session.execute(stmt)
            await self.session.commit()
            return employee
        except Exception as e:
            print('Exception in update_employee: ', e)
            return False
        
    async def delete_employee(self, employee_id: int) -> bool:
        try:
            stmt = delete(Employee).where(Employee.id == employee_id)
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception as e:
            print('Exception in delete_employee: ', e)
            return False
        
    
    async def get_employee_by_business_id(self, business_id: int) -> List[Employee]:
        try:
            stmt = select(Employee).where(Employee.business_id == business_id)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_employee_by_business_id: ', e)
            return False