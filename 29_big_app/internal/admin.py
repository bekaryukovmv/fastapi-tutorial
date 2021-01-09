from fastapi import APIRouter

# Типа, роуты внутреннего приложения, к которому мы предоставляем доступ,
# через своё, изменяя префикс и способы авторизации в main
router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
