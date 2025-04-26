class person:

    def __init__(self):
        self.name='Dhoni'
        self.age=43
        self.address='jarkhand'
        self.love=2
        self.wife=1
        self.child=1
    def income(self):
        self.salary=15000000
        self.team=100000
        print(self.team)
    def lis(self):
        pass
class Team(person):
    def __init__(self):
        self.team_name='RCB'
        self.team_members=25
    def team_income(self):
      
        self.team_incomes=100000000
    #@staticmethod
    def print_all(self):
        super().__init__()
        super().income()
         
        lis=[self.name,self.age,self.love,self.address,self.child,self.salary ]
         
        for i in lis:
            
            print(f"this: {i}")
        
obj=Team()
obj.print_all()
        


