'''
Create a class “Vehicle” (Exploring simple classes)
. The class contains one static (class) variable vehicle_terrain = “land”
  (accessible by all instances of the class vehicle)
. Add a constructor to the class. The constructor receives several parameters:
    . number of wheels, number of passengers, max_speed (km/hour)
    . The constructor also defines the attribute speed. To start the speed is
      initialize to zero.
. Create a method called current_speed() that returns the current speed of the
  vehicle
. Create a method called set_speed(speed) that sets the speed of the vehicle.

Once your Class is done, use it to create the following objects:
V01 = vehicle(4,2,100)
V02 = vehicle(6,4,75)

Print the current_speed of both vehicles
Set the speed of vehicle V01 to 90 Set the speed of vehicle V02 to 60
Print the current_speed of both vehicles
Print the value vehicle_terrain for both vehicles
'''
class Vehicle:
    vehicle_terrain = "land"
