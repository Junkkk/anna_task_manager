from fastapi import APIRouter
from app.api.endpoints import users, tasks,login

router = APIRouter()
router.include_router(users.router)
router.include_router(tasks.router)
router.include_router(login.router)