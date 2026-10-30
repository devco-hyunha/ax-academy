from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, DateTime
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/hh"
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  username = Column(String(50), unique=True)
  email = Column(String(100), unique=True)
  is_active = Column(Boolean, default=True)
  created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Pydantic 모델 UserCreate를 사용
# username 길이 4~15, email 반드시 @ 포함
# age는 0 이상이어야 함
# 유효하지 않으면 에러 발생
class UserCreate(BaseModel):
  username: str = Field(min_length=4, max_length=15)
  email: str = Field(pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
  age: int = Field(ge=0)

@app.post("/user")
async def create_user(user: UserCreate):
  return user