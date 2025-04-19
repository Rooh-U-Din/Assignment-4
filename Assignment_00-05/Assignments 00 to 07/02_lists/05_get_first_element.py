# 05_get_first_element.


def first_element(lst):
    print(lst[0])


def get_list ():
    
    lst = []
    element = input("Enter an element: ")
    while element != "":
        lst.append(element)
        element = input("Enter an element: ")
        return lst

def main():
    lst = get_list()
    first_element(lst)
    
if __name__ == '__main__':
    main()