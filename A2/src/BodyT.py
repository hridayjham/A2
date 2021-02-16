## @file BodyT.py
#  @author
#  @brief
#  @date

from Shape import Shape
import math


class BodyT(Shape):
    
    def __init__(self,x, y, m ):
        if ((len(x) == len(y) and len (y) == len(m)) == False):
            raise ValueError("Lengths of inputs are invalid")
        else:
            for i in m:
                if i <= 0:
                    raise ValueError("m values cannot be 0 or negative")
            self.cmx = self.__cm(x, m)
            self.cmy = self.__cm(y, m)
            self.m = sum(m)
            self.moment = self.__mmom(x, y, m) - sum(m)*(math.pow(self.__cm(x, m), 2) + math.pow(self.__cm(y, m), 2))
            
    def __cm(self, z, m):
        temp = 0
        for i in range(len(m)):
            temp += z[i]*m[i]
        return temp/sum(m)   
    
    def __mmom(self, x, y, m):
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
