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
