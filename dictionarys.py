#coding:utf-8
"""[x+'='+y for x,y in d.items()]
[x+'=' for x in d.keys()]
[x+'=' for x in d.values()]
[x+'=' for x in d.values()]
d.lower"""
L = ['Hello',"World",18,'IBM','Apple']
l1 = [x for x in L if isinstance(x,str)]
l2 = [x.lower() for x in L if isinstance(x,str)]