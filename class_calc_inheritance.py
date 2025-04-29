class sum:
    def sum(num1,num2):
        print(num1+num2) 
class sub:
    def sub(num1,num2):
        print(abs(num1-num2)) 
class mul:
    def mul(num1,num2):
        print(num1*num2) 
class div:
    def div(num1,num2):
        print(num1/num2) 
class calc(sum,sub,mul,div):
    num1=int(input("Enter the Num 1:"))
    num2=int(input("Enter the Num 2:"))
    operator=input("Enter the Operator:")
    if operator=="+":
        sum.sum(num1,num2)
    elif operator=='-':
        sub.sub(num1,num2)
    elif operator=='*':
        mul.mul(num1,num2)
    elif operator=='/':
        div.div(num1,num2)
    else:
        print('Invaild Operator')    

#obj=calc()


