class A:
    a=10
    b=20
    def __init__(self):
        self.c=100
class B(A):
    aa=150
    def __init__(self):
        super().__init__()
        self.d=200
        self.e=self.d+self.c
class C(B):
    cc=250
    def __init__(self):
        A.__init__(self)
        
        self.f=400
        self.add=self.c+self.f 
obj=C()
print(obj.add)





 

 


