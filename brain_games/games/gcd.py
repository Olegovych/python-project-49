from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def gcd():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = f'{first_num} {second_num}'
    smaller, bigger = sorted((first_num, second_num))
    if bigger % smaller == 0:
        return question, str(smaller)
    for div in range(smaller // 2, 0, -1):
        if bigger % div == 0 and smaller % div == 0:
            return question, str(div)
