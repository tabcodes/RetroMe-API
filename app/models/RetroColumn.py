from sqlmodel import Relationship, sql, Field, SQLModel
from models import RetroBoard, RetroTopic
import uuid


class RetroColumn(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    board_id: uuid.UUID = Field(default=None, foreign_key="retroboard.id")
    board: RetroBoard = Relationship(back_populates="retro_columns")

    topics: list["RetroTopic"] = Relationship(back_populates="retro_column")