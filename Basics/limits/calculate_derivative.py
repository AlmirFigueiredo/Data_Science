from sympy import *

x, s = symbols('x s')
f = x**2 + 3*x

def slope_calc(x, s, f):
    return (f.subs(x, x+s)-f)/((x+s) -x)

slope_f = slope_calc(x, s, f)
result = limit(slope_f, s, 0)

print(result)