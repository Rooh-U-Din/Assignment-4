# 02_double_list

def double_list(numbers: list[int]) -> list[int]:
    return [x * 2 for x in numbers]

def main():
    numbers = [1, 2, 3, 4, 5]
    print(double_list(numbers))
    
if __name__ == "__main__":
    main()