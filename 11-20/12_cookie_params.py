from typing import Optional

from fastapi import Cookie, FastAPI

app = FastAPI()


# Cookie поддерживает те же аргументы, что Path и Query
@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}
