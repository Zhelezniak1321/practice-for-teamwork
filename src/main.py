class Helicopter:

    def __init__(self, passengers=0, name="", max_speed=0):
        self.__passengers = passengers  
        self.__name = name 
        self.__max_speed = max_speed 
    
    def get_passengers(self):
        return self.__passengers
    
    def set_passengers(self, passengers):
        self.__passengers = passengers
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_max_speed(self):
        return self.__max_speed
    
    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed
    
    def __str__(self):
        return f"Helicopter {self.__name} can carry {self.__passengers} passengers at a max speed of {self.__max_speed}"
    
    def __repr__(self):
        return f"Helicopter (name={self.__name}, passengers={self.__passengers}, max speed={self.__max_speed})"

def main():
    helicopter1 = Helicopter(4, "Skyline SL-222", 250)
    helicopter2 = Helicopter(5, "Robinson R-22", 300)
    helicopter3 = Helicopter(2, "Enstrom F-28", 220)

    print(helicopter1)
    print(helicopter2)
    print(helicopter3)
    
    helicopter1.set_passengers(5)
    helicopter1.set_name("Skyline SL-222")
    helicopter1.set_max_speed(270)
    
    print("\nUpdated information:")
    print(helicopter1)

if __name__ == "__main__":
    main() 