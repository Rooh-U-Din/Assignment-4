# Project 3-Rock, paper, scissors Python Project

import random
from termcolor import colored


def play():
    choises = ["rock","paper","scissors"]

    user_choice = 0
    while True:
        user_choice = input("Enter rock, paper, or scissors and if you want to exit click (Enter): ").lower()
        computer_guess = random.choice(choises)
        if user_choice == computer_guess:
            print(colored("Tie", "blue", attrs=["bold"]))
        elif user_choice == "rock" and computer_guess == "scissors":
            print(colored("You win", "green", attrs=["bold"]))
        elif user_choice == "scissors" and computer_guess == "paper":
            print(colored("You win", "green", attrs=["bold"]))
        elif user_choice == "paper" and computer_guess == "rock":
            print(colored("You win", "green", attrs=["bold"]))
        elif user_choice == "":
            print(colored("Goodbye see you later!","yellow"))
            break
        else:
            print(colored("You lost", "red", attrs=["bold"]))
            
        print(colored(f"Computer guess was: {computer_guess}",attrs=["bold"]))
        
        
        
play()