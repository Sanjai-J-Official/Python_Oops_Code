class car:
    def __init__(self,brand):
        self.brand=brand
    def model(self,model):
        self.model=model
        print(f"Car Name:{self.brand} and model:{model}")
    def details(self):
        print(f"Car model : {self.model}")

def car_manufacture(model1):
    #self.model1=model1
    print(f'This Car manufacture {model1}')
car1=car('BMW')
car1.model('CLA 200')
car1.details()
car_manufacture('Mahindra')

