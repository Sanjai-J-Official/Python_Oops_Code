class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print('Move...!')

class car(vehicle):
    pass
class boat(vehicle):
    def move(self):
        print("Sail...!")

class flight(vehicle):
    def move(self):
        print('Fly...!')

car1=car('ford',2324)
boat1=boat('Blackperl',2020)
flight1=flight('Airindia',2025)

for i in (car1,boat1,flight1):
    print(i.brand)
    print(i.model)
    i.move() 
    