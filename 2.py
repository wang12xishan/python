#coding:utf-8

sum = 0
for x in range(1,11):
    sum = sum + x
print (sum)

""" sum= reduce(lambda x,y:x+y,[a for a in range(11)])"""