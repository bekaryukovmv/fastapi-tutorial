from fastapi import FastAPI, status

app = FastAPI()


# Статус-коды лучше импортировать из FastAPI или напрямую из starlette они более человеко-читаемы
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
