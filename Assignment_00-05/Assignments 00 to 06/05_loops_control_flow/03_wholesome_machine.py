# 03_wholesome_machine

def main():
    affirmation = "I am capable of doing anything I put my mind to."
    user_input = str(input("Enter your affirmation: "))

    while user_input != affirmation:
        print("Try again.")
        print(f"Please say: {affirmation}")
        user_input = str(input("Enter your affirmation: "))

    print("You did it!")

if __name__ == "__main__":
    main()