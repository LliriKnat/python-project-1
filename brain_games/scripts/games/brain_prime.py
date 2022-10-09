from brain_games.scripts.games import brain_even
import prompt
import random


def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, number + 1):
        if number % i == 0 and number != i:
            return 'no'
        elif number % i == 0 and number == i:
            return 'yes'
    return 'no'


def play_prime():
    number = random.randint(1, 50)
    print(f"Question: {number}")
    user_answer = prompt.string("Your answer: ")
    return brain_even.analyze_answer(user_answer, is_prime(number))


def main():
    name = brain_even.greet_user()
    print('Answer "yes" if the number is prime, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        if play_prime():
            correct_answers += 1
        else:
            print(f"Lets try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
