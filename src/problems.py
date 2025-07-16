import os
import psycopg2
import datetime


from dotenv import load_dotenv

load_dotenv()

conn_params = dict(
    host=os.getenv('host'),
    database=os.getenv('database'),
    user=os.getenv('user'),
    password=os.getenv('password'),
)


def add_problem(content: str):
    created_value = datetime.datetime.now().strftime('%Y-%m-%d')
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""INSERT INTO problem (created, content)
                        VALUES ('{created_value}', '{content}');""")


def select_random_problem():
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT problem_id, content FROM problem ORDER BY RANDOM() limit 1;""")
            return cur.fetchall()[0]

def get_problem_by_id(problem_id):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT content FROM problem WHERE problem_id = {problem_id}")
            return cur.fetchall()[0]


