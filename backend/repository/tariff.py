from typing import Dict, Any, List, Union
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.tariff import Tariff
from sqlalchemy import update, delete, select, insert

class TariffRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_tariff(self, tariff: Dict[str, Any]) -> int:
        try:
            stmt = insert(Tariff).values(**tariff).returning(Tariff.id)
            result = await self.session.execute(stmt)
            await self.session.flush()
            tariff_id = result.fetchone()[0]
            await self.session.commit()            
            return tariff_id
        except Exception as e:
            print('Exception in create_tariff: ', e)
            return False
    
    async def get_tariff(self, tariff_id: int) -> Tariff:
        try:
            stmt = select(Tariff).where(Tariff.id == tariff_id)
            result = await self.session.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print('Exception in get_tariff: ', e)
            return False
        
    async def get_tariffs(self) -> List[Tariff]:
        try:
            stmt = select(Tariff)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_tariffs: ', e)
            return False
        
    async def update_tariff(self, tariff: Dict[str, Any]) -> Dict:
        try:
            stmt = update(Tariff).where(Tariff.id == tariff['id']).values(**tariff)
            await self.session.execute(stmt)
            await self.session.commit()
            return tariff
        except Exception as e:
            print('Exception in update_tariff: ', e)
            return False
        
    async def delete_tariff(self, tariff_id: int) -> bool:
        try:
            stmt = delete(Tariff).where(Tariff.id == tariff_id)
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception as e:
            print('Exception in delete_tariff: ', e)
            return False
        
    async def get_tariff_by_business_id(self, business_id: int) -> Tariff:
        try:
            stmt = select(Tariff).where(Tariff.business_id == business_id)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_tariff_by_business_id: ', e)
            return False
