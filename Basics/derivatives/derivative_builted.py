from sympy import *

def f(x):
    return 1/x

x = symbols('x')
dx_y = diff(f(x))
print(dx_y)