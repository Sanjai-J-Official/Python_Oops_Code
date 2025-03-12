class Parent:
    def __init__(self,assets1,assets2):
        self.assets1=assets1
        self.assets2=assets2
    def parent_assets(self):
        print(f'Parent assets:{self.assets1},{self.assets2}')
    
class child(Parent):
    def __init__(self, assets1, assets2,assets3):
        self.assets3=assets3
        super().__init__(assets1, assets2) #that used to Assign the assets1 and assets2 becauze you already assign the value
        # so you cannot rewrite code its not necessary
    

    def child_assets(self):
        print(f"Parent as Assets:{self.assets1}")
        print(f"Parent as Assets:{self.assets2}")
        print(f"Child Assets:{self.assets3}")

p_ass=Parent('Land','House')
p_ass.parent_assets()
ass=child(p_ass.assets1,p_ass.assets2,'BMW Car')
ass.child_assets()

