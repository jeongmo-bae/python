from pydantic import BaseModel, ConfigDict, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    description: str | None = Field(default=None, max_length=1000)


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    item_id: int
    name: str
    price: float
    description: str | None
