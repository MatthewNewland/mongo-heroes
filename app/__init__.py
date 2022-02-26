from beanie import init_beanie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from .models import Hero
from .routers import hero_router

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(hero_router, prefix="/heroes")


@app.on_event("startup")
async def startup():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(client.heroes, document_models=[Hero])
