from itertools import count
from abc import ABC, abstractmethod

from fastapi_study.models.item import Item


class ItemRepository(ABC):
    """저장소 구현체가 제공해야 하는 공통 계약."""

    @abstractmethod
    def add(self, item: Item) -> Item:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, item_id: int) -> Item | None:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[Item]:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: Item) -> Item:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        raise NotImplementedError


class InMemoryItemRepository(ItemRepository):
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._ids = count(1)

    def add(self, item: Item) -> Item:
        item_id = next(self._ids)
        saved = Item(
            item_id=item_id,
            name=item.name,
            price=item.price,
            description=item.description,
        )
        self._items[item_id] = saved
        return saved

    def get_by_id(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def list_all(self) -> list[Item]:
        return list(self._items.values())

    def update(self, item: Item) -> Item:
        assert item.item_id is not None
        self._items[item.item_id] = item
        return item

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None
