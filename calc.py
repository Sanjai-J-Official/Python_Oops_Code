class Calc:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2

obj=Calc(2,4)
print(obj.sum())
print(obj.sub())
print(obj.mul())