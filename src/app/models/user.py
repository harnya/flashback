from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4


class AuthGroup(BaseModel):
    id : UUID = uuid4()
    name : str


class UserRegistration(BaseModel):
    id : UUID = uuid4()
    email : EmailStr
    password : str
    # auth_group_id : UUID
    

class UserLogin(BaseModel):
    email : EmailStr
    password : str


class UserProfile(BaseModel):
    email : EmailStr
    auth_group_name : str









    