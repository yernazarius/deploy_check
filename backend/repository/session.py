from typing import Dict, Any, List, Union
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.session import Session
from sqlalchemy import update, delete, select, insert

class SessionRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_session(self, session: Dict[str, Any]) -> int:
        try:
            stmt = insert(Session).values(**session).returning(Session.id)
            result = await self.db.execute(stmt)
            await self.db.flush()
            session_id = result.fetchone()[0]
            await self.db.commit()            
            return session_id
        except Exception as e:
            print('Exception in create_session: ', e)
            return False
    
    async def get_session(self, session_id: int) -> Session:
        try:
            stmt = select(Session).where(Session.id == session_id)
            result = await self.db.execute(stmt)
            return result.scalars().first()
        except Exception as e:
            print('Exception in get_session: ', e)
            return False
        
    async def get_sessions(self) -> List[Session]:
        try:
            stmt = select(Session)
            result = await self.db.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_sessions: ', e)
            return False
        
    async def update_session(self, session: Dict[str, Any]) -> Dict:
        try:
            stmt = update(Session).where(Session.id == session['id']).values(**session)
            await self.db.execute(stmt)
            await self.db.commit()
            return session
        except Exception as e:
            print('Exception in update_session: ', e)
            return False
        
    async def delete_session(self, session_id: int) -> bool:
        try:
            stmt = delete(Session).where(Session.id == session_id)
            await self.db.execute(stmt)
            await self.db.commit()
            return True
        except Exception as e:
            print('Exception in delete_session: ', e)
            return False
        
    
    async def get_sessions_by_business_id(self, business_id: int) -> List[Session]:
        try:
            stmt = select(Session).where(Session.business_id == business_id)
            result = await self.db.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print('Exception in get_session_by_business_id: ', e)
            return False