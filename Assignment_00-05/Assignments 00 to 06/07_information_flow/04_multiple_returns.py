# 04_multiple_returns

def get_user_data():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    email = input("Enter your email: ")
    return f"{firstName},{lastName},{email}."
def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)
if __name__ == "__main__":
    main()
    