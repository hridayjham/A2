## @file test_driver.py
#  @author 
#  @brief 
#  @date 

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

a = ComplexT(0.0, 0.0)
c = a.get_phi()
if c != None:
    get_phi_test = False

if get_phi_test == True:
    print("get_phi test passes")
else:
    print("get_phi test FAILS")

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
    print("Complex equal test passes")
else:
    print("Complex equal test FAILS")

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