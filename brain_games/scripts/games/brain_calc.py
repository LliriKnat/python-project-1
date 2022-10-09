from brain_games.scripts.games import brain_even as ev
import random
import prompt


def play_calc():
    operands = ["+", "-", "*"]  # can create a dict with lambda functions
    nums = (random.randint(1, 10), random.randint(1, 10))
    operand = operands[random.randint(0, 2)]
    print(f"Question: {nums[0]} {operand} {nums[1]}")
    answer = prompt.integer("Your answer: ")
    return ev.analyze_answer(answer, eval(f"{nums[0]} {operand} {nums[1]}"))


def main():
    name = ev.greet_user()
    print("What is the result of the expression?")
    correct_answers = 0
    while correct_answers < 3:
        if play_calc():
            correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
