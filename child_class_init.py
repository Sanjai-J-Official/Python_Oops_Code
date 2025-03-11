class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def printname(self):
        print(f"This is name:{self.name}, Model : {self.model}")

class mini_car(car):
    def __init__(self,name,model):
        car.__init__(self,name,model)

car1=mini_car('BMW','CLA 200')
car1.printname()
