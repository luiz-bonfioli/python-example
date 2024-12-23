from src.common.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
from src.core.database.database import Database
from src.domain.posts_repository import PostsRepository
from src.domain.posts_service import PostsService


def get_database():
    db = Database()
    db.connect(host=DB_HOST,
               port=DB_PORT,
               dbname=DB_NAME,
               user=DB_USER,
               password=DB_PASSWORD)
    return db


def get_posts_service() -> PostsService:
    return PostsService(posts_repository=get_posts_repository())


def get_posts_repository():
    return PostsRepository(db=get_database())
