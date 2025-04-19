# Project 2: Guess the Number Game Python Project (computer)

import random

computer_number = random.randint(1, 100)
guess = 0

while guess != computer_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < computer_number:
        print("Too low!")
    elif guess > computer_number:
        print("Too high!")
    else:
        print("You got it!")
        break

print(f"The computer's number was {computer_number}")