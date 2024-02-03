import sys, os
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from model.data.user import User
from db_config.session import get_user_db
from config import SECRET_KEY

from task.email_service import send_verification_token_to_user_sync, send_reset_token_to_user_sync


SECRET = SECRET_KEY

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET # type: ignore
    verification_token_secret = SECRET # type: ignore

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):  
        send_reset_token_to_user_sync.delay(user.name, user.email, token)
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        send_verification_token_to_user_sync.delay(user.name, user.email, token)
        print(f"Verification requested for user {user.id}. Verification token: {token}")



async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
