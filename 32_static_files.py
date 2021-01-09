"""необходимо установить aiofiles"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Обработчик статических файлов монтируется как отдельное приложениею
# Его работа не отображается в документации
app.mount("/static", StaticFiles(directory="static"), name="static")
