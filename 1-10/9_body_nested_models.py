from typing import Dict, List, Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


# Определяем подмодель
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()  # сохранит уникальные тэги
    # tags: List[str] = [] # или так, но это будет список, в котором могут быть повторы
    # image: Optional[Image] = None  # Вложенная модель
    images: Optional[List[Image]] = None  # несколько изображений


# Глубоко вложенные модели
class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# можно объявить, что ожидается список в теле запроса
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


# произвольные словари в теле
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
