price=1700000
def usd(x):
    return x*87
print(f"This book Price:{price*100}")
print(f"This book price as not decimal:{price}")
print(f"this book is price{' expencive'if price>20 else 'budget friendly'}")
print(f"this price has in USD:{usd(price)}")
print(f"formating integer:{price:1f}")
print(f"is it print {price:<5}book")

txt="Hi my name is {1}.and My age of {1}"
print(txt.format("Sanjai",22))
