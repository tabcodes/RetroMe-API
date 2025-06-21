from sqlmodel import Relationship, sql, Field, SQLModel
from models import RetroColumn
import uuid

class RetroBoard(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)

    retro_columns: list["RetroColumn"] = Relationship(back_populates="board")