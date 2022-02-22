from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Depends, Request

from .models import Hero, HeroUpdate


hero_router = APIRouter()


async def get_hero(id: PydanticObjectId) -> Hero:
    result = await Hero.get(id)
    if result is None:
        raise HTTPException(status_code=404, detail="Not found")
    return result


@hero_router.get("/", response_model=list[Hero])
async def read_heroes(req: Request):
    return await Hero.find(req.query_params).to_list()


@hero_router.post("/", response_model=Hero)
async def create_hero(hero: Hero):
    await hero.create()
    return hero


@hero_router.get("/by-id/{id}", response_model=Hero)
async def read_hero(hero: Hero = Depends(get_hero)):
    return hero


@hero_router.post("/by-id/{id}", response_model=Hero)
async def update_hero(update: HeroUpdate, hero: Hero = Depends(get_hero)):
    update_dict = update.dict(exclude_unset=True)
    await hero.set(update_dict)
    return hero


@hero_router.delete("/by-id/{id}")
async def delete_hero(hero: Hero = Depends(get_hero)):
    await hero.delete()
    return {"message": "Hero successfully deleted"}