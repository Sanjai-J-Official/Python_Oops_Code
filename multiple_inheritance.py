class P1:
    a=10
    b=20
    def __init__(self):
        self.aa=100
        self.bb=200
class P2:
    c=30
    d=40
    def __init__(self):
        self.cc=300
        self.dd=400
class C1(P2,P1):
    child_name='Sanjai'
obj1=C1()
print(obj1.__dict__)

print(obj1.c)
# print(obj1.cc)
print()
print(obj1.child_name)