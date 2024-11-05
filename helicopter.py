class Helicopter:
    def __init__(self, passengers=0, name="", max_speed=0, flight_hours=0):
        self.__passengers = passengers  
        self.__name = name 
        self.__max_speed = max_speed 
        self.__flight_hours = flight_hours  

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

    def get_flight_hours(self):
        return self.__flight_hours

    def set_flight_hours(self, flight_hours):
        self.__flight_hours = flight_hours

    def __str__(self):
        return (f"Helicopter {self.__name} can carry {self.__passengers} passengers at "
                f"a max speed of {self.__max_speed} with {self.__flight_hours} flight hours")

    def __repr__(self):
        return (f"Helicopter (name={self.__name}, passengers={self.__passengers}, "
                f"max speed={self.__max_speed}, flight hours={self.__flight_hours})")

def main():
    helicopter1 = Helicopter(4, "Skyline SL-222", 250, 1500)
    helicopter2 = Helicopter(5, "Robinson R-22", 300, 2000)
    helicopter3 = Helicopter(2, "Enstrom F-28", 220, 1800)

    helicopters = [helicopter1, helicopter2, helicopter3]  

    
    max_flight_hours_helicopter = helicopters[0] 
    for helicopter in helicopters[1:]:
        if helicopter.get_flight_hours() > max_flight_hours_helicopter.get_flight_hours():
            max_flight_hours_helicopter = helicopter
    
    for helicopter in helicopters:
        print(helicopter)

    print(f"\nThe helicopter with the most flight hours is: {max_flight_hours_helicopter}")

if __name__ == "__main__":
    main()