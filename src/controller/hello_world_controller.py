from typing import Optional

from fastapi import APIRouter
from fastapi.params import Param, Depends
from starlette.responses import JSONResponse

from src.core.context import get_posts_service

router = APIRouter(prefix='/v1/hello-world', tags=['Hello World'])


@router.get('/hello')
async def hello(user_id: Optional[int] = Param(None, alias="userId"),
                entity_id: Optional[int] = Param(None, alias="id"),
                posts_service=Depends(get_posts_service)) -> JSONResponse:
    return handle_response(posts_service, user_id, entity_id)


def handle_response(posts_service, user_id, entity_id):
    if user_id and entity_id:
        response = posts_service.get_posts_by_params(user_id, entity_id)
    elif user_id:
        response = posts_service.get_posts_by_user_id(user_id, entity_id)
    elif entity_id:
        response = posts_service.get_posts_by_id(entity_id)
    else:
        response = posts_service.get_all_posts()

    if response:
        posts_service.save_posts(response)

    return JSONResponse(content=response)
