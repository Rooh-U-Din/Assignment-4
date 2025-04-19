# 08_shorten

max_length:int = 3

def shorten(lst):
    while len(lst) > max_length:
        lst.pop(0)
        return lst
def get_list():
    lst = []
    element = input("Enter an element: ")
    while element != "":
        lst.append(element)
        element = input("Enter an element: ")
    return lst    
    
def main():
    lst = get_list()
    shorten(lst)
    print(lst)
    
if __name__ == '__main__':
    main()