fr1=open(r"C:\Users\Ajith\Desktop\python code\Oops_Concept\demofile.txt", "r")
print(fr1.read())
fr1.close()


print("----------------------------------------")

fw1=open(r"C:\Users\Ajith\Desktop\python code\Oops_Concept\demofile.txt", "a")
wr=fw1.write("This is New txt!")
 
#f=open(r"C:\Users\Ajith\Desktop\python code\Oops_Concept\demofile.txt", "w") #rewite the all txt delete the all text then write the txt
#w=f.write("This is  now New txt!")

fr2=open(r"C:\Users\Ajith\Desktop\python code\Oops_Concept\demofile.txt", "r")
print(fr2.read())
fr2.close()
