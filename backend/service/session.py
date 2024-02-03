from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from typing import List, Dict, Any, Union

from repository.session import SessionRepo

class SessionService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.session_repo = SessionRepo(db)
    
    async def create_session(self, session: Dict[str, Any]) -> bool:
        session = await self.session_repo.create_session(session)
        return session
    
    async def get_sessions(self):
        sessions = await self.session_repo.get_sessions()
        return sessions
    
    async def update_session(self, session: Dict[str, Any]) -> Union[Dict, bool]:
        session = await self.session_repo.update_session(session)
        return session
    
    async def delete_session(self, session_id: int) -> bool:
        session = await self.session_repo.delete_session(session_id)
        return session
    
    async def get_session(self, session_id: int) -> bool:
        session = await self.session_repo.get_session(session_id)
        return session
    
    async def get_sessions_by_business_id(self, business_id: int) -> bool:
        sessions = await self.session_repo.get_sessions_by_business_id(business_id)
        return sessions
    