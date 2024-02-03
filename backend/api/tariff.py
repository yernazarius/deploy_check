from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db_config.session import get_async_session

from model.request.tariff import TariffCreate, TariffUpdate, TariffRead
from model.data.user import User
from service.tariff import TariffService
from auth.auth import current_user

from typing import Dict, List

router = APIRouter()

@router.post('/create_tariff', response_model=TariffRead)
async def create_tariff(tariff: TariffCreate, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    tariff_service = TariffService(session)
    tariff = await tariff_service.create_tariff(tariff.model_dump())
    if tariff:
        return JSONResponse(status_code=200, content={'message': 'Tariff created successfully', 'tariff_id': tariff})
    return JSONResponse(status_code=400, content={'message': 'Tariff creation failed'})

@router.get('/get_tariffs', response_model=List[TariffRead])
async def get_tariffs(current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    tariff_service = TariffService(session)
    tariffs = await tariff_service.get_tariffs()
    if tariffs:
        return tariffs
    return JSONResponse(status_code=400, content={'message': 'Tariffs retrieval failed'})

@router.patch('/update_tariff', response_model=TariffRead)
async def update_tariff(tariff: TariffUpdate, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    tariff_service = TariffService(session)
    tariff = await tariff_service.update_tariff(tariff.model_dump(exclude_none=True, exclude_defaults=True))
    if tariff:
        return JSONResponse(status_code=200, content={'message': 'Tariff updated successfully', 'tariff': tariff})
    return JSONResponse(status_code=400, content={'message': 'Tariff update failed'})

@router.delete('/delete_tariff')
async def delete_tariff(tariff_id: int, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    tariff_service = TariffService(session)
    tariff = await tariff_service.delete_tariff(tariff_id)
    if tariff:
        return JSONResponse(status_code=200, content={'message': 'Tariff deleted successfully'})
    return JSONResponse(status_code=400, content={'message': 'Tariff deletion failed'})

@router.get('/get_tariff_by_business_id', response_model=List[TariffRead])
async def get_tariff_by_business_id(business_id: int, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    tariff_service = TariffService(session)
    tariff = await tariff_service.get_tariff_by_business_id(business_id)
    if tariff:
        return tariff
    return JSONResponse(status_code=400, content={'message': 'Tariff retrieval failed'})