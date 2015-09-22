#coding:utf-8
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score= score
    
    def print_score(self):
        print("%s:%s"%(self.__name,self.__score))
    
    def get_name(self):
        return self.__name
    def get_socre(self):
        return self.__score
    def set_score(self,score):
        if 0<= score <= 100:
            self._score = score
        else :
            raise ValueError('bad score')
            
bart = Student("Bart Simpson",100)
bart.set_score(79)
bart.print_score()