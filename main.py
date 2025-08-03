import psycopg2

from src.queries import get_user_id, get_username, insert_user, select_random_problem, add_answer


def main():
    auth_user_id = None

    while True:
        if auth_user_id is not None:
            username = get_username(auth_user_id)
            print(f"Добро пожаловать {username}")
        if auth_user_id is None:
            print("1. Войти")
            print("2. Зарегистрироваться")
        else:
            print("3. Выйти")
            print("4. Получить вопрос ")
        print("5. Завершить программу ")
        user = input()
        match user:
            case "1":
                if auth_user_id is not None:
                    print("Вы ввели не верный пункт меню ")
                    continue
                username = input("Введите логин: ")
                password = input("Введите пароль: ")
                user_id = get_user_id(username, password)
                if user_id is None:
                    print("Неверный логин или пароль ")
                else:
                    print("Пользователь авторизован ")
                    auth_user_id = user_id
            case "2":
                if auth_user_id is not None:
                    print("Вы ввели не верный пункт меню ")
                    continue
                username = input("Введите логин: ")
                password = input("Введите пароль: ")
                try:
                    insert_user(username, password)
                except psycopg2.errors.UniqueViolation:
                    print("Пользователь уже существует! ")
                except Exception:
                    print("Ошибка при создании пользователя! ")
                else:
                    print(f"{username} создан!")
            case "3":
                if auth_user_id is None:
                    print("Вы ввели не верный пункт меню ")
                    continue
                auth_user_id = None
                print("Вы вышли из аккаунта ")
            case "4":
                if auth_user_id is None:
                    print("Вы ввели не верный пункт меню ")
                    continue
                res = select_random_problem()
                print(res[1])
                answer = input('Введите ответ ')
                add_answer(res[0], auth_user_id, answer)
                print('Ответ записан в базу данных ')
            case "5":
                print("Программа завершена. ")
                return
            case _:
                print("Не верный пункт меню. ")


if __name__ == "__main__":
    main()
