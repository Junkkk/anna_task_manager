import uvicorn

from typing import Optional
from fastapi import FastAPI, APIRouter

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/auth/{login}/{password}")
async def read_auth(login: str, password: str):
    return {'login': login, 'password': password}


if __name__ == '__main__':
    uvicorn.run(app)
