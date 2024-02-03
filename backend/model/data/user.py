from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
from fastapi_users.db import SQLAlchemyBaseUserTable
from .kpi import Kpi
from .user_business import UserBusiness


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    is_owner: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    kpi: Mapped[list['Kpi']] = relationship("Kpi", backref="user")
    user_business: Mapped[list['UserBusiness']] = relationship("UserBusiness", backref="user", cascade="all, delete-orphan")