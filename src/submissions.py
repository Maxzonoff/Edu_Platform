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


def add_submissions(problem_id: int, text: str, state: str='NEW'):
    created_value = datetime.datetime.now().strftime('%Y-%m-%d')
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""INSERT INTO submission (created, problem_id, text, state)
                        VALUES ('{created_value}', '{problem_id}', '{text}', '{state}');""")


def select_new_submissions():
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT sub_id, problem_id, text FROM submission WHERE state = 'NEW'")
            return cur.fetchall()

def update_status(submission_id, new_state):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE submission SET state = '{new_state}' WHERE sub_id = {submission_id}")


def get_graded():
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""SELECT sub_id, state FROM submission WHERE state = 'ok' OR state = 'fail' """)
            return cur.fetchall()