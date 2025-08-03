from src.db import get_connection


def insert_user(username: str, password: str) -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password),
            )


def get_user_id(username: str, password: str) -> int | None:
    """ Функция принимает логин и пароль и возвращает ID если он существует
    либо None если не существует"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM users WHERE username=%s AND password=%s",
                (username, password),
            )
            result = cur.fetchone()
            if result is None:
                return None
            return result[0]


def get_username(user_id: int) -> str:
    """ Функция принимает ID и возвращает логин """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT username FROM users WHERE id=%s",
                (user_id,),
            )
            result = cur.fetchone()
            return result[0]


def select_random_problem():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """SELECT id, text FROM problems ORDER BY RANDOM() limit 1;"""
            )
            return cur.fetchone()


def add_answer(problem_id: int, user_id: int, answer: str) -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT into submissions (problem_id, user_id, text) values (%s, %s, %s)""", (problem_id, user_id, answer)
            )

