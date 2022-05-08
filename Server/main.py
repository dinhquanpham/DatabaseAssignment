from imp import reload
from urllib.request import Request
from fastapi import FastAPI
from sqlalchemy import true
from database import engine
from models import Base
from api.router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='FastAPI Project',
)

app.include_router(router)




