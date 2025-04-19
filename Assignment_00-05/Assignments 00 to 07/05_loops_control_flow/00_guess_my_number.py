# 00_guess_my_number

import random
def main():
    number = random.randint(1, 99)
    guess = int(input("Guess the number between 1 to 99: "))
    
    while guess != number:
        if guess > number:
            print("Too high")
        else:
            print("Too low")
        guess = int(input("Guess the number between 1 to 99: "))
    print("You guessed it!")
    print("The number was", number)

if __name__ == "__main__":
    main()