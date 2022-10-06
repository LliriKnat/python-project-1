import prompt
import random


def is_even(number):
    answer = prompt.string("Your answer: ")
    if number % 2 == 0 and answer != "yes":
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    elif number % 2 != 0 and answer != "no":
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
        return False
    else:
        print("Correct!")
        return True


def main():
    correct_answers = 0
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
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
