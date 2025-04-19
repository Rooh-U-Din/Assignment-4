# 07_get_list

def main():
    my_lst = []
    element = input("Enter an element: ")
    while element != "":
        my_lst.append(element)
        element = input("Enter an element: ")
    print(my_lst)


if __name__ == '__main__':
    main()
