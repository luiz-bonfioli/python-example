import json
import uuid

from src.core.database.database import Database
from src.core.database.schema import INSERT_BATCH


class PostsRepository:

    def __init__(self, db: Database):
        self.__db = db

    def insert_posts(self, posts):
        self.__db.execute_insert(INSERT_BATCH, (str(uuid.uuid4()), json.dumps(posts)))
