import random


RULES = "Find the greatest common divisor of given numbers."


def is_gcd(tuple_of_numbers):
    first_number = max(tuple_of_numbers[0], tuple_of_numbers[1])
    second_number = min(tuple_of_numbers[0], tuple_of_numbers[1])
    remainder = first_number % second_number
    if remainder == 0:
        return second_number
    else:
        return is_gcd((second_number, remainder))


def generate_game():  # Greatest common divisor
    numbers = (random.randint(1, 50), random.randint(1, 50))
    return (f"{numbers[0]} {numbers[1]}", str(is_gcd(numbers)))
