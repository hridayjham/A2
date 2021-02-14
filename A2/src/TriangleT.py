## @file TriangleT.py
#  @author
#  @brief
#  @date

from Shape import Shape

class TriangleT(Shape):
    
    def __init__(self, x, y, s, m):
        if s > 0 and m > 0:
            self.x = x
            self.y = y
            self.s = s
            self.m = m
        else:
            raise ValueError("Invalid input for TriangleT")
        
    def cm_x(self):
        return self.x
    
    def cm_y(self):
        return self.y
    
    def mass(self):
        return self.m
    
    def m_inert(self):
        return self.m*self.s*self.s/12
    
