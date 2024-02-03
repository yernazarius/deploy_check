from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db_config.session import get_async_session

from model.request.session import SessionCreate, SessionUpdate, SessionRead
from model.data.user import User
from service.session import SessionService
from auth.auth import current_user

from typing import Dict, List

router = APIRouter()

@router.post('/create_session', response_model=SessionRead)
async def create_session(session: SessionCreate, current_user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    session_service = SessionService(db)
    session_dump = session.model_dump(exclude_none=True)
    session_dump['user_id'] = current_user.id
    session_res = await session_service.create_session(session_dump)
    if session_res:
        return JSONResponse(status_code=200, content={'message': 'Session created successfully', 'session_id': session_res})
    return JSONResponse(status_code=400, content={'message': 'Session creation failed'})

@router.get('/get_sessions', response_model=List[SessionRead])
async def get_sessions(current_user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    session_service = SessionService(db)
    sessions = await session_service.get_sessions()
    if sessions:
        return sessions
    return JSONResponse(status_code=400, content={'message': 'Sessions retrieval failed'})

@router.patch('/update_session', response_model=SessionRead)
async def update_session(session: SessionUpdate, current_user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    session_service = SessionService(db)
    session = await session_service.update_session(session.model_dump(exclude_none=True, exclude_defaults=True))
    if session:
        return JSONResponse(status_code=200, content={'message': 'Session updated successfully', 'session': session})
    return JSONResponse(status_code=400, content={'message': 'Session update failed'})

@router.delete('/delete_session')
async def delete_session(session_id: int, current_user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    session_service = SessionService(db)
    session = await session_service.delete_session(session_id)
    if session:
        return JSONResponse(status_code=200, content={'message': 'Session deleted successfully'})
    return JSONResponse(status_code=400, content={'message': 'Session deletion failed'})

@router.get('/get_session_by_business_id', response_model=List[SessionRead])
async def get_session_by_business_id(business_id: int, current_user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    session_service = SessionService(db)
    session = await session_service.get_session_by_business_id(business_id)
    if session:
        return session
    return JSONResponse(status_code=400, content={'message': 'Session retrieval failed'})