#coding:utf-8
def triangles():
    a = [1]
    while True:
        yield(a)
        a = [a[i-1]+a[i] for i in range(len(a))]
        a[0] = 1
        a.append(1)
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break