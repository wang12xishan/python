#coding:utf-8
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    X=[]
    for key in t:
        X.append(key)
    return X
L2=sorted(L,key = by_name)
print(L2)