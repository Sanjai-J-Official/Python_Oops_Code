class p1:
    a=10
    def __init__(self):
        self.aa=100
class p2(p1):
    b=20
class p3(p2):
    c=30
    def __init__(self):
        self.cc=300
        super().__init__()
class p4(p3):
    d=50
obj=p4()
print(type(obj.aa),obj.cc)
"""
Multiple  Level Inheritance:
--------------------

process of invoking properties or attributes or method of multiple parent class 
into multiple child classes is know as multi level inheritans 

"""