from brain_games.scripts.games import brain_even
import random
import prompt


def play_calc():
    operands = ["+", "-", "*"]  # can create a dict with lambda functions
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operand = operands[random.randint(0, 2)]
    print(f"Question: {first_number} {operand} {second_number}")
    answer = prompt.integer("Your answer: ")
    return brain_even.analyze_answer(answer, eval(f"{first_number} {operand} {second_number}"))  # eval is discouraged for security risks


def main():
    name = brain_even.greet_user()
    print("What is the result of the expression?")
    correct_answers = 0
    while correct_answers < 3:
        if play_calc():
            correct_answers += 1
        else:
            print(f"Lets try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
