from pydantic import BaseModel
from typing import Optional, Union


'''
class Tariff(Base):
    __tablename__ = "tariff"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=False)
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("business.id", ondelete='CASCADE'), nullable=False)

    session: Mapped[list['Session']] = relationship('Session', backref="tariff")
'''

class TariffCreate(BaseModel):
    title: str
    description: str
    business_id: int

class TariffUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    business_id: Optional[int] = None

class TariffRead(TariffCreate):
    id: int

    class Config:
        orm_mode = True