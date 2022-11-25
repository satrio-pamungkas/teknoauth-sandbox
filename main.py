from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils.env import env
from app.routers import auth, user

app = FastAPI()

# Default to all IP
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(auth.router, tags=['User'], prefix='/api/user')

@app.get("/")
async def read_root():
    return {"Hello": "World"}
