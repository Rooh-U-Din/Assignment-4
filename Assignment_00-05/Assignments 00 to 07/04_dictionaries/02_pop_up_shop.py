# 02_pop_up_shop

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    total_cost = 0
    for fruit, price in fruits.items():
        total_cost += price
        print(f"{fruit}: ${price:.2f}")
    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
