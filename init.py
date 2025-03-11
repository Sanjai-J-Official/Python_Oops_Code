#create class and object

class student_db:
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept

#s1=student_db('sanjai',22,'ai')
s2=student_db('jai',21,'cse')
s1=student_db('jai',21,'cse')
print(s1.name,s1.dept)
print(s2.name,s2.dept)


