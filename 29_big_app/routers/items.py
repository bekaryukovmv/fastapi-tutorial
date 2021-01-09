from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",  # ! Префикс не должен включать завершающий слэш!
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},  # Предопределяет ответ содержащий код ошибки
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")  # Сюда также можно добавить Depends и они будут выполнены
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],  # Можно добавить и теги, на уровне роута. Тогда они прибавятся к тегам роутера в целом.
    responses={403: {"description": "Operation forbidden"}},  # То же касается и ответов
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(status_code=403, detail="You can only update the item: plumbus")
    return {"item_id": item_id, "name": "The great Plumbus"}
