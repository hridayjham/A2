## @file TriangleT.py
#  @author Hriday Jham
#  @brief Contains the TriangleT type to represent Triangles
#  @date 02/16/2021

from Shape import Shape

## @brief TriangleT is used to represent a triangle which is a Shape


class TriangleT(Shape):

    ## @brief constructor for TriangleT denoting a triangle by its x, y, side and mass
    #  @param takes four real numbers to denote x, y, side and mass
    def __init__(self, x, y, s, m):
        if s > 0 and m > 0:
            self.x = x
            self.y = y
            self.s = s
            self.m = m
        else:
            raise ValueError("Invalid input for TriangleT")

    ## @brief returns the centre of mass along x axis of the triangle
    #  @return a real number denoting centre of mass along x axis of the triangle
    def cm_x(self):
        return self.x

    ## @brief returns the centre of mass along y axis of the triangle
    #  @return a real number denoting centre of mass along y axis of the triangle
    def cm_y(self):
        return self.y

    ## @brief returns the mass of the triangle
    #  @return a real number denoting mass of the triangle
    def mass(self):
        return self.m

    ## @brief returns the moment of inertia of the triangle
    #  @return a real number denoting moment of inertia of the triangle
    def m_inert(self):
        return self.m * self.s * self.s / 12
