from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .models import Hero
from .routers import hero_router

app = FastAPI()
app.include_router(hero_router, prefix="/heroes")


@app.on_event("startup")
async def startup():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(client.heroes, document_models=[Hero])
