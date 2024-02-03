from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
from .session import Session

class Employee(Base):
    __tablename__ = "employee"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    position: Mapped[str] = mapped_column(String(50), nullable=False)
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("business.id", ondelete='CASCADE'), nullable=False)

    session: Mapped[list['Session']] = relationship('Session', backref="employee")