#coding:utf-8
for num in range (1,10000):
    n = 0
    for i in range(1,num) :
        if num%i == 0:
            n += i
    if n == num:
        print(num)    
    
    
    
