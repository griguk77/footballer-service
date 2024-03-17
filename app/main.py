from fastapi import FastAPI, APIRouter

app = FastAPI(openapi_url="/api/v1/footballers/openapi.json", docs_url="/api/v1/footballers/docs")

footballers_router = APIRouter()

footballers = [
    {'footballers_id': 1, 'name': 'Mbappe',
     'country': 'France',
     'goals': '50', 'age': '34'},
    {'footballers_id': 2, 'name': 'Ronaldo',
     'country': 'Portugal',
     'goals': '5', 'age': '26'},
    {'footballers_id': 3, 'name': 'Akinfeev',
     'country': 'Russia',
     'goals': '90', 'age': '47'}
]


@footballers_router.get("/")
async def read_footballers():
    return footballers

@footballers_router.get("/{footballers_id}")
async def read_footballer(footballers_id: int):
    for footballer in footballers:
        if footballer['footballers_id'] == footballers_id:
            return footballer
    return None

app.include_router(footballers_router, prefix='/api/v1/footballers', tags=['footballers'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)