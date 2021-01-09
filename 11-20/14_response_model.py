from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


# Модель ответа позволяет проверить возвращаемые данные. Она может быть той же, что и входная
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


# А может быть другой, что более правильно
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# Использование response_model_exclude_unset для исключения из ответа значений по умолчанию
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


# использовать response_model_exclude_defaults=True response_model_exclude_none=True

# или response_model_include и response_model_exclude
# если есть только одна модель для входящих и исходящих данных.
# Но это нарушит документацию и не рекомендуется
