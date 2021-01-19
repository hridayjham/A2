## @file complex_adt.py
#  @author 
#  @brief 
#  @date 
import math

class ComplexT: 
    x = 0.0
    y = 0.0
      
    # parameterized constructor 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def real(self):
        return self.x

    def imag(self):
        return self.y

    def get_r(self):
        return math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))

    def get_phi(self):
        if self.x > 0 or self.y != 0:
            return (2 * math.atan(self.y / (self.get_r() + self.x)))
        elif self.x < 0 and self.y == 0:
            return math.pi
        elif self.x == 0 and self.y == 0:
            return None
    
    def equal(self, ComplexNo):
        if self.x == ComplexNo.x and self.y == ComplexNo.y:
            return True
        else:
            return False
    
    def conj(self):
        return ComplexT(self.x, -1 * self.y)

    def add(self, ComplexNo):
        return ComplexT(self.x + ComplexNo.x, self.y + ComplexNo.y)

    def sub(self, ComplexNo):
        return ComplexT(self.x - ComplexNo.x, self.y - ComplexNo.y)

    def mult(self, ComplexNo):
        return ComplexT((self.x * ComplexNo.x - self.y * ComplexNo.y), (self.x * ComplexNo.y + self.y * ComplexNo.x)) 

    def recip(self):
        if self.x == 0 and self.y == 0:
            return None
        else:
            realPart = self.x / (math.pow(self.x, 2) + math.pow(self.y, 2))
            imagPart = -1 * self. y / (math.pow(self.x, 2) + math.pow(self.y, 2))
            return ComplexT(realPart, imagPart)

    def div(self, ComplexNo):
        return self.mult(ComplexNo.recip())
    #def div(self, ComplexNo):
        
    def sqrt(self):
        sign = 0.0
        if self.y < 0:
            sign = -1.0
        elif self.y > 0:
            sign = 1.0
        else:
            sign = 0.0
        realPart = math.sqrt((self.x + self.get_r()) / 2)
        imagPart = sign * math.sqrt(( -self.x + self.get_r()) / 2)
        return ComplexT(realPart, imagPart)

##a = ComplexT(3.0, 3.0)
##b = ComplexT(1.0, -1.0)
##c = a.sqrt()
##print(c.real())
##print(c.imag())