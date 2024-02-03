from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
import datetime


class Session(Base):
    __tablename__ = "session"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_name: Mapped[str] = mapped_column(String(50), nullable=False)
    client_phone: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    start_time: Mapped[Time] = mapped_column(Time, nullable=False)
    end_time: Mapped[Time] = mapped_column(Time, nullable=False)
    comment: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey("service.id"), nullable=True)
    tariff_id: Mapped[int] = mapped_column(Integer, ForeignKey("tariff.id"), nullable=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employee.id"), nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id", ondelete='CASCADE'), nullable=False)
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("business.id", ondelete='CASCADE'), nullable=False)


