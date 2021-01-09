from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from starlette.middleware.cors import CORSMiddleware #? можно так. starlette поддерживает больше middlewares
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Список источников, которым разрешено делать запросы
    allow_credentials=True,  # Поддерживать ли Cookie
    allow_methods=["*"],  # Список разрешённых методов HTTP
    allow_headers=["*"],  # Список поддерживаемых заголовков HTTP-запросов
)
# allow_origin_regex - Строка регулярного выражения для сопоставления с источниками, которым разрешено делать запросы
# expose_headers - Заголовки ответов, которые должны быть доступны браузеру. По умолчанию [].
# max_age - максимальное время кэширования ответа. По умолчанию 600 сек.


@app.get("/")
async def main():
    return {"message": "Hello World"}
