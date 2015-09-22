#!/usr/bin/env python
#coding:utf-8

import random

numbers = [random.randint(1,100) for i in range(20)] #以list解析的方式得到随机的list

odd = [x for x in numbers if x%2==0]
even = [x for x in numbers if x%2==1]
print (numbers)
print ("odd:",odd)
print( "even:",even)