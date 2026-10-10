from fastapi import APIRouter, HTTPException, Response, status

from fastapi_study.dependencies import ItemServiceDep
from fastapi_study.schemas.item import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(data: ItemCreate, service: ItemServiceDep):
    return service.create_item(data.name, data.price, data.description)


@router.get("", response_model=list[ItemResponse])
def list_items(service: ItemServiceDep):
    return service.list_items()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, service: ItemServiceDep):
    item = service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=ItemResponse)
def replace_item(item_id: int, data: ItemCreate, service: ItemServiceDep):
    item = service.replace_item(
        item_id, data.name, data.price, data.description
    )
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, service: ItemServiceDep) -> Response:
    if not service.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
