import random
incorrect_guesses_remaining = 6
guessed_letters = []

def choose_word():
    word_list = ["canada", "brazil", "mexico", "china", "japan", "india", "germany", "peru", "france", "bolivia"]
    return random.choice(word_list)

def initialize_game():
    word = choose_word()
    current_word = ['_'] * len(word)
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
    word, current_word, guessed_letters, incorrect_guesses_remaining = initialize_game()

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