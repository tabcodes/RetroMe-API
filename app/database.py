import os
from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends

DATABASE_URL = os.environ.get("DATABASE_URL")

if(DATABASE_URL == None):
    raise Exception("No DB credentials found in environment.")


engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

