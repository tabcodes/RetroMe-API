from typing import Annotated, Union
from fastapi import FastAPI, Depends
from sqlmodel import Field, Session, SQLModel, select, text
from app.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

from app.database import create_db_and_tables, get_session

app = FastAPI()

SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/")
def read_root(session: SessionDep):
    return {"ping": "pong!"}

@app.get("/_ping")
def read_ping(session: SessionDep):
    statement = text("SELECT 1;")
    results = session.exec(statement)
    return {"ping": results.all()}