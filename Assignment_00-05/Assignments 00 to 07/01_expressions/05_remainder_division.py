# 05_remainder_division.

def main():
    number1 = int(input("Please enter an integer to be divided: "))
    number2 = int(input("Please enter an integer to divide by: "))
    number3 = number1 // number2
    reminder = number1 % number2
    print (f"The result of this division is {number3} with a remainder of {reminder}")
    
if __name__ == '__main__':
    main()