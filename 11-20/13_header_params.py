from typing import Optional

from fastapi import FastAPI, Header

app = FastAPI()

"""
Header определяются также как и Query, Path, Cookie
по умолчанию Header символы имен параметров преобразуются из подчеркивания (_)
в дефис (-) для извлечения и документирования заголовков.

Кроме того, заголовки HTTP не чувствительны к регистру, поэтому вы можете
объявить их в стандартном стиле Python

Если по каким-то причинам необходимо отключить автоматическое преобразование
символов подчеркивания в дефисы, установите параметр
convert_underscores=False
"""


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}
