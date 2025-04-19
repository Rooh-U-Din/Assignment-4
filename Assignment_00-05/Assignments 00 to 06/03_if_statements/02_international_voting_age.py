# 02_international_voting_age

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    age : int = int(input("Enter your age: "))
    
    if age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo.")
    if age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau.")
    if age >= MAYENGUA_AGE:
        print("You can vote in Stanlau where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua.")

if __name__ == "__main__":
    main()