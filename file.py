f=open(r"C:\Users\Ajith\Desktop\python code\Oops_Concept\demofile.txt", "r")
           
#print(f.read())
#for i in f:
 #   print(i[0])
#print(f.readline()) #it is used to print first 1st line return str
 
print(f.readlines()) #alread 1st lines cannot execute return its return list of all lines 
f.close()