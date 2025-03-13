class car:
    def __init__(self ,brand ,model):
        self.brand=brand
        self.model=model
    def move(self):
        print('Car Start...!')

class boat:    
    def __init__(self ,brand ,model):
        self.brand=brand
        self.model=model
    def move(self):
        print('boat Start...!')

class Bike:   
    def __init__(self ,brand ,model):
        self.brand=brand
        self.model=model
    def move(self):
        print('bike Start...!')

car1=car("BMW",234)
boat1=boat("Titanic",1995)
bike1=Bike("Pulsar",454)

for i in (car1,boat1,bike1):
    i.move()