from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
from .session import Session

class Tariff(Base):
    __tablename__ = "tariff"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=False)
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("business.id", ondelete='CASCADE'), nullable=False)

    session: Mapped[list['Session']] = relationship('Session', backref="tariff")