import random
incorrect_guesses_remaining = 6
guessed_letters = []

difficulty_levels = {
    '1': {'word_length': (1, 4)},
    '2': {'word_length': (5, 6)},
    '3': {'word_length': (7, 10)}
}

def choose_word(difficulty_level):
    word_list = ["canada", "brazil", "mexico", "china", "japan", "india", "germany", "peru", "france", "bolivia"]
    try:
        if difficulty_level == "1":
            word_list = [word for word in word_list if 1 <= len(word) <= 4]
        elif difficulty_level == "2":
            word_list = [word for word in word_list if 5 <= len(word) <= 6]
        elif difficulty_level == "3":
            word_list = [word for word in word_list if 7 <= len(word) <= 10]

        return random.choice(word_list)
    except ValueError:
        print("It's invalid. Please choose a number between 1-3")

def initialize_game(difficulty_level):
    word = choose_word(difficulty_level)
    current_word = ['_'] * len(word)
    global incorrect_guesses_remaining
    return word, current_word, guessed_letters, incorrect_guesses_remaining

def display_game(current_word, guessed_letters, incorrect_guesses_remaining):
    print()
    print("Current word:", " ".join(current_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print(f"Incorrect guesses remaining: {incorrect_guesses_remaining}")

def update_current_word(word, current_word, letter):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                current_word[i] = letter
        return True

def play_hangman():
    print("Welcome to Hangman!")
    print("Choose a difficulty level:")
    for key, value in difficulty_levels.items():
        print(f"{key}: Word length between {value['word_length'][0]} and {value['word_length'][1]}")
    difficulty_level = input("Enter difficulty level (1, 2, or 3): ")

    while difficulty_level not in difficulty_levels:
        print("Invalid difficulty level. Please choose among the available options.")
        difficulty_level = input("Enter difficulty level (1, 2, or 3): ")

    word, current_word, guessed_letters, incorrect_guesses_remaining = initialize_game(difficulty_level)

    while incorrect_guesses_remaining > 0 and '_' in current_word:
        display_game(current_word, guessed_letters, incorrect_guesses_remaining)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if update_current_word(word, current_word, guess):
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses_remaining -= 1

    display_game(current_word, guessed_letters, incorrect_guesses_remaining)

    if '_' not in current_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)
play_hangman()