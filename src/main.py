#!/usr/bin/env python

import ctypes as C
math = C.CDLL('./libMiLibreria.so')
print math.add_int(3, 4)
 
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
print math.add_float(3, 4)

tres = C.c_int(3)
cuatro = C.c_int(4)
res = C.c_int()
math.add_int_ref(C.byref(tres), C.byref(cuatro), C.byref(res))
print res.value

tres = C.c_float(3)
cuatro = C.c_float(4)
res = C.c_float()
math.add_float_ref(C.byref(tres), C.byref(cuatro), C.byref(res))
print res.value

in1 = (C.c_int * 3) (1, 2, -5)
in2 = (C.c_int * 3) (-1, 3, 3)
out = (C.c_int * 3) (0, 0, 0)

math.add_int_array(C.byref(in1), C.byref(in2), C.byref(out), 3)
print out[1]

fl1 = (C.c_float * 3) (1, 2, -5)
fl2 = (C.c_float * 3) (-1, 3, 3)
math.dot_product.restype = C.c_float

print math.dot_product(C.byref(fl1), C.byref(fl2), 3)
 