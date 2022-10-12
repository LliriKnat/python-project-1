import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, number + 1):
        if number % i == 0 and number != i:
            return 'no'
        elif number % i == 0 and number == i:
            return 'yes'
    return 'no'


def generate_game():
    number = random.randint(1, 50)
    return (str(number), is_prime(number))
