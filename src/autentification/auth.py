import os
import datetime

import psycopg2

from dotenv import load_dotenv

load_dotenv()

conn_params = dict(
    host=os.getenv('host'),
    database=os.getenv('database'),
    user=os.getenv('user'),
    password=os.getenv('password'),
)


def auth(login: str) -> int | None:
    '''Функция принимает логин и возвращает ID если он существует
    либо None если не существует'''
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""SELECT * FROM USERS
            WHERE login = '{login}'""")
            res = cur.fetchall()
            if not res:
                return None
            return res[0][0]


def auth_user():
    login = input('Введите логин: ')
    if auth(login) == None:
        print('Процесс регистрации ')
        login = input('Введите логин ')
        fullname = input('Введите полное имя ')
        register_user(login, fullname)

    else:
        print('Пользователь авторизован ')


def register_user(login, fullname):
    created_value = datetime.datetime.now().strftime('%Y-%m-%d')
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(f"""INSERT INTO users (created_at, full_name, login)
                            VALUES ('{created_value}', '{fullname}','{login}');""")
            except Exception:
                print('Не удалось создать пользователя! ')





register_user('test', 'abc')
register_user('test', 'abc')
auth_user()
