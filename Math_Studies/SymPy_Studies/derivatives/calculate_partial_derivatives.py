from sympy import *
from sympy.plotting import plot3d

#Let's use the function: f(x) = 2x^3 + 3y^3
def f(x, y):
    return 2*x**3 + 3*y**3

x,y = symbols('x y')
dx_f = diff(f(x, y), x)
dy_f = diff(f(x, y), y)

print(dx_f)
print(dy_f)
plot3d(f(x, y))