#coding:utf-8
s="ceshi"
name = input("name:")
height = float(input('height:'))
weight = float(input("weight:"))
bmi = weight/height**2
print ("name:%s BMI:%d"%(name,bmi),s)
print (name,bmi,s)
if bmi < 18.5 :
    print("you are too light")
elif bmi < 25 :
    print ("your are normal weight")
elif bmi < 28 :
    print  ("your are fat")
elif bmi < 32 :
    print (" your are too fat")
else:
    print ("you are vrey fat") 