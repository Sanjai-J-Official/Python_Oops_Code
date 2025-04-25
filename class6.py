class A:  
    a=37
    num1=200
    def __init__(self):
        self.b=20
    @classmethod
    def change(cls):
        cls.b=30 #add 
        cls.a=40 #over write
        num2=500 #can't store 
        print(num2)
    @staticmethod 
    def smethod ():
        a=100         
obj=A()
print(obj.a)
print("------------------------------")
obj.smethod()
print(A.__dict__)
print("-----------------------------------")
obj.change()
print(A.__dict__)
