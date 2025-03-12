class Parent:
    def __init__(self,assets1,assets2):
        self.assets1=assets1
        self.assets2=assets2
    
class child(Parent):
    def __init__(self, assets1, assets2,assets3):
        self.assets3=assets3
        super().__init__(assets1, assets2) #that used to Assign the assets1 and assets2 becauze you already assign the value
        # so you cannot rewrite code its not necessary
    

    def retrive_assets(self):
        print(self.assets1)
        print(self.assets2)
        print(self.assets3)

ass=child('BMW Car','Home','Land')
ass.retrive_assets()