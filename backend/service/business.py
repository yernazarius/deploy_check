from sqlalchemy.ext.asyncio import AsyncSession
from repository.business import BusinessRepo
from repository.user_business import UserBusinessRepo
from typing import List, Dict, Any, Union

class BusinessService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.business_repo = BusinessRepo(session)
        self.user_business_repo = UserBusinessRepo(session)
    
    async def create_business(self, business: Dict[str, Any], user_id: int) -> bool:
        business_id = await self.business_repo.create_business(business)
        if business_id:
            user_business = {
                'user_id': user_id,
                'business_id': business_id
            }
            user_business = await self.user_business_repo.create_user_business(user_business)
            if user_business:
                return business_id
        return False

    async def get_businesses(self, user_id: int):
        businesses = await self.user_business_repo.get_user_businesses_by_user_id(user_id)
        return businesses
    
    async def update_business(self, business: Dict[str, Any]) -> Union[Dict, bool]:
        business = await self.business_repo.update_business(business)
        return business
    
    async def delete_business(self, business_id: int) -> bool:
        business = await self.business_repo.delete_business(business_id)
        return business