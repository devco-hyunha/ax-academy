## orm 사용
from fastapi import FastAPI
from sqlalchemy import create_engine, text, Column, Integer, String, Boolean, DateTime
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/hh"
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool
)