class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        sum=self.a+self.b
        print(f'Sum of {self.a} & {self.b}:{sum}')
    def sub(self):
        sub=self.a-self.b
        print(f'Subract of {self.a} & {self.b}:{sub}')
    def mul(self):
        mul=self.a*self.b
        print(f'multiple of {self.a} & {self.b}:{mul}')
    def div(self):
        div=self.a//self.b
        print(f'divided of {self.a} & {self.b}:{div}')

calc=calculator(8,4)
calc.sum()
calc.div()
calc.sub()
calc.mul()
