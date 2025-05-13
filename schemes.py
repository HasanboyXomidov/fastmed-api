from pydantic import BaseModel

class UserCreate(BaseModel):
    phone: str
    illness: str
    adress: str

class UserResponse(UserCreate):
    id: int

    model_config = {
        "from_attributes": True
    }

class UserGetRequest(BaseModel):
    phone: str  

class UserGetResponse(BaseModel):
    id: int
    phone: str
    illness: str
    adress: str
    
    model_config = {
        "from_attributes": True
    }    