# 03_guess_my_number

import random

def main():
    secret_number = random.randint(1, 99)
    guess = 0

    while guess != secret_number:
        guess = int(input("Guess a number between 1, 99: "))
        if guess < secret_number:
            print("Too low")
        else:
            print("Too high")

    print("You got it!")

if __name__ == "__main__":
    main()
        