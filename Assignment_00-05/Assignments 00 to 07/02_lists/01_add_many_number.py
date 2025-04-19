# 01_add_many_number

def add_many(args)-> int:
    result = 0
    for i in args:
        result += i
    return result
def main():
    numbers:list[int] = [1,2,3,4,5]
    sum_of_numbers: int = add_many(numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()