class A:
    def __init__(self):
        self.name=input("Enter the name:")
    def display(self):
        print("dsiplay name:",self.name)
class B(A):
    def __init__(self):
        super().__init__()
        self.c=200
    def display(self):
        super().display()
        print("Display value:",self.c)
obj=B()
obj.display()
