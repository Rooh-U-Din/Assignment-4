# High Low

import random

NUM_ROUNDS = 5

def get_valid_guess():
    """Get a valid user input: 'h' for higher or 'l' for lower"""
    while True:
        guess = input("Do you think your number is higher or lower than the computer's? (h/l): ").lower()
        if guess in ["h", "l"]:
            return guess
        else:
            print("Please enter either 'h' for higher or 'l' for lower.")

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    player_score = 0
    computer_score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        guess = get_valid_guess()

        correct = (
            (guess == "h" and user_number > computer_number) or
            (guess == "l" and user_number < computer_number)
        )

        if correct:
            print(f"You were right! The computer's number was {computer_number}")
            player_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
            computer_score += 1

        print(f"Your score: {player_score} | Computer's score: {computer_score}")
        print()


    print("Thanks for playing!")
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")

    if player_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif player_score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

    if computer_score > player_score:
        print("The computer wins this time!")
    elif computer_score < player_score:
        print("You beat the computer!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
