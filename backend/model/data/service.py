from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
from .session import Session

class Service(Base):
    __tablename__ = "service"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("business.id", ondelete='CASCADE'), nullable=False)

    session: Mapped[list['Session']] = relationship('Session', backref="service")