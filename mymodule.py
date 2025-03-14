class maths_calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def getting_in(obj,name):
        print('hello boss',name)
    def sum(self):
        print(f"Sum:{self.a+self.b}")

    def sub(self,c):
        d=self.a-self.b+c-c
        print(f"Sub:{d}")
    def mul(self):
        print(f"mul:{self.a*self.b}")
    def div(self):
        print(f"Div:{self.a//self.b}")

def getting(name):
        print("Hello",name)