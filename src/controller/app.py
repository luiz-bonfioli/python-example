from fastapi import FastAPI, Depends
from starlette.middleware.gzip import GZipMiddleware

from src.controller import hello_world_controller
from src.core.context import get_database
from src.core.database.database import Database

app = FastAPI()
app.add_middleware(GZipMiddleware)
app.include_router(hello_world_controller.router)


async def create_db():
    db = get_database()
    db.create_db()


@app.on_event("startup")
async def startup():
    await create_db()

# @app.on_event("shutdown")
# async def shutdown():
#     await shutdown_event()

#
# brew install libpq --build-from-source
# brew install openssl
# export LDFLAGS="-L$(brew --prefix openssl)/lib"
# export CPPFLAGS="-I$(brew --prefix openssl)/include"
