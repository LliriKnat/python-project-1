from brain_games.scripts.games import brain_even
import prompt
import random


def is_gcd(tuple_of_numbers):
    first_number = max(tuple_of_numbers[0], tuple_of_numbers[1])
    second_number = min(tuple_of_numbers[0], tuple_of_numbers[1])
    remainder = first_number % second_number
    if remainder == 0:
        return second_number
    else:
        return is_gcd((second_number, remainder))


def play_gcd():  # Greatest common divisor
    numbers = \
        (random.randint(1, 50), random.randint(1, 50))  # Using tuples this time
    print(f"Question: {numbers[0]} {numbers[1]}")
    answer = prompt.integer("Your answer: ")
    return brain_even.analyze_answer(answer, is_gcd(numbers))


def main():
    name = brain_even.greet_user()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    while correct_answers < 3:
        if play_gcd():
            correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
