'''
Create two new classes Motorcycle and Auto that inherit from Vehicle (in 14_1)
. Add a new attribute to these classes “color” and “brand”
. Create the appropriate constructor for this classes.
. Create an object of type Motorcycle and an object of type Car
. Get the current speed for both objects
. Set the speed of the Motorcycle to 95
. Set the speed of the car to 100
. Get the current speed for both the Motorcycle and the Car
. Print the color and brands of the car and the color of the motorcycle objects
'''
class Vehicle:
    vehicle_terrain = "land"

    def __init__(self, iNumWheels, iNumPassengers, iMaxSpeed, iSpeed = 0):
        self.numWheels = iNumWheels
        self.numPassengers = iNumPassengers
        self.maxSpeed = iMaxSpeed
        self.speed = iSpeed

    @property
    def current_speed(self):
        return self.speed

    @current_speed.setter
    def current_speed(self, iCurrentSpeed):
        self.speed = iCurrentSpeed

class Motorcycle(Vehicle):

    def __init__(self, iNumWheels, iNumPassengers, iMaxSpeed, sColor, sBrand, iSpeed = 0):
        super().__init__(iNumWheels, iNumPassengers, iMaxSpeed, iSpeed)
        self.color = sColor
        self.brand = sBrand

    def __repr__(self):
        return "Motorcycle({}, {}, {}, {}, {}, {})".format(
        self.numWheels, self.numPassengers, self.maxSpeed,
        self.speed, self.color, self.brand
        )

class Auto(Vehicle):
    def __init__(self, iNumWheels, iNumPassengers, iMaxSpeed, sColor, sBrand, iSpeed = 0):
        super().__init__(iNumWheels, iNumPassengers, iMaxSpeed, iSpeed)
        self.color = sColor
        self.brand = sBrand

m1 = Motorcycle(2, 1, 200, 'Black', 'Honda', 95)
car1 = Auto(4, 5, 180, 'Blue', 'BMW', 100)
car1.current_speed = 100
print('{} {}'.format(m1.current_speed, car1.current_speed))
print('"{} {}" and "{} {}"'.format(car1.color, car1.brand, m1.color, m1.brand))
