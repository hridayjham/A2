## @file triangle_adt.py
#  @author 
#  @brief 
#  @date 

import math
from enum import Enum, auto

class TriangleT:
    side1 = 0
    side2 = 0
    side3 = 0

    def __init__(self, x, y, z): 
        self.side1 = x 
        self.side2 = y
        self.side3 = z

    def get_sides(self):
        return (self.side1, self.side2, self.side3)

    def equal(self, new_triangle):
        tuple1 = self.get_sides()
        tuple2 = new_triangle.get_sides()
        if sorted(tuple1) == sorted(tuple2):
            return True
        else :
            return False
    
    def perim(self):
        return self.side1 + self.side2 + self.side3

    def area(self) :
        s = self.perim() / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def is_valid(self) :
        if (self.side1 + self.side2 > self.side3) and (self.side1 + self.side3 > self.side2) and (self.side2 + self.side3 > self.side1) :
            return True
        else :
            return False

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


class TriType(Enum):
    equilat = auto()
    isosceles = auto()
    scalene = auto()
    right = auto()

a = TriangleT(3, 5, 4)
print(a.tri_type())