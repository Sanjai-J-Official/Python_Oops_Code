class A:
    def __init__(self,a,b,c):
        self.a=a 
        self.b=b
        self.c=c 
class B(A):
    def __init__(self,a,b,c,d,e):
        super().__init__(a,b,c)
        self.d=d
        self.e=e
        print("Init:",self.a) 
 
obj=B(10,20,3,4,5)
 
 