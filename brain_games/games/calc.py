import random
import operator


RULES = "What is the result of the expression?"


def generate_game():
    operation = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }
    nums = (random.randint(1, 10), random.randint(1, 10))
    operand = random.choice(["+", "-", "*"])
    answer = (operation[operand](nums[0], nums[1]))
    return (f"{nums[0]} {operand} {nums[1]}", str(answer))
