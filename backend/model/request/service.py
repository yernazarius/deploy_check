'''
class Service(Base):
    __tablename__ = "service"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("business.id", ondelete='CASCADE'), nullable=False)

    session: Mapped[list['Session']] = relationship('Session', backref="service")
'''

from pydantic import BaseModel
from typing import Optional, Union

class ServiceCreate(BaseModel):
    title: str
    price: float
    business_id: int

class ServiceUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    price: Optional[float] = None
    business_id: Optional[int] = None


class ServiceRead(ServiceCreate):
    id: int

    class Config:
        orm_mode = True