# 02_in_range.py

def in_range(n, low, high):
    if low < n < high:
        print(True)
    else:
        print(False)

def main():
    low = int(input("Enter low number: "))
    n = int(input("Enter mid number: "))
    high = int(input("Enter high number: "))
    in_range(n, low, high)

if __name__ == "__main__":
    main()
