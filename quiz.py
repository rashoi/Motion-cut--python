# Function to start a new game
def new_game1():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    score(correct_guesses, guesses)


# Function to check if the answer is correct
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# Function to display the score
def score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


# Dictionary of questions and their correct answers
questions = {
    "1. Who is the current President of the United States?": "A",
    "2. What is the capital of France?": "D",
    "3. Which planet is known as the Red Planet?": "C",
    "4. What is the largest ocean on Earth?": "D"
}

# List of options for each question
options = [
    ["A) Joe Biden", "B) Donald Trump", "C) Barack Obama", "D) George W. Bush"],
    ["A) Rome", "B) Berlin", "C) Madrid", "D) Paris"],
    ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
    ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"]
]

# Start the game
new_game1()
