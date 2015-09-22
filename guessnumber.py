#!/usr/bin/env python
#coding:utf-8

import random
i = 0
while i < 4:
    print ('*************')
    num = int(input(('请您输入0到9任一个数：')))
    
    nums = random.randint(0,9)
    
    x = 3 - i
    
    if num == nums :
        print ('运气真好猜对了！')
        break
    elif num > nums:
        print ("猜大了!\n正确答案是：%s\n你还有%s次机会"%(nums,x))
    elif num < nums :
        print ("猜小了!\n正确答案是：%s\n你还有%s次机会"%(nums,x))
    print ('*************')
    i += 1