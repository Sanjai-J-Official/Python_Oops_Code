class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def __str__ (self):
        return f'This is car name:{self.name} and model {self.model}'

car1=car('BMW',2000)
print(car1)