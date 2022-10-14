import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def generate_game():
    number = random.randint(1, 100)
    if is_even(number):
        return (f"{number}", "yes")
    else:
        return (f"{number}", "no")
