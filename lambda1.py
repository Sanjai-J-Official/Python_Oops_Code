nums=[1,3,4,5,3,6,8,9,3,6,43,4,6,2,5]

stu_name=["sanjai",'jai','python',"opencv","math"]

stu_age=[21,19,23,34]
fil=filter(lambda x: x>=5 and not x<=10 ,nums)
s=sum(nums)

stu_age[0]=99
zipped=zip(stu_name,stu_age)
print(list(fil))
print(s)
 
print(list(zipped))

