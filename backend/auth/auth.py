from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from config import SECRET_KEY
from fastapi_users import FastAPIUsers
from .manager import get_user_manager
from model.data.user import User
from fastapi import Depends, HTTPException, status


cookie_transport = CookieTransport(cookie_max_age=3600, cookie_secure=False)



def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600) # type: ignore


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

def require_is_owner():
    def is_owner(current_user: User = Depends(current_user)):
        if current_user.is_owner == False:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
        return current_user
    return is_owner


