from typing import Annotated

from fastapi import Depends

from fastapi_study.repositories.item_repository import (
    InMemoryItemRepository,
    ItemRepository,
)
from fastapi_study.services.item_service import ItemService

_item_repository = InMemoryItemRepository()


def get_item_repository() -> ItemRepository:
    return _item_repository


def get_item_service(
    repository: Annotated[ItemRepository, Depends(get_item_repository)],
) -> ItemService:
    return ItemService(repository)


ItemServiceDep = Annotated[ItemService, Depends(get_item_service)]
