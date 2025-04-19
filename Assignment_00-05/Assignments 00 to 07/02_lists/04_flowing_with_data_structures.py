# 04_flowing_with_data_structures

def three_copies(mylist,data):
    for i in range(3):
        mylist.append(data)

def main():
    massege = input("Enter a massege: ")
    mylist = []
    print(f"before my list is {mylist}")
    three_copies(mylist,massege)
    print(f"after my list is {mylist}")
    
if __name__ == "__main__":
    main()
    