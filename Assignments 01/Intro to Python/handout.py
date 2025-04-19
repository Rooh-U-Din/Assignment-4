# Planetary Weight Calculator

# Mercury: 37.6%
# Venus: 88.9%
# Mars: 37.8%
# Jupiter: 236.0%
# Saturn: 108.1%
# Uranus: 81.5%
# Neptune: 114.0%

# we can also use a dictionary but i use simple variables because its easier for me

# planet_gravity = {
#     "Mercury": 3.76,
#     "Venus": 8.89,
#     "Earth": 9.8,
#     "Mars": 3.78,
#     "Jupiter": 236.0,
#     "Saturn": 108.1,
#     "Uranus": 81.5,
#     "Neptune": 114.0
# }
# like this 

earth_gravity = 9.81
mars_gravity = 3.78
mercury_gravity = 3.76
venus_gravity = 8.89
jupiter_gravity = 236
saturn_gravity = 108.1
uranus_gravity = 81.5
neptune_gravity = 114

def main():
    weight = float(input("Enter your weight: "))
    planet = input("Enter the planet (Earth or Mars or Venus or Mercury or Jupiter or Saturn or Uranus or Neptune): ").capitalize()
    if planet == "Earth":
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight, "kg on Earth.")
    elif planet == "Mars":
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight *(mars_gravity / earth_gravity), "kg on Mars.")
    elif planet == "Venus":
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight *(venus_gravity / earth_gravity), "kg on Venus.")
    elif planet == "Mercury": 
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight *(mercury_gravity / earth_gravity), "kg on Mercury.")
    elif planet == "Jupiter":
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight *(jupiter_gravity / earth_gravity), "kg on Jupiter.")
    elif planet == "Saturn":
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight *(saturn_gravity / earth_gravity), "kg on Saturn.")
    elif planet == "Uranus":
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight *(uranus_gravity / earth_gravity), "kg on Uranus.")
    elif planet == "Neptune":
        print("Your weight is", weight, "kg on Earth.")
        print("Your weight is", weight *(neptune_gravity / earth_gravity), "kg on Neptune.")

    else:
        print("Invalid planet.")

if __name__ == "__main__":
    main()