from src.queries import insert_user
import psycopg2

def main():
    while True:
        print('1. Войти')
        print('2. Зарегистрироваться')
        print('3. Выйти')
        user = input()
        match user:
            case '1':
                print('Войти')
            case '2':
                username = input('Введите логин: ')
                password = input('Введите пароль: ')
                try:
                    insert_user(username, password)
                except psycopg2.errors.UniqueViolation:
                    print('Пользователь уже существует! ')
                except Exception:
                    print('Ошибка при создании пользователя! ')
                else:
                    print(f'{username} создан!')
            case '3':
                print('Программа завершена. ')
                return
            case _:
                print('Не верный пункт меню. ')

if __name__ == '__main__':
    main()
