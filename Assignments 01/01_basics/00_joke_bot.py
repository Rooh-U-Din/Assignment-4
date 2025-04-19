# 00_joke_bot

def main():
    prompt = input("What you want? ").lower()
    joke = """Sophia is heading out to the grocery store.
A programmer tells her: get a liter of milk, and if they have eggs, get 12.
Sophia returns with 13 liters of milk. 
The programmer asks why and Sophia replies: 
'because they had eggs'"""
    sorry = "Sorry I only tell jokes."

    if prompt == "joke":
        print(joke)
    else:
        print(sorry)


if __name__ == "__main__":
    main()
