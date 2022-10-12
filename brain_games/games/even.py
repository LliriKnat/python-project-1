import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    number = random.randint(1, 100)
    if number % 2 == 0:
        return (f"{number}", "yes")
    else:
        return (f"{number}", "no")
