# e=mc2

C:int = 299792458

def main():
    m:float = float(input("Enter mass in kilograms: "))
    e:float = m * C**2
    
    print("e = m * C^2...")
    print("m = " + str(m) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(e) + " joules of energy!")
    
    
if __name__ == '__main__':
    main()