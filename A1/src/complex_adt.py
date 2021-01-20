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
    
    def equal(self, complex_no):
        if self.x == complex_no.x and self.y == complex_no.y:
            return True
        else:
            return False
    
    def conj(self):
        return ComplexT(self.x, -1 * self.y)

    def add(self, complex_no):
        return ComplexT(self.x + complex_no.x, self.y + complex_no.y)

    def sub(self, complex_no):
        return ComplexT(self.x - complex_no.x, self.y - complex_no.y)

    def mult(self, complex_no):
        return ComplexT((self.x * complex_no.x - self.y * complex_no.y), (self.x * complex_no.y + self.y * complex_no.x)) 

    def recip(self):
        if self.x == 0 and self.y == 0:
            return None
        else:
            real_part = self.x / (math.pow(self.x, 2) + math.pow(self.y, 2))
            imag_part = -1 * self. y / (math.pow(self.x, 2) + math.pow(self.y, 2))
            return ComplexT(real_part, imag_part)

    def div(self, complex_no):
        return self.mult(complex_no.recip())
        
    def sqrt(self):
        sign = 0.0
        if self.y < 0:
            sign = -1.0
        elif self.y > 0:
            sign = 1.0
        else:
            sign = 0.0
        real_part = math.sqrt((self.x + self.get_r()) / 2)
        imag_part = sign * math.sqrt(( -self.x + self.get_r()) / 2)
        return ComplexT(real_part, imag_part)

a = ComplexT(0.0, 0.0)
b = ComplexT(1.0, -1.0)
c = a.sqrt()
print(c.real())
print(c.imag())