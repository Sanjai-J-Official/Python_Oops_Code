
class person:
    def __init__(self,name,age):
        self.name=name
    def printname(self):
        print(f'This is name:{self.name}')
class Student(person): #we can  access the data from  parent class to child class
    pass
x=Student('python',21) 
x.printname()
