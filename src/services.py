from src.problems import select_random_problem, get_problem_by_id, add_problem
from src.submissions import add_submissions, select_new_submissions, update_status, get_graded


def question():
    problem_id, problem_text = select_random_problem()
    print(f'Вопрос: {problem_text}')
    answer = input('Введите ответ: ')
    add_submissions(problem_id, answer)
    print('Ответ сохранен.')


def grade_submission():
    for sub in select_new_submissions():
        submission_id, problem_id, submission_text = sub
        problem_text = get_problem_by_id(problem_id)[0]
        print(problem_text)
        print(submission_text)
        new_state = input('Введите новый статус ')
        if new_state != 'ok' and new_state !='fail':
            print('Статус не корректный')
            continue
        else:
            update_status(submission_id, new_state)


def get_graded_submission():
    res = get_graded()
    for x in res:
        sub_id, state = x
        print(f'Посылка: {sub_id} - {state}')

def new_problem():
    content = input('Введите текст задания: ')
    add_problem(content)
    print('Задача добавлена. ')
