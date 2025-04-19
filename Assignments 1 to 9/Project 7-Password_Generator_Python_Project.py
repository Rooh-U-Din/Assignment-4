import random
import string

def generate_password(length):
    password = []
    characters = string.ascii_letters + string.digits + string.punctuation
    
    for i in range(length):
        password.append(random.choice(characters))
    
    password = "".join(password)
    return password

length = int(input("Enter the length of the password: "))

password = generate_password(length)
print(f"Generated Password: {password}")
