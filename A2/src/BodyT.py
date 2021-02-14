## @file BodyT.py
#  @author
#  @brief
#  @date

from Shape import Shape
import math

def __cm(z, m):
    temp = 0
    for i in range(len(m)):
        temp += z[i]*m[i]
    return temp/sum(m)

def __sum(m):
    temp = 0
    for i in m:
        temp += i
    return temp

def __mmom(x, y, m):
    temp = 0
    for i in range(len(m)):
        temp += m[i]*(math.pow(x[i], 2)+ math.pow(y[i], 2))
    return temp


class BodyT(Shape):
    
    def __init__(self,x, y, m ):
        if ((len(x) ==len(y)) == False) or ((len(y) == len(m)) == False):
            raise ValueError("Lengths of inputs are invalid")
        elif self.sum(m) <= 0 :
            raise ValueError("Invalid input for m")
        else:
            self.cmx = self.cm(x, m)
            self.cmy = self.cm(y, m)
            self.m = self.sum(m)
            self.moment = mmom(x, y, m) - sum(m)*(math.pow(cm(x, m), 2) + math.pow(cm(y, m), 2))
            
            
    def cm_x(self):
        return self.cmx
        
    def cm_y(self):
        return self.cmy
        
    def mass(self):
        return self.m
        
    def m_inert(self):
        return self.moment
