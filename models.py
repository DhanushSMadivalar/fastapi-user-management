from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    phone_no: str
    address: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone_no: Optional[str] = None
    address: Optional[str] = None
