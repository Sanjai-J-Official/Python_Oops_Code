class school:
    def __init__(self,name): #instance of this class is Selfss and self is we can chhnage it
        self.name=name 

    def scl_name(self):
        print(f'The School Name:{self.name}')

class clg:   # we can also use name instance in all class but values defends on Object creation
    def __init__(self,name):
        self.name=name

    def clg_name(self):
        print(f"this is college name:{self.name}")

sch1=school('PAAHS SCHOOL')
sch1.scl_name()
clg1=clg('DSCE COllge')
clg1.clg_name()