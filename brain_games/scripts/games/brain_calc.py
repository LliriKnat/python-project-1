from brain_games.scripts.games import brain_even
import random
import prompt


def play_calc():
    first_number = random.randint(1,99)
    second_number = random.randint(1,99)
    print(f"Question: {first_number}+{second_number}")
    answer = prompt.integer("Your answer: ")
    return brain_even.analyze_answer(answer, first_number+second_number)

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