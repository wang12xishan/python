#coding:utf-8
def is_palindrome(n):
    for x in  range(n): 
        return str(n)[x]==str(n)[-x-1:]
output = filter(is_palindrome,range(1,1000))
print (list(output))