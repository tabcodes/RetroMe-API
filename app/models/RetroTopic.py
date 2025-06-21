from sqlmodel import Relationship, sql, Field, SQLModel
from models import RetroColumn
import uuid


class Topic(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    retro_column_id: int | None = Field(default=None, foreign_key="retrocolumn.id")
    retro_column: RetroColumn = Relationship(back_populates="topics")
