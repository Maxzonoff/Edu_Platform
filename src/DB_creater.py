from src.db import get_connection

def create_problem():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE problem
                    (
                    problem_id serial PRIMARY KEY,
                    created date,
                    content text
                    )"""
            )


def create_submission():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE submission
                (
                sub_id serial PRIMARY KEY,
                created date,
                problem_id int REFERENCES problem (problem_id),
                text text,
                state text
                )"""
            )

def drop_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """DROP TABLE problem CASCADE;
                DROP TABLE submission CASCADE;
                """
            )




if __name__ == '__main__':
    # drop_table()
    create_problem()
    create_submission()