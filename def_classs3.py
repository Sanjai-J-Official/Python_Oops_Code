def maths(num1,num2,operator):
    if operator=='+':
        return f'the Sum of :{num1+num2}'
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    elif operator=='//':
        return num1//num2
print(maths(int(input("Enter num 1:")),int(input("Enter num 2:")),input("Enter operator:")))