# 00_choosing_returns

ADULT_AGE = 18

def is_of_age(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False
def main():
    age = int(input("Enter your age for checking if you are adult or not: "))
    age = is_of_age(age)
    print(age)
if __name__ == "__main__":
    main()