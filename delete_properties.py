class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
car1=car('BMW','1,22,00,000')
print(car1.name)
del car1.name    #we can delete properties 
car1.name='Thar' # and asign the value or change the value after delete
print(car1.name)

del car1        #we can also delete the object 
print(car1.name)  # output // car1 is not defined
 
