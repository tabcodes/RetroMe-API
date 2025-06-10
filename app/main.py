from typing import Annotated, Union
from fastapi import FastAPI, Depends
from sqlmodel import Field, Session, SQLModel
from app.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

from app.database import create_db_and_tables, get_session

app = FastAPI()

SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/")
def read_root(session: SessionDep):
    return {"ping": "pong!"}
