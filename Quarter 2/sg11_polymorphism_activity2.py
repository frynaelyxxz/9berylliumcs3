class Car: 
    def move(self):
        print("The car drives on the road.")
class Boat:
    def move(self):
        print("The boat sails on water.")
class Drone:
    def move(self):
        print("The drone flies in the sky.")
def start_trip(vehicle):
    vehicle.move()
    
c = Car()
b = Boat()
d = Drone()

start_trip(c) 
start_trip(b) 
start_trip(d)