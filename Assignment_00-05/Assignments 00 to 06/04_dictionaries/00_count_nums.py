
# 00_count_nums

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number or press Enter to finish")
    return numbers

def count_numbers(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return counts

def print_counts(counts):
    for num, count in sorted(counts.items()):
        print(f"{num} appears {count} times.", end=" ")

def main():
    print("Number Counter")
    numbers = get_numbers()
    counts = count_numbers(numbers)
    print_counts(counts)

if __name__ == "__main__":
    main()