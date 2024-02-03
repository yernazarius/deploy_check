from model.data.user import User
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead, UserUpdate

from fastapi.middleware.cors import CORSMiddleware

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from config import REDIS_HOST, REDIS_PORT



from api import business, employee, tariff, service, session, whatsapp_webhook



fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app = FastAPI()


origins = ['http://localhost:3000', 'http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/api/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/api/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    business.router,
    prefix="/business",
    tags=["business"],
)

app.include_router(
    employee.router,
    prefix="/employee",
    tags=["employee"],
)

app.include_router(
    tariff.router,
    prefix="/tariff",
    tags=["tariff"],
)

app.include_router(
    service.router,
    prefix="/service",
    tags=["service"],
)

app.include_router(
    session.router,
    prefix="/session",
    tags=["session"],
)

app.include_router(
    whatsapp_webhook.router,
    prefix="/whatsapp_webhook",
    tags=["whatsapp_webhook"],
)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")