class Bank:
    def __new__(cls):
        cls.c=49
        return super().__new__(cls)
    def __init__(cls):
        cls.a=10
        
 

    #def __init__(self):
     
     #    print("Step 2: Initializing the object")

# Create an object of the Bank class
bank_obj = Bank()
print(bank_obj.c)

# Output:
# Step 1: Creating the object
# Step 2: Initializing the object
