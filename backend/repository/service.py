from typing import Dict, Any, List, Union
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.service import Service
from sqlalchemy import update, delete, select, insert

class ServiceRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_service(self, service: Dict[str, Any]) -> int:
        try:
            stmt = insert(Service).values(**service).returning(Service.id)
            result = await self.session.execute(stmt)
            await self.session.flush()
            service_id = result.fetchone()[0]
            await self.session.commit()            
            return service_id
        except Exception as e:
            print('Exception in create_service: ', e)
            return False
    
    async def get_service(self, service_id: int) -> Service:
        try:
            stmt = select(Service).where(Service.id == service_id)
            result = await self.session.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print('Exception in get_service: ', e)
            return False
        
    async def get_services(self) -> List[Service]:
        try:
            stmt = select(Service)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_services: ', e)
            return False
        
    async def update_service(self, service: Dict[str, Any]) -> Dict:
        try:
            stmt = update(Service).where(Service.id == service['id']).values(**service)
            await self.session.execute(stmt)
            await self.session.commit()
            return service
        except Exception as e:
            print('Exception in update_service: ', e)
            return False
        
    async def delete_service(self, service_id: int) -> bool:
        try:
            stmt = delete(Service).where(Service.id == service_id)
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception as e:
            print('Exception in delete_service: ', e)
            return False

    async def get_services_by_business_id(self, business_id: int) -> List[Service]:
        try:
            stmt = select(Service).where(Service.business_id == business_id)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_services_by_business_id: ', e)
            return False