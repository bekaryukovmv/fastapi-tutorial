from typing import List, Optional

from fastapi import FastAPI, Query

app = FastAPI()


# Дополнительная проверка query params, min and max lenght, regexp
# ... - делает параметр обязательным
@app.get("/items/")
async def read_items(q: Optional[str] = Query(..., min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Получение повторяющегося значения параметра
@app.get("/multi-items/")
async def read_multi_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items


# несколько значений со значениями по умолчанию
@app.get("/multi-default-items/")
async def read_multi_default_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


# добавить дополнительную информацию о параметре (для сваггера)
@app.get("/doc-items/")
async def read_doc_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# alias для неформатных параметров
@app.get("/items-alias/")
async def read_items_alias(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# пометка параметра устаревшим (для сваггера)
@app.get("/deprecated-items/")
async def read_deprecated_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,  # this!
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
