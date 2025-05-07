from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import  schemes, crud
from models import Base
from database import engine, SessionLocal


app = FastAPI()
# Dependency – har bir so‘rov uchun DB sessiya
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Jadvalni yaratish
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "FastAPI is working!"}

@app.post("/users", response_model=schemes.UserResponse)
def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)