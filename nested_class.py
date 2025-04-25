class parent:
    father_salary=50000
    car='BMW'
    bike='RE'

class brother:
    brother_salary=60000

class  me:
    child_salary=100000
    total_revenue=parent.father_salary+child_salary+brother.brother_salary
obj=parent()
print(obj.__dict__)
print(brother.__dict__)
print(me.__dict__)
print(me.total_revenue) 



