from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID, uuid4


class AuthGroup(BaseModel):
    id : UUID = uuid4()
    name : str


class UserRegistration(BaseModel):
    email : EmailStr
    password : str
    

class UserLogin(BaseModel):
    email : EmailStr
    password : str


class UserProfile(BaseModel):
    id : str 
    email : EmailStr
    is_active : bool = False
    first_name : str | None = None
    last_name : str | None = None
    created_at : datetime









    