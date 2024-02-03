from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from typing import List, Dict, Any, Union

from repository.tariff import TariffRepo

class TariffService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.business_repo = TariffRepo(session)
    
    async def create_tariff(self, tariff: Dict[str, Any]) -> bool:
        tariff = await self.business_repo.create_tariff(tariff)
        return tariff
    
    async def get_tariffs(self):
        tariffs = await self.business_repo.get_tariffs()
        return tariffs
    
    async def update_tariff(self, tariff: Dict[str, Any]) -> Union[Dict, bool]:
        tariff = await self.business_repo.update_tariff(tariff)
        return tariff
    
    async def delete_tariff(self, tariff_id: int) -> bool:
        tariff = await self.business_repo.delete_tariff(tariff_id)
        return tariff
    
    async def get_tariff_by_business_id(self, business_id: int) -> bool:
        tariff = await self.business_repo.get_tariff_by_business_id(business_id)
        return tariff

