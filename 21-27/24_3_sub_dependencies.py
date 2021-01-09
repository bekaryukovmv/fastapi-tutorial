from typing import Optional

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: Optional[str] = None):
    return q


# Иерархия зависимостей может быть сколь угодно глубокой
def query_or_cookie_extractor(q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)):
    if not q:
        return last_query
    return q


# В самом роуте вызывается только одна зависимость, та, которая вызывает остальные
@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


# ! При повторном вызове подзависимости для одного роута используется кэш,
# ! для тех случаев, когда это не нужно, можно использовать флаг use_cache=False
