# 03_in_stock

fruits = {
    "apple": 20,
    "banana": 12,
    "mango": 90,
}

def num_in_stock(fruit):
    if fruit in fruits:
        print(f"{fruit} is in stock with quantity {fruits[fruit]}")
    else:
        print(f"{fruit} is not available")

def main():
    fruit = input("Enter the fruit name to check availability: ").lower()
    num_in_stock(fruit)

if __name__ == "__main__":
    main()
