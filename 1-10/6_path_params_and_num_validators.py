from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


# N.B! параметр пути требуется всегда! Его нельзя сделать необязательным!
# ge - Проверка на больше или равно.
# gt - больше
# lt - меньше, le - меньше или равно
# N.B! для float надо использовать только строгие проверки
@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get", ge=1),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Хитрость с порядком передаваемых аргументов.
# Если в начале поставить * то все последующие будут интерпретироваться не как позиционные, а как kwargs
@app.get("/items-kw/{item_id}")
async def read_items_kw(*, item_id: int = Path(..., title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
