# 06_rolldice

import random

def main():
    dice:int = 6
    die1 = random.randint(1,dice)
    die2 = random.randint(1,dice)
    total = die1 + die2
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)
    
if __name__ == '__main__':
    main()