from fastapi import APIRouter
from api import UserApi

router = APIRouter()

router.include_router(UserApi.router, tags=["user"], prefix="/users")