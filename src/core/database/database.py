import psycopg2

from src.core.database.schema import SCHEMA, SET_SCHEMA, POSTS_TABLE


class Database:
    __connection = None

    def connect(self, host, port, dbname, user, password):
        if not self.__connection or self.__connection.closed != 0:
            self.__connection = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password
            )

    def create_db(self):
        self.__create_schemas()
        self.__create_tables()

    def __create_schemas(self):
        self.execute(SCHEMA)
        self.execute(SET_SCHEMA)

    def __create_tables(self):
        self.execute(POSTS_TABLE)

    def execute(self, command, values=None):
        cursor = self.__connection.cursor()
        cursor.execute(command, values)
        self.commit()
        cursor.close()

    def execute_insert(self, command, values):
        cursor = self.__connection.cursor()
        cursor.execute(command, values)
        self.commit()
        cursor.close()

    def commit(self):
        self.__connection.commit()
