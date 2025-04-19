# Project 3-Guess_the_Number_Game_Python_Project_(user)

low = 0
high = 100
answer = ""

think_number = input("Think A number bitween 1-100: ")

while answer != "c":
    guess = (low + high) // 2
    print(f"Computer number is {guess}: ")
    answer= input("Please answer in c(correct) l(low) and h(high): ").lower()
    if answer == "h":
        high = guess - 1
    elif answer == "l":
        low = guess + 1
    elif answer != "c":
        print("Please respond with only h, l, or c.")
print(f"Yay! I guessed your number!{think_number}")
