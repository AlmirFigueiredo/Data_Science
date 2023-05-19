from sympy import *
x, s = symbols('x s')
f = x**3

def slope(f, point):
    slope_f = (f.subs(x, point+s)-f.subs(x, point))/(s)
    return slope_f

point = 2
result = limit(slope(f, point), s, 0)
print(result)

# The limit function works this way: limit({function}, {variable}, {point}). The point means the 'point' the variable is approaching
# I can represent infinity as oo (double o)

