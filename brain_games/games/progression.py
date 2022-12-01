from random import randint


task = 'What number is missing in the progression?'


def progression():
    pr_start = randint(1, 20)
    pr_step = randint(1, 10)
    pr_len = randint(5, 10)
    pr_list = list(str(_) for _ in range
                   (pr_start, pr_start + pr_len * pr_step, pr_step))
    question_index = randint(0, pr_len - 1)
    correct_answer = pr_list[question_index]
    pr_list[question_index] = '..'
    question = ' '.join(pr_list)
    return question, correct_answer
