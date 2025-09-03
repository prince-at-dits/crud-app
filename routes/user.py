from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from config.db import SessionLocal
from models.user import User
from schemas.index import User as UserSchema
from app.auth.auth_handler import get_current_user



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

user = APIRouter()

@user.get("/")
async def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        result = db.query(User).all()
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@user.get("/{id}")
async def get_user_by_id(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        result = db.query(User).filter(User.id == id).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@user.post("/")
async def write_data(user: UserSchema, db: Session = Depends(get_db)):
    try:
        new_user = User(name=user.name, email=user.email, age=user.age)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"status": "success", "message": "User created successfully", "data": new_user}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@user.put("/{id}")
async def update_data(id: int, user: UserSchema, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.id == id).first()
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        existing_user.name = user.name
        existing_user.email = user.email
        existing_user.age = user.age
        db.commit()
        db.refresh(existing_user)
        return {"status": "success", "message": "User updated successfully", "data": existing_user}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@user.delete("/{id}")
async def delete_data(id: int, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.id == id).first()
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        db.delete(existing_user)
        db.commit()
        return {"status": "success", "message": "User deleted successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
