## @file complex_adt.py
#  @author Hriday Jham
#  @brief Contains the ComplexT type to represent Complex
#  numbers with their real and imaginary parts
#  @date 02/21/2021
import math

## @brief ComplexT is a class that implements an ADT for the
#  mathematical concept of Complex Numbers
#  @details the ADT contains the real and imaginary parts of 
#  complex number

class ComplexT: 

    ## @brief constructor method for ComplexT
    #  @param x a float indicating the real part of the complex 
    #  number
    #  @param y a float indicating the imaginary part of the
    #  complex number 
    
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    ## @brief get the real part of the complex number
    #  @return a float indicating the real part 

    def real(self):
        return self.x

    ## @brief get the imaginary part of the complex number
    #  @return a float indicating the imaginary part

    def imag(self):
        return self.y

    ## @brief get the absolute value of the complex number
    #  @return a float indicating the absolute value

    def get_r(self):
        return math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))

    ## @brief get the phase of the complex number (in radians)
    #  @return a float indicating the phase

    def get_phi(self):
        if self.x > 0 or self.y != 0:
            return (2 * math.atan(self.y / (self.get_r() + self.x)))
        elif self.x < 0 and self.y == 0:
            return math.pi
        elif self.x == 0 and self.y == 0:
            return None
    
    ## @brief check if two complex numbers are equal
    #  @details two complex numbers are equal if their real and imaginary
    #  parts are equal
    #  @param complex_no a ComplexT object to compare with
    #  @return boolean indicating whether two complex numbers are equal

    def equal(self, complex_no):
        if self.x == complex_no.x and self.y == complex_no.y:
            return True
        else:
            return False
    
    ## @brief get the conjugate of the complex number
    #  @details a conjugate of a number is the reflection of the 
    #  complex number about the real axis
    #  @return a float indicating the conjugate

    def conj(self):
        return ComplexT(self.x, -self.y)

    ## @brief get the sum of two complex numbers
    #  @details the sum of two complex numbers is the sum of both the 
    #  real parts and imaginary parts.
    #  @param complex_no a ComplexT object to add
    #  @return ComplexT object indicating the sum

    def add(self, complex_no):
        return ComplexT(self.x + complex_no.x, self.y + complex_no.y)

    ## @brief get the difference of two complex numbers
    #  @details the difference of two complex numbers is the difference of both the 
    #  real parts and imaginary parts.
    #  @param complex_no a ComplexT object to subtract
    #  @return ComplexT object indicating the difference

    def sub(self, complex_no):
        return ComplexT(self.x - complex_no.x, self.y - complex_no.y)

    ## @brief get the product of two complex numbers
    #  @param complex_no a ComplexT object to multiply
    #  @return ComplexT object indicating the product

    def mult(self, complex_no):
        return ComplexT((self.x * complex_no.x - self.y * complex_no.y), (self.x * complex_no.y + self.y * complex_no.x)) 

    ## @brief get the reciprocal of the complex number
    #  @return ComplexT object indicating the reciprocal

    def recip(self):
        if self.x == 0 and self.y == 0:
            return None
        else:
            real_part = self.x / (math.pow(self.x, 2) + math.pow(self.y, 2))
            imag_part = -1 * self.y / (math.pow(self.x, 2) + math.pow(self.y, 2))
            return ComplexT(real_part, imag_part)

    ## @brief get the quotient of two complex numbers
    #  @param complex_no a ComplexT object to divide
    #  @return ComplexT object indicating the quotient

    def div(self, complex_no):
        if complex_no.equal(ComplexT(0.0, 0.0)):
            return None
        else:
            return self.mult(complex_no.recip())

    ## @brief get the positive square root of two complex numbers
    #  @return a float indicating the root

    def sqrt(self):
        sign = 0.0
        if self.y < 0:
            sign = -1.0
        elif self.y > 0:
            sign = 1.0
        else:
            sign = 1.0
        real_part = math.sqrt((self.x + self.get_r()) / 2)
        imag_part = sign * math.sqrt(( -self.x + self.get_r()) / 2)
        return ComplexT(real_part, imag_part)

