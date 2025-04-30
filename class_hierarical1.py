import random
class RBI:
    def __init__(self):
        self.name=input("Enter the name:")
        self.age=int(input("Enter the Age:"))
        self.aadhar_num=input("Enter the aadhar No:")
        self.pan_num=input("Enter the Pan No:")
        self.cibil_score=random.randint(730,800)
    
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Aadhar No:{self.aadhar_num}")
        print(f"Pan no:{self.pan_num}")
        print(f"Cibil Score:{self.cibil_score}")
       

class HDFC(RBI):
     def display(self):
        super().display()
        print("Welcome to HDFC BANK !!!")
        if 790<=self.cibil_score<=800:
             print("You are elibile for loan")
        else:
            print("You are not elibile for load ,Try another bank")
class SBI(RBI):
    def display(self):
        super().display()
        print("Welcome to SBI BANK !!!")
        if 760<=self.cibil_score<=800:
             print("You are elibile for loan")
        else:
            print("You are not elibile for load ,Try another bank")
class YES(RBI):
    def display(self):
        super().display()
        print("Welcome to YES BANK !!!")
        if 730<=self.cibil_score<=800:
             print("You are elibile for loan")
        else:
            print("You are not elibile for load ")

obj=HDFC()
obj.display()
