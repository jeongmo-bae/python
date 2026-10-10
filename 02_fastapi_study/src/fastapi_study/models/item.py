from dataclasses import dataclass


@dataclass
class Item:
    item_id: int | None
    name: str
    price: float
    description: str | None = None
