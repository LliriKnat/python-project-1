import prompt


def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    answers_count = 0
    print(game.RULES)
    while answers_count < 3:
        question, correct_answer = game.generate_game()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            answers_count += 1
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.".format
                (user_answer, correct_answer))
            print(f"Let's try again, {name}!")
            break
    if answers_count == 3:
        print(f"Congratulations, {name}!")
