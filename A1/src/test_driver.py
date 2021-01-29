## @file test_driver.py
#  @author Hriday Jham
#  @brief File containing tests for all the functions implemented
#  in ComplexT and TriangleT 
#  @date 01/21/2020

import math
from complex_adt import ComplexT
from triangle_adt import TriangleT, TriType

real_test = True
imag_test = True
get_r_test = True
get_phi_test = True
complex_equal_test = True
conj_test = True
add_test = True
sub_test = True
mult_test = True
recip_test = True
div_test = True
sqrt_test = True
get_sides_test = True
tri_equal_test = True
perim_test = True
area_test = True
is_valid_test = True
tri_type_test = True


print("ComplexT function tests:")

a = ComplexT(1.0, 2.0)
c = a.real()
if c != 1:
    real_test = False

a = ComplexT(-1.0, 2.0)
c = a.real()
if c != -1:
    real_test = False

a = ComplexT(0.0, 0.0)
c = a.real()
if c != 0:
    real_test = False

if real_test == True:
    print("real test passes")
else :
    print("real test FAILS")
#

a = ComplexT(1.0, 2.0)
c = a.imag()
if c != 2:
    imag_test = False

a = ComplexT(-1.0, -2.0)
c = a.imag()
if c != -2:
    imag_test = False

a = ComplexT(0.0, 0.0)
c = a.imag()
if c != 0:
    imag_test = False

if imag_test == True:
    print("imag test passes")
else:
    print("real test FAILS")

a = ComplexT(1.0, 2.0)
c = a.get_r()
if c != math.sqrt(5):
    get_r_test = False

a = ComplexT(-1.0, -2.0)
c = a.get_r()
if c != math.sqrt(5):
    get_r_test = False

a = ComplexT(0.0, 0.0)
c = a.get_r()
if c != 0:
    get_r_test = False

if get_r_test == True:
    print("get_r test passes")
else:
    print("get_r test FAILS")

a = ComplexT(5.0, -3.0)
c = a.get_phi()
if c != -0.5404195002705842:
    get_phi_test = False

a = ComplexT(-3.0, 0.0)
c = a.get_phi()
if c != math.pi:
    get_phi_test = False

#a = ComplexT(0.0, 0.0)
#c = a.get_phi()
if c != None:
    get_phi_test = False

#if get_phi_test == True:
#    print("get_phi test passes")
#else:
#    print("get_phi test FAILS")

a = ComplexT(-3.0, 0.0)
b = ComplexT(-3.0, 0.0)
c = a.equal(b)
if c == False:
    complex_equal_test = False

a = ComplexT(0.0, 0.0)
b = ComplexT(1.0, 3.0)
c = a.equal(b)
if c != False:
    complex_equal_test = False

if complex_equal_test == True:
    print("equal test passes")
else:
    print("equal test FAILS")

a = ComplexT(5.0, -3.0)
c = a.conj()
if c.equal(ComplexT(5.0, 3.0)) == False:
    conj_test = False

a = ComplexT(-3.0, 0.0)
c = a.conj()
if c.equal(ComplexT(-3.0, 0.0)) == False:
    conj_test = False

a = ComplexT(1.0, 1.0)
c = a.conj()
if c.equal(ComplexT(1.0, -1.0)) == False:
    conj_test = False

if conj_test == True:
    print("conj test passes")
else:
    print("conj test FAILS")

a = ComplexT(5.0, -3.0)
b = ComplexT(-3.5, 4.5)
c = a.add(b)
if c.equal(ComplexT(1.5, 1.5)) == False:
    add_test = False

a = ComplexT(-3.0, 0.0)
b = ComplexT(-3.0, 45.0)
c = a.add(b)
if c.equal(ComplexT(-6.0, 45.0)) == False:
    add_test = False

a = ComplexT(1.0, 1.0)
b = ComplexT(-1.0, -1.0)
c = a.add(b)
if c.equal(ComplexT(0.0, 0.0)) == False:
    add_test = False

if add_test == True:
    print("add test passes")
else:
    print("add test FAILS")

a = ComplexT(5.0, -3.0)
b = ComplexT(-3.5, 4.5)
c = a.sub(b)
if c.equal(ComplexT(8.5, -7.5)) == False:
    sub_test = False

a = ComplexT(-3.0, 0.0)
b = ComplexT(-3.0, 45.0)
c = a.sub(b)
if c.equal(ComplexT(0.0, -45.0)) == False:
    sub_test = False

a = ComplexT(1.0, 1.0)
b = ComplexT(-1.0, -1.0)
c = a.sub(b)
if c.equal(ComplexT(2.0, 2.0)) == False:
    sub_test = False

if sub_test == True:
    print("sub test passes")
else:
    print("sub test FAILS")

a = ComplexT(5.0, -3.0)
b = ComplexT(-3.5, 4.5)
c = a.mult(b)
if c.equal(ComplexT(-4.0, 33.0)) == False:
    mult_test = False

a = ComplexT(-3.0, 0.0)
b = ComplexT(-3.0, 45.0)
c = a.mult(b)
if c.equal(ComplexT(9.0, -135.0)) == False:
    mult_test = False

a = ComplexT(1.0, 1.0)
b = ComplexT(-1.0, -1.0)
c = a.mult(b)
if c.equal(ComplexT(0.0, -2.0)) == False:
    mult_test = False

if mult_test == True:
    print("mult test passes")
else:
    print("mult test FAILS")

a = ComplexT(5.0, -3.0)
c = a.recip()
if c.equal(ComplexT(5/34, 3/34)) == False:
    recip_test = False

a = ComplexT(-3.0, 0.0)
c = a.recip()
if c.equal(ComplexT(-1/3, 0.0)) == False:
    recip_test = False

a = ComplexT(1.0, 1.0)
c = a.recip()
if c.equal(ComplexT(1/2, -1/2)) == False:
    recip_test = False

if recip_test == True:
    print("recip test passes")
else:
    print("recip test FAILS")

a = ComplexT(5.0, -3.0)
b = ComplexT(-3.5, 4.5)
c = a.div(b)
if c.equal(ComplexT(-0.953846153846154, -0.3692307692307692)) == False:
    div_test = False

a = ComplexT(0.0, 0.0)
b = ComplexT(-3.0, 45.0)
c = a.div(b)
if c.equal(ComplexT(0.0, 0.0)) == False:
    div_test = False

a = ComplexT(1.0, 1.0)
b = ComplexT(0.0, 0.0)
c = a.div(b)
if c != None:
    div_test = False

if div_test == True:
    print("div test passes")
else:
    print("div test FAILS")

a = ComplexT(5.0, -3.0)
c = a.sqrt()
if c.equal(ComplexT(2.3271175190399496, -0.644574237324647)) == False:
    sqrt_test = False
    print("1")

a = ComplexT(-3.0, 0.0)
c = a.sqrt()
if c.equal(ComplexT(0.0, 1.7320508075688772)) == False:
    sqrt_test = False
    print("2")

a = ComplexT(1.0, 1.0)
c = a.sqrt()
if c.equal(ComplexT(1.09868411346781, 0.4550898605622274)) == False:
    sqrt_test = False
    print("3")

if sqrt_test == True:
    print("sqrt test passes")
else:
    print("sqrt test FAILS")

print("")
print("TriangleT tests:")

a = TriangleT(4, 5, 6)
c = a.get_sides()
if c != (4, 5, 6):
    get_sides_test = False

a = TriangleT(3,5, 6)
c = a.get_sides()
if c != (3, 5, 6):
    get_sides_test = False

if get_sides_test == True:
    print("get_sides test passes")
else:
    print("get_sides test FAILS")

a = TriangleT(4, 5, 6)
b = TriangleT(6, 4, 5)
c = a.equal(b)
if c != True:
    tri_equal_test = False

a = TriangleT(3,5, 6)
b = TriangleT(3,5,7)
c = a.equal(b)
if c != False:
    tri_equal_test = False

if tri_equal_test == True:
    print("equal test passes")
else:
    print("equal test FAILS")

a = TriangleT(4, 5, 6)
c = a.perim()
if c != 15:
    perim_test = False

a = TriangleT(3,5, 6)
c = a.perim()
if c != 14:
    perim_test = False

if perim_test == True:
    print("perim test passes")
else:
    print("perim test FAILS")

a = TriangleT(4, 5, 6)
c = a.area()
if c != 9.921567416492215:
    area_test = False

a = TriangleT(3,5, 6)
c = a.area()
if c != 7.483314773547883:
    area_test = False

if area_test == True:
    print("area test passes")
else:
    print("area test FAILS")

a = TriangleT(0, 3, 4)
c = a.is_valid()
if c == True:
    is_valid_test = False

a = TriangleT(1, 2, 3)
c = a.is_valid()
if c == True:
    is_valid_test = False

a = TriangleT(4, 5, 6)
c = a.is_valid()
if c == False:
    is_valid_test = False

if is_valid_test == True:
    print("is_valid test passes")
else:
    print("is_valid test FAILS")

a = TriangleT(1, 1, 1)
c = a.tri_type()
if c != TriType.equilat:
    tri_type_test = False

a = TriangleT(3, 2, 3)
c = a.tri_type()
if c != TriType.isosceles:
    tri_type_test = False

a = TriangleT(3, 4, 5)
c = a.tri_type()
if c != TriType.right:
    tri_type_test = False

a = TriangleT(3, 5, 7)
c = a.tri_type()
if c != TriType.scalene:
    tri_type_test = False

if tri_type_test == True:
    print("tri_type test passes")
else:
    print("tri_type test FAILS")