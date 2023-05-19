from sympy import *

x, s = symbols('x s')

def f(x):
    return x**2 + 3*x

def slope_formula(x, s, f):
    return (f.subs(x, x+s)-f)/((x+s) -x)

result = limit(slope_formula(x, s, f), s, 0)

print(result)