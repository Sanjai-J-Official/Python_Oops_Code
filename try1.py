Book=['Rich Dad Poor Dad', "Automic"]
try:
    print(f"Price of Book:{Book}")
    try:
        for i in Book:
            print(i)
    except:
        print("Book Doest have any value")
    else:
        print("are you buy the Book?")
except:
    print("Can't Open The Book May be it not defined")