import os 

if os.path.exists(r"C:\Users\Ajith\Desktop\python code\Oops_Concept\demofile.txt"):
    os.remove(r"C:\Users\Ajith\Desktop\python code\Oops_Concept\demofile.txt")
else:
    print("file doesn't exists")


    