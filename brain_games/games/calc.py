import random


RULES = "What is the result of the expression?"


def generate_game():
    operands = ["+", "-", "*"]  # can create a dict with lambda functions
    nums = (random.randint(1, 10), random.randint(1, 10))
    operand = operands[random.randint(0, 2)]
    answer = eval(f"{nums[0]} {operand} {nums[1]}")
    return (f"{nums[0]} {operand} {nums[1]}", str(answer))
