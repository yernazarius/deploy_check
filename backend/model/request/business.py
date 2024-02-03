from pydantic import BaseModel
from typing import Optional, Union

'''
class Business(Base):
    __tablename__ = "business"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
'''

class BusinessCreate(BaseModel):
    name: str
    country: str
    city: str
    address: str

class BusinessUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None

class BusinessRead(BusinessCreate):
    id: int

    class Config:
        orm_mode = True
