#coding:utf-8
def add(x,y,f):
    return f(x)+f(y)
r=add(1,-3,abs)
print(r)