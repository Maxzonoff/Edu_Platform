import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

conn_params = dict(
    host=os.getenv('host'),
    database=os.getenv('database'),
    user=os.getenv('user'),
    password=os.getenv('password'),
)

def create_user():
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE users
                    (
                    user_id serial PRIMARY KEY,
                    created_at date,
                    full_name varchar(100),
                    login varchar(100) UNIQUE
                    )"""
            )



create_user()