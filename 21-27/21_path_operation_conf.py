from typing import Optional, Set

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()


# Так можно передать статус, возвращаемый в случае успеха, в декоратор пути
# Он будет добавлен в документацию
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item


# А так, можно добавить тэги, которые тоже отразятся в документации
@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


# Также, можно добавить summary и description
"""Строка документации"""


@app.post(
    "/descripted-items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item_2(item: Item):
    return item


# Извлечение описания из строки документации используя Markdown
@app.post(
    "/docstringed-items/",
    response_model=Item,
    summary="Create an item",
    response_description="The created item",  # Добавление описания ответа
)
async def create_item_3(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# Пометка устаревшего эндпоинта
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
