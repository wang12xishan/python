#coding:utf-8
def pascal(N):
    a = [1]
    n = 0
    while n < N :
        print (a)
        a = [a[i-1]+a[i] for i in range(len(a))]
        a[0]=1
        a.append(1)
        n = n + 1 

pascal (10)
        
