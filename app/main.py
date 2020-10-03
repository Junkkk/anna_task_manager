import uvicorn

from app.api.routers import router
from fastapi import FastAPI, Request, Response
from db.session import SessionLocal

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app)
