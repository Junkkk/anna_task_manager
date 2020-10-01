import uvicorn

from typing import Optional
from fastapi import FastAPI, APIRouter

app = FastAPI()


if __name__ == '__main__':
    uvicorn.run(app)
