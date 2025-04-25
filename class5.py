class A:
    a=10
    b=20

    def __init__(selff):
        selff.p=230
    @classmethod
    def display(self):
        self.a=100
        print(self.a)
        print(selff.p)

obj=A()

A.a=200
print(A.a)
print(obj.a)
