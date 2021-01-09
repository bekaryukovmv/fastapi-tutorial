from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Создаем токен-авторизацию. tokenUrl оказывает путь к эндпоинту авторизации
# ! Эта прпоцедура не создает обработчик авторизации, а лишь указывает путь.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
