from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.user_business import UserBusiness
from model.data.business import Business
from sqlalchemy import update, delete, select, insert, join

class UserBusinessRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user_business(self, user_business: Dict[str, Any]) -> int:
        try:
            stmt = insert(UserBusiness).values(**user_business).returning(UserBusiness.id)
            result = await self.session.execute(stmt)
            await self.session.commit()
            return result
        except Exception as e:
            print('Exception in create_user_business: ', e)
            return False
    
    async def get_user_business(self, user_business_id: int) -> UserBusiness:
        try:
            stmt = select(UserBusiness).where(UserBusiness.id == user_business_id)
            result = await self.session.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print('Exception in get_user_business: ', e)
            return False
    
    async def get_user_businesses_by_user_id(self, user_id: int) -> List[UserBusiness]:
        try:
            # write the query to get business by user_id using joinload
            stmt = select(Business).join(UserBusiness).where(UserBusiness.business_id == Business.id).where(UserBusiness.user_id == user_id)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_user_business_by_user_id: ', e)
            return False

        
    async def update_user_business(self, user_business: Dict[str, Any]) -> Dict:
        try:
            stmt = update(UserBusiness).where(UserBusiness.id == user_business['id']).values(**user_business)
            await self.session.execute(stmt)
            await self.session.commit()
            return user_business
        except Exception as e:
            print('Exception in update_user_business: ', e)
            return False
        
    async def delete_user_business(self, user_business_id: int) -> bool:
        try:
            stmt = delete(UserBusiness).where(UserBusiness.id == user_business_id)
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception as e:
            print('Exception in delete_user_business: ', e)
            return False