# 01_dicesimulator

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

dice = 6

def roll_dice():
    die1 = int(random.randint(1, dice))
    die2 = int(random.randint(1, dice))
    total:int = die1 + die2
    print(f"Total of two dice: {total}")


def main():
    roll_dice()
    roll_dice()
    roll_dice()
    
if __name__ == '__main__':
    main()
