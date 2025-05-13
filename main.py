from http.client import HTTPException
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import  schemes, crud
from models import Base
from database import engine, SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Dependency – har bir so‘rov uchun DB sessiya
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# Jadvalni yaratish
# Base.metadata.create_all(bind=engine)

#  <----- web-sockets:start ----->

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
active_connections = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            print("Received:", data)

            # Broadcast to all connected clients
            for conn in active_connections:
                if conn != websocket:
                    await conn.send_json(data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)

#  <----- web-sockets:end ----->


@app.get("/")
def read_root():
    return {"msg": "FastAPI is working!"}

# @app.post("/users", response_model=schemes.UserResponse)
# def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db=db, user=user)

# @app.get("/users/{phone}")
# def read_user_by_phone(phone: str, db: Session = Depends(get_db)):
#     user = crud.get_user_by_phone(db, phone)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


