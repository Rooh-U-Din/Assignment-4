# add two numbers

def main ():
    print("Enter the numbers for sum")
    number1 = str(input("Enter first number: "))
    num1 = int(number1)
    number2 = str(input("Enter second number: "))
    num2 = int(number2)
    sum = num1 + num2
    print("The sum of", sum)
    
if __name__ == "__main__":
    main()