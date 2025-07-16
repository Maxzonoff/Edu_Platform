from src.services import question, grade_submission, get_graded_submission, new_problem


def menu():
    print('1. Ответить на случайный вопрос.')
    print('2. Режим оценки. ')
    print('3. Получить оценки. ')
    print('4. Добавить задачу. ')
    print('5. ')
    print('6. ')
    print('7. ')
    print('"Стоп" для завершения работы.')
    print()
    command = input('Введите команду: ').lower()
    if command == '1':
        question()
    elif command == '2':
        grade_submission()
    elif command == '3':
        get_graded_submission()
    elif command == '4':
        new_problem()
    elif command == 'стоп':
        return

