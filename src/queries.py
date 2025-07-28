from src.db import get_connection


def insert_user(username: str, password: str) -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password),
            )


def get_user_id(username: str, password: str) -> int | None:
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
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT username FROM users WHERE id=%s",
                (user_id,),
            )
            result = cur.fetchone()
            return result[0]
