from brain_games.scripts.games import brain_even
import prompt
import random


def generate_progression():
    first_number = random.randint(0, 50)
    common_difference = random.randint(-10, 10)
    progression = [first_number]
    for i in range(10):
        progression.append(progression[i] + common_difference)
    missing_index = random.randint(0, len(progression) - 1)
    missing_number = progression[missing_index]
    progression[missing_index] = ".."
    return (progression, missing_number)


def play_progression():
    progression = generate_progression()
    print(f"Question: {' '.join(map(str, progression[0]))}")
    user_answer = prompt.integer("Your answer: ")
    return brain_even.analyze_answer(user_answer, progression[1])


def main():
    name = brain_even.greet_user()
    print("What number is missing in the progression?")
    correct_answers = 0
    while correct_answers < 3:
        if play_progression():
            correct_answers += 1
        else:
            print(f"Lets try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
