import random


RULES = "What number is missing in the progression?"


def generate_progression():
    first_number = random.randint(0, 50)
    common_difference = random.randint(-10, 10)
    progression = [first_number]
    for i in range(10):
        progression.append(progression[i] + common_difference)
    missing_index = random.randint(0, len(progression) - 1)
    missing_number = progression[missing_index]
    progression[missing_index] = ".."
    return (progression, missing_number)


def generate_game():
    progression = generate_progression()
    question = ' '.join(map(str, progression[0]))
    return (question, str(progression[1]))
