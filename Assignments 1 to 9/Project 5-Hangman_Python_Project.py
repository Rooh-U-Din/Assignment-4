import random
from termcolor import colored

def hangman():
    words = ["python", "typescript", "genai", "nextjs", "agenticai"]
    
    user_input = int(input(colored("Enter a number between 1 and 5: ", "cyan", attrs=["bold"])))
    if user_input < 1 or user_input > 5:
        print(colored("Invalid number. Please run the game again.", "red", attrs=["bold"]))
        return

    selected_word = words[user_input - 1]
    blanks = ["_"] * len(selected_word)
    attempts = 3
    incorrect = []

    while attempts > 0:        
        print("\nWord: " + colored(" ".join(blanks), "blue", attrs=["bold"]))
        print(colored("Incorrect guesses: ", "magenta") + ", ".join(incorrect))
        print(colored(f"Remaining attempts: {attempts}", "yellow", attrs=["bold"]))

        guess = input(colored("Guess a letter: ", "cyan")).lower()

        if not guess.isalpha() or len(guess) != 1:
            print(colored("Please enter a single valid letter.", "red"))
            continue

        if guess in blanks or guess in incorrect:
            print(colored("You already guessed that letter.", "yellow"))
            continue

        if guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    blanks[i] = guess
            print(colored("✅ Correct!", "green", attrs=["bold"]))
        else:
            incorrect.append(guess)
            attempts -= 1
            print(colored("❌ Wrong guess!", "red", attrs=["bold"]))

        if "_" not in blanks:
            print(colored("\n🎉 Congratulations! You guessed the word: ", "green", attrs=["bold"]) + selected_word)
            break

    if "_" in blanks:
        print(colored("\n💀 Game Over! The word was: ", "red", attrs=["bold"]) + selected_word)

hangman()
