import prompt
import random


def greet_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def analyze_answer(user_answer, correct_asnwer):
    if user_answer == correct_asnwer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_asnwer}'.")
        return False


def is_even(number):
    answer = prompt.string("Your answer: ")
    if number % 2 == 0:
        return analyze_answer(answer, "yes")
    else:
        return analyze_answer(answer, "no")


def main():
    correct_answers = 0
    name = greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        if is_even(number):
            correct_answers += 1
        else:
            print(f"Lets try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
