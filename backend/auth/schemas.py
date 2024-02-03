import uuid

from fastapi_users import schemas
import datetime
from typing import Union

'''
class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    is_owner: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    business = relationship("Business", backref="user")
    
'''


class UserRead(schemas.BaseUser[int]):
    name: str
    phone: str
    is_owner: bool


class UserCreate(schemas.BaseUserCreate):
    name: str
    phone: str
    is_owner: bool = False

class UserUpdate(schemas.BaseUserUpdate):
    name: str
    phone: str
    is_owner: bool