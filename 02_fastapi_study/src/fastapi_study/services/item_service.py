from fastapi_study.models.item import Item
from fastapi_study.repositories.item_repository import ItemRepository


class ItemService:
    def __init__(self, repository: ItemRepository) -> None:
        self._repository = repository

    def create_item(
        self,
        name: str,
        price: float,
        description: str | None,
    ) -> Item:
        item = Item(
            item_id=None,
            name=name,
            price=price,
            description=description,
        )
        return self._repository.add(item)

    def get_item(self, item_id: int) -> Item | None:
        return self._repository.get_by_id(item_id)

    def list_items(self) -> list[Item]:
        return self._repository.list_all()

    def replace_item(
        self,
        item_id: int,
        name: str,
        price: float,
        description: str | None,
    ) -> Item | None:
        if self._repository.get_by_id(item_id) is None:
            return None

        item = Item(
            item_id=item_id,
            name=name,
            price=price,
            description=description,
        )
        return self._repository.update(item)

    def delete_item(self, item_id: int) -> bool:
        return self._repository.delete(item_id)
