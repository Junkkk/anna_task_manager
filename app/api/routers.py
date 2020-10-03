from fastapi import APIRouter
from app.api.endpoints import users, tasks

router = APIRouter()
router.include_router(users.router)
router.include_router(tasks.router)
