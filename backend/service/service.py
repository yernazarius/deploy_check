from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from typing import List, Dict, Any, Union

from repository.service import ServiceRepo

class ServiceService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.service_repo = ServiceRepo(session)
    
    async def create_service(self, service: Dict[str, Any]) -> bool:
        service = await self.service_repo.create_service(service)
        return service
    
    async def get_services(self):
        services = await self.service_repo.get_services()
        return services
    
    async def update_service(self, service: Dict[str, Any]) -> Union[Dict, bool]:
        service = await self.service_repo.update_service(service)
        return service
    
    async def delete_service(self, service_id: int) -> bool:
        service = await self.service_repo.delete_service(service_id)
        return service
    
    async def get_service(self, service_id: int) -> bool:
        service = await self.service_repo.get_service(service_id)
        return service
    
    async def get_services_by_business_id(self, business_id: int) -> bool:
        services = await self.service_repo.get_services_by_business_id(business_id)
        return services