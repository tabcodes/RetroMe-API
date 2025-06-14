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
    database_ok = False;

    try:
        session.exec(text("SELECT 1;"))
        database_ok = True;
    except Exception as e:
        raise Exception("DB connection failure: ", e)


    return {"database": database_ok}