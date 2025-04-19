# 01_double_it
def main():
    num = int(input("Enter a number: "))
    
    curr_value = num
    
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')
    
    print()

if __name__ == "__main__":
    main()