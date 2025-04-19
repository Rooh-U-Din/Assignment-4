# 05_double_it

def main():
    curr_value = int(input("Enter a number: "))
    curr_value = curr_value * 2
    
    while curr_value < 100:
        
        print("The new value is", curr_value)
        curr_value = int(input("Enter a number: "))
        curr_value = curr_value * 2

    print("The new value is greater than or equal to 100:", curr_value)
    

if __name__ == "__main__":
    main()