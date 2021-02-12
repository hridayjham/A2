## @file CircleT.py
#  @author
#  @brief
#  @date



class CircleT:
    
    def __init__(self, x, y, r, m):
        if r > 0 and m > 0:
            self.x = x
            self.y = y
            self.r = r
            self.m = m
        else:
            raise ValueError("Invalid input for CircleT")
        
    def cm_x(self):
        return self.x

    def cm_y(self):
        return self.y
    
    def mass(self):
        return self.m
    
    def m_inert(self):
        return self.m*self.r*self.r/2
        
    
    
a = CircleT(1,2,5,0)
