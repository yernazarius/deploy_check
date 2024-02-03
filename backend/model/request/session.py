'''class Session(Base):
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

'''

from pydantic import BaseModel
from typing import Optional, Union
from datetime import date, time, datetime

class SessionCreate(BaseModel):
    client_name: str
    client_phone: str
    price: float
    date: date
    start_time: time
    end_time: time
    comment: Optional[str] = None
    service_id: Optional[int] = None
    tariff_id: Optional[int] = None
    employee_id: Optional[int] = None
    business_id: int

class SessionUpdate(BaseModel):
    id: int
    client_name: Optional[str] = None
    client_phone: Optional[str] = None
    price: Optional[float] = None
    date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    comment: Optional[str] = None
    service_id: Optional[int] = None
    tariff_id: Optional[int] = None
    employee_id: Optional[int] = None
    business_id: Optional[int] = None

class SessionRead(SessionCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True