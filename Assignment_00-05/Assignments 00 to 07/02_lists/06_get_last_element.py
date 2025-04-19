# 06_get_last_element

def last_element(lst):
    print(lst[-1])
    
def main():
    lst = get_list()
    last_element(lst)

def get_list():
    lst = []
    element = input("Enter an element: ")
    while element != "":
        lst.append(element)
        element = input("Enter an element: ")
    return lst

if __name__ == '__main__':
    main()