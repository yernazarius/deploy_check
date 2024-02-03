'''
class Employee(Base):
    __tablename__ = "employee"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    position: Mapped[str] = mapped_column(String(50), nullable=False)
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("business.id", ondelete='CASCADE'), nullable=False)

    session: Mapped[list['Session']] = relationship('Session', backref="employee")
'''
from pydantic import BaseModel
from typing import Optional, Union


class EmployeeCreate(BaseModel):
    name: str
    phone: Optional[str]
    position: str
    business_id: int

class EmployeeUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    business_id: Optional[int] = None

class EmployeeRead(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True