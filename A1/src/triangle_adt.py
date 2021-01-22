## @file triangle_adt.py
#  @author Hriday Jham
#  @brief Contains the TriangleT type to represent all three
#  sides of a triangle
#  @date 01/21/2021

import math
from enum import Enum, auto

## @brief TriangleT is a class that implements an ADT for the
#  mathematical concept of triangles.
#  @details the ADT contains the three sides of a triangle

class TriangleT:

    ## @brief constructor method for TriangleT
    #  @param x a float indicating first side of the Triangle
    #  @param y a float indicating second side of the Triangle
    #  @param z a float indicating third side of the Triangle

    def __init__(self, x, y, z): 
        self.side1 = x 
        self.side2 = y
        self.side3 = z

    ## @brief get the three sides of the triangle
    #  @return a tuple containing the three sides. 

    def get_sides(self):
        return (self.side1, self.side2, self.side3)

    ## @brief check if two triangles are equal
    #  @details two triangles are equal if their sides are equal
    #  @param new_triangle a TriangleT object to compare with
    #  @return boolean indicating whether two triangles are equal

    def equal(self, new_triangle):
        tuple1 = self.get_sides()
        tuple2 = new_triangle.get_sides()
        if sorted(tuple1) == sorted(tuple2):
            return True
        else :
            return False
    
    ## @brief get the perimeter of the triangle
    #  @details the perimeter of as triangle is the sum of all three sides
    #  @return float indicating the perimeter

    def perim(self):
        return self.side1 + self.side2 + self.side3

    ## @brief get the area of the triangle
    #  @details the area of a triangle is the area it covers
    #  @return float indicating the area
    
    def area(self) :
        s = self.perim() / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    ## @brief checks if the three sides form a valid triangle
    #  @details the sum of any two sides of a triangle should be greater than 
    #  its third side. Also the length of a side cannot be negative or zero.
    #  @return boolean indicating whether the triangle is valid.

    def is_valid(self) :
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            return False
        elif (self.side1 + self.side2 > self.side3) and (self.side1 + self.side3 > self.side2) and (self.side2 + self.side3 > self.side1) :
            return True
        else :
            return False

    ## @brief checks the type of triangle.
    #  @details A triangle is equilateral if all three sides are equal, Isosceles
    #  if two sides are equal, scalene if all three sides have different length, and
    #  right if one angle of the triangle is 90 degrees (pi/2 radian)
    #  @return TriType returning the type of triangle

    def tri_type(self):
        if self.side1 == self.side2 and self.side1 == self.side3:
            return TriType.equilat
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return TriType.isosceles
        else:
            sides_list = sorted(self.get_sides())
            if (pow(sides_list[0], 2) + pow(sides_list[1], 2) == pow(sides_list[2], 2)):
                return TriType.right
            else :
                return TriType.scalene

## @brief TriType contains an enum for the types of triangles.

class TriType(Enum):
    equilat = auto()
    isosceles = auto()
    scalene = auto()
    right = auto()
