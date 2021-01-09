"""Ключевым фактором является то, что зависимость должна быть 'вызываемой'."""

from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# Заменяем функцию на класс в параметры инициализации которого, передаются параметры роута
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    # FastApi позволяет минимизировать код используя такой синтаксис вызова зависимости КЛАССА
    # commons: CommonQueryParams = Depends()
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
