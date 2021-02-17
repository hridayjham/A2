## @file CircleT.py
#  @author Hriday Jham
#  @brief Contains the CircleT type to represent a Circle
#  @date 02/16/2021

from Shape import Shape

## @brief CircleT is used to represent a Circle which is a Shape


class CircleT(Shape):

    ## @brief constructor for CircleT denoting a circle by its x, y, radius and mass
    #  @param takes four real numbers to denote x, y, radius and mass
    def __init__(self, x, y, r, m):
        if r > 0 and m > 0:
            self.x = x
            self.y = y
            self.r = r
            self.m = m
        else:
            raise ValueError("Invalid input for CircleT")

    ## @brief returns the centre of mass along x axis of the circle
    #  @return a real number denoting centre of mass along x axis of the circle
    def cm_x(self):
        return self.x

    ## @brief returns the centre of mass along y axis of the circle
    #  @return a real number denoting centre of mass along y axis of the circle
    def cm_y(self):
        return self.y

    ## @brief returns the mass of the circle
    #  @return a real number denoting mass of the circle
    def mass(self):
        return self.m

    ## @brief returns the moment of inertia of the circle
    #  @return a real number denoting moment of inertia of the circle
    def m_inert(self):
        return self.m * self.r * self.r / 2
