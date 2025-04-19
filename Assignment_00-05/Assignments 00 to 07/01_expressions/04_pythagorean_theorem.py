# 04_pythagorean_theorem

import math 

def main():
    ab = float(input("Enter AB: "))
    ac = float(input("Enter AC: "))
    bc:float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc}")


if __name__ == '__main__':
    main()