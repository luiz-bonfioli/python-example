SCHEMA = "CREATE SCHEMA IF NOT EXISTS hello_world;"
SET_SCHEMA = "SET SCHEMA 'hello_world';"
POSTS_TABLE = "CREATE TABLE IF NOT EXISTS hello_world.posts( id uuid PRIMARY KEY, content JSONB);"
INSERT_BATCH = "INSERT INTO hello_world.posts (id, content) VALUES (%s, %s);"
