import psycopg2
from src.config import Config


def get_connection():
    return psycopg2.connect(host=Config.host,
                            database=Config.database,
                            user=Config.db_user,
                            password=Config.password
                            )



# запрос создания базы данных
# CREATE TABLE users (
# 	id SERIAL PRIMARY KEY,
# 	username VARCHAR(100) UNIQUE NOT NULL,
# 	password VARCHAR(100) NOT NULL
# )