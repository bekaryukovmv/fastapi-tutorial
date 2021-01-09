from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)  # ! N.B! Если мы не можем изменить роутер (например, он из стороннего модуля)
# ! Мы всё равно можем добавить префикс, теги и зависимости, при его подключении.

# ? Один и тот же роутер можно подключить несколько раз, с несколькими префиксами.
# ? Например: /api/v1и /api/latest

# * Кроме того, можно включать один роутер в другой: router.include_router(other_router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
