# 02_count_even

def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

def get_lst_int():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        lst.append(int(user_input))  
    return lst

def main():
    lst = get_lst_int()
    print(f"Count of even numbers: {count_even(lst)}")

if __name__ == "__main__":
    main()
