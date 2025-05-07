from sqlalchemy.orm import Session
import models, schemes

def create_user(db: Session, user: schemes.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
