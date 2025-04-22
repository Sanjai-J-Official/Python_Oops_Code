class student:
    college_name='Dhanalakshmi srinivasan college of engineering'
    college_location='Coimbatore'
    def __init__(self):
        self.name='jai'

    def stu(self):
        print(obj.college_name, id(obj.college_name))
        student.college_name='AJK College of Engineering'
        print(student.college_name,id(student.college_name))
        obj.college_name='Anna university'
        print(self.college_name,id(self.college_name))


obj=student()
obj.stu()
   

"""
   
   The member of the object 
   the modification with respect to obj method of obj members will be applicable for all the obj 
   which are using in particualr class
   
   
"""