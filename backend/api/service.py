from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db_config.session import get_async_session

from model.request.service import ServiceCreate, ServiceUpdate, ServiceRead
from model.data.user import User
from service.service import ServiceService
from auth.auth import current_user

from typing import Dict, List

router = APIRouter()

@router.post('/create_service', response_model=ServiceRead)
async def create_service(service: ServiceCreate, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    service_service = ServiceService(session)
    service = await service_service.create_service(service.model_dump())
    if service:
        return JSONResponse(status_code=200, content={'message': 'Service created successfully', 'service_id': service})
    return JSONResponse(status_code=400, content={'message': 'Service creation failed'})

@router.get('/get_services', response_model=List[ServiceRead])
async def get_services(current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    service_service = ServiceService(session)
    services = await service_service.get_services()
    if services:
        return services
    return JSONResponse(status_code=400, content={'message': 'Services retrieval failed'})

@router.patch('/update_service', response_model=ServiceRead)
async def update_service(service: ServiceUpdate, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    service_service = ServiceService(session)
    service = await service_service.update_service(service.model_dump(exclude_none=True, exclude_defaults=True))
    if service:
        return JSONResponse(status_code=200, content={'message': 'Service updated successfully', 'service': service})
    return JSONResponse(status_code=400, content={'message': 'Service update failed'})

@router.delete('/delete_service')
async def delete_service(service_id: int, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    service_service = ServiceService(session)
    service = await service_service.delete_service(service_id)
    if service:
        return JSONResponse(status_code=200, content={'message': 'Service deleted successfully'})
    return JSONResponse(status_code=400, content={'message': 'Service deletion failed'})

@router.get('/get_service_by_business_id', response_model=List[ServiceRead])
async def get_service_by_business_id(business_id: int, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    service_service = ServiceService(session)
    services = await service_service.get_service_by_business_id(business_id)
    if services:
        return services
    return JSONResponse(status_code=400, content={'message': 'Services retrieval failed'})

