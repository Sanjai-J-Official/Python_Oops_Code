
class student:
    def __init__(self,name='sanjai',age='20',dept_no='AI'):
        self.name=name
        self.age=age
        self.dept_no=dept_no
 #If you give argument in object its return that value ,suppose you cannot give any argument ,its take default
 #value

st1=student()
print(st1.name)

#we can also change value 
#st1.name='hari'
#print(st1.name) // output: hari