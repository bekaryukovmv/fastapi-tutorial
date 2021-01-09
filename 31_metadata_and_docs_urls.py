from fastapi import FastAPI

# Дополнительные метаданные для тегов. Можно использовать Markdown!
# ! Порядок тегов определит порядок отображения эндпоинтов
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]


# Описание проекта, отражаемое в документации
app = FastAPI(
    title="My Super Project",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="2.5.0",
    # Подключение метадаты для тегов.
    openapi_tags=tags_metadata,
    # Определяет адрес, по которому доступна схема апи. None - полностью её отключит
    openapi_url="/api/v1/openapi.json",
    # Путь для документации (swagger). None его полностью отключит
    docs_url="/documentation",
    # Путь для альтернативной документации
    redoc_url=None,
)


@app.get("/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("/items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
