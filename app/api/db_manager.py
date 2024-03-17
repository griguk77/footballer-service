from app.api.models import FootballerIn, FootballerOut, FootballerUpdate
from app.api.db import footballers, database


async def add_footballer(payload: FootballerIn):
    query = footballers.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_footballers():
    query = footballers.select()
    return await database.fetch_all(query=query)


async def get_footballer(id):
    query = footballers.select(footballers.c.id == id)
    return await database.fetch_one(query=query)


async def delete_footballer(id: int):
    query = footballers.delete().where(footballers.c.id == id)
    return await database.execute(query=query)


async def update_footballer(id: int, payload: FootballerIn):
    query = (
        footballers
        .update()
        .where(footballers.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
