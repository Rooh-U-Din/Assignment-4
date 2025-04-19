# 00_averages

def average(a: float, b: float):
    return (a + b) / 2

def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    avg = average(a, b)
    print("avg_1", a)
    print("avg_2", b)
    print("The average is:", avg)

if __name__ == "__main__":
    main()
