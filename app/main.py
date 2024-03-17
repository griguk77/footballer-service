from fastapi import FastAPI, APIRouter

'''
from api.db import metadata, database, engine

metadata.create_all(engine)
'''
app = FastAPI(openapi_url="/api/v1/footballers/openapi.json", docs_url="/api/v1/footballers/docs")

footballers_router = APIRouter()

footballers = [
    {'clubs_id': 1, 'name': 'Killian', 'surname': 'Mbappe', 'age': 24, 'goals': 135},
    {'clubs_id': 2, 'name': 'Cristiano', 'surname': 'Ronaldo', 'age': 31, 'goals': 837}
]


@footballers_router.get("/")
async def read_footballers():
    return footballers


@footballers_router.get("/{clubs_id}")
async def read_footballer(clubs_id: int):
    foots = []
    for footballer in footballers:
        if footballer['clubs_id'] == clubs_id:
            foots.append(footballer)
    return foots


'''
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
'''
app.include_router(footballers_router, prefix='/api/v1/footballers', tags=['footballers'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
