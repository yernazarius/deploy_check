from typing import Dict, Any, List, Union
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.business import Business
from sqlalchemy import update, delete, select, insert

class BusinessRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_business(self, business: Dict[str, Any]) -> int:
        try:
            stmt = insert(Business).values(**business).returning(Business.id)
            result = await self.session.execute(stmt)
            await self.session.flush()
            business_id = result.fetchone()[0]
            await self.session.commit()            
            return business_id
        except Exception as e:
            print('Exception in create_business: ', e)
            return False
    
    async def get_business(self, business_id: int) -> Business:
        try:
            stmt = select(Business).where(Business.id == business_id)
            result = await self.session.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print('Exception in get_business: ', e)
            return False
    
    async def get_businesses(self) -> List[Business]:
        try:
            stmt = select(Business)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_businesses: ', e)
            return False

    async def update_business(self, business: Dict[str, Any]) -> Dict:
        try:
            stmt = update(Business).where(Business.id == business['id']).values(**business)
            await self.session.execute(stmt)
            await self.session.commit()
            return business
        except Exception as e:
            print('Exception in update_business: ', e)
            return False
    
    async def delete_business(self, business_id: int) -> bool:
        try:
            stmt = delete(Business).where(Business.id == business_id)
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception as e:
            print('Exception in delete_business: ', e)
            return False
        

    