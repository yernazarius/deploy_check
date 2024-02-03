from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db_config.session import get_async_session

from model.request.business import BusinessCreate, BusinessUpdate, BusinessRead
from model.data.user import User
from service.business import BusinessService
from auth.auth import require_is_owner, current_user

from typing import Dict, List

router = APIRouter()

@router.post('/create_business', response_model=BusinessRead)
async def create_business(business: BusinessCreate, current_user: User = Depends(require_is_owner()), session: AsyncSession = Depends(get_async_session)):
    business_service = BusinessService(session)
    business_id = await business_service.create_business(business.model_dump(), current_user.id)
    if business_id:
        return JSONResponse(status_code=200, content={'message': 'Business created successfully', 'business_id': business_id})
    return JSONResponse(status_code=400, content={'message': 'Business creation failed'})

@router.get('/get_businesses', response_model=List[BusinessRead])
async def get_businesses(current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    business_service = BusinessService(session)
    businesses = await business_service.get_businesses(current_user.id)
    if businesses:
        return businesses
    return JSONResponse(status_code=400, content={'message': 'Businesses retrieval failed'})

@router.put('/update_business', response_model=BusinessRead)
async def update_business(business: BusinessUpdate, current_user: User = Depends(require_is_owner()), session: AsyncSession = Depends(get_async_session)):
    business_service = BusinessService(session)
    business = await business_service.update_business(business.model_dump(exclude_none=True, exclude_defaults=True))
    if business:
        return JSONResponse(status_code=200, content={'message': 'Business updated successfully', 'business': business})
    return JSONResponse(status_code=400, content={'message': 'Business update failed'})

@router.delete('/delete_business')
async def delete_business(business_id: int, current_user: User = Depends(require_is_owner()), session: AsyncSession = Depends(get_async_session)):
    business_service = BusinessService(session)
    business = await business_service.delete_business(business_id)
    if business:
        return JSONResponse(status_code=200, content={'message': 'Business deleted successfully'})
    return JSONResponse(status_code=400, content={'message': 'Business deletion failed'})