"""
Чтобы получать form-data вместо JSON надо использовать Form
Для этого необходимо импортировать pip install python-multipart
"""
from fastapi import FastAPI, Form

app = FastAPI()


# Параметры Form создаются также как Body или Query
# Form напрямую наследуется от Body
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
