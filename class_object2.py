class lap:
    def __init__(self ,laptop,price,ram,processor):
        self.laptop=laptop
        self.price=price
        self.ram=ram
        self.processor=processor
#print statement
    def print_statement(self):
        print(f'Laptop :{self.laptop}')
        print(f'Price:{self.price}')         
        print(f'Ram:{self.ram}')
        print(f'Processor:{self.processor}')

lap1=lap('Asus',12500,16,'AMD Ryzen') 
lap1.print_statement()