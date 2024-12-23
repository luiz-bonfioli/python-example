from typing import Optional

from src.core.http.http_client import get_posts
from src.domain.posts_repository import PostsRepository


class PostsService:

    def __init__(self, posts_repository: PostsRepository):
        self.__posts_repository = posts_repository

    def save_posts(self, posts):
        self.__posts_repository.insert_posts(posts)

    @staticmethod
    def get_posts_by_user_id(user_id: Optional[int]):
        params = {
            "userId": user_id
        }
        return get_posts(params)

    @staticmethod
    def get_posts_by_id(entity_id: Optional[int]):
        params = {
            "id": entity_id
        }
        return get_posts(params)

    @staticmethod
    def get_posts_by_params(user_id: Optional[int], entity_id: Optional[int]):
        params = {
            "userId": user_id,
            "id": entity_id
        }
        return get_posts(params)

    @staticmethod
    def get_all_posts():
        return get_posts()
