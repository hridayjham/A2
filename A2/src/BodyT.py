## @file BodyT.py
#  @author
#  @brief
#  @date

from Shape import Shape
import math

def cm(z, m):
    temp = 0
    for i in range(len(m)):
        temp += z[i]*m[i]
    return temp/sum(m)

def mmom(x, y, m):
    temp = 0
    for i in range(len(m)):
        temp += m[i]*(math.pow(x[i], 2)+ math.pow(y[i], 2))
    return temp

class BodyT(Shape):
    
    def __init__(self,x, y, m ):
        if ((len(x) == len(y) and len (y) == len(m)) == False):
            raise ValueError("Lengths of inputs are invalid")
        elif sum(m) <= 0 :
            raise ValueError("Invalid input for m")
        else:
            self.cmx = cm(x, m)
            self.cmy = cm(y, m)
            self.m = sum(m)
            self.moment = mmom(x, y, m) - sum(m)*(math.pow(cm(x, m), 2) + math.pow(cm(y, m), 2))
            
        


    def __mmom(x, y, m):
        temp = 0
        for i in range(len(m)):
            temp += m[i]*(math.pow(x[i], 2)+ math.pow(y[i], 2))
        return temp

            
    def cm_x(self):
        return self.cmx
        
    def cm_y(self):
        return self.cmy
        
    def mass(self):
        return self.m
        
    def m_inert(self):
        return self.moment
