name="sanjai"
if not type(name) is str:
    raise TypeError("This is Not a string")
elif name[9] is IndexError :
    raise IndexError("Index Error Found")
elif name[3] is KeyError:
    raise KeyError('Enter the Book ')
else:
    print("this is String No occurred any Error")