from typing import Optional

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Pydantic-объект также м.б. необязательным
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,  # sic!
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# Несколько параметров тела и особый параметр Body, не имеющий модели
class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/multi-items/{item_id}")
async def update_multi_item(item_id: int, item: Item, user: User, importance: int = Body(...)):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


# Можно заставить ожидать JSON с ключом, даже если приходит всего один объект, задав параметр embed=True
@app.put("/key-items/{item_id}")
async def update_key_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
