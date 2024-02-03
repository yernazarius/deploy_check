from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
from .user_business import UserBusiness
from .employee import Employee
from .tariff import Tariff
from .service import Service


class Business(Base):
    __tablename__ = "business"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)


    user_business: Mapped[list['UserBusiness']] = relationship("UserBusiness", backref="business", cascade="all, delete-orphan")
    employee: Mapped[list['Employee']] = relationship("Employee", backref="business", cascade="all, delete-orphan")
    tariff: Mapped[list['Tariff']] = relationship("Tariff", backref="business", cascade="all, delete-orphan")
    service: Mapped[list['Service']] = relationship("Service", backref="business", cascade="all, delete-orphan")