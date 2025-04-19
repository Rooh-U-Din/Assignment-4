# 01_phonebook

def read_phonebook(filename):
    phonebook = {}
    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        phone = input("Enter a phone number: ")
        phonebook[name] = phone
    return phonebook
def print_phonebook(phonebook):
    for name,phone in phonebook.items():
        print(f"{name}: {phone}")

def look_up(phonebook):
    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print(f"{name} not found")
def main():
    phonebook = read_phonebook("phonebook.txt")
    print_phonebook(phonebook)
    look_up(phonebook)

if __name__ == "__main__":
    main()