## @file BodyT.py
#  @author Hriday Jham
#  @brief Contains the BodyT type to represent the object body
#  @date 02/16/2021

from Shape import Shape
from math import pow

## @brief BodyT is used to represent the Body of an object.


class BodyT(Shape):
    ## @brief constructor for class BodyT. BodyT is a set of shapes
    #  @param three sequences of real numbers
    def __init__(self, x, y, m):
        if not (len(x) == len(y) and len(y) == len(m)):
            raise ValueError("Lengths of inputs are invalid")
        else:
            for i in m:
                if i <= 0:
                    raise ValueError("m values cannot be 0 or negative")
            self.cmx = self.__cm(x, m)
            self.cmy = self.__cm(y, m)
            self.m = sum(m)
            self.moment = self.__mmom(x, y, m)
            self.moment -= sum(m) * (pow(self.__cm(x, m), 2) + pow(self.__cm(y, m), 2))

    ## @brief used to calculate centre of mass
    #  @param two sequences of real numbers
    #  @return Real number denoting centre of mass

    def __cm(self, z, m):
        temp = 0
        for i in range(len(m)):
            temp += z[i] * m[i]
        return temp / sum(m)

    ## @brief used to calculate moment of inertia
    #  @param three sequences of real numbers
    #  @return Real number used to calculate moment of inertia
    def __mmom(self, x, y, m):
        temp = 0
        for i in range(len(m)):
            temp += m[i] * (pow(x[i], 2) + pow(y[i], 2))
        return temp

    ## @brief return the centre of mass along x axis
    #  @return Real number denoting centre of mass along x axis

    def cm_x(self):
        return self.cmx

    ## @brief return the centre of mass along y axis
    #  @return Real number denoting centre of mass along y axis
    def cm_y(self):
        return self.cmy

    ## @brief return the mass of the Body
    #  @return real number denoting the mass of the body
    def mass(self):
        return self.m

    ## @brief return the moment of inertia of the Body
    #  @return real number denoting the moment of inertia of the body
    def m_inert(self):
        return self.moment
