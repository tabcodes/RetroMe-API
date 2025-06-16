from sqlmodel import sql, Field, SQLModel
import uuid

class RetroBoard(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)