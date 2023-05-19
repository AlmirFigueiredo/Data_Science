from sympy import *

x = symbols('x')
def f(x):
    return x**2 + 4
#Calculate the area between x = 0 and x = 1
area = integrate(f(x), (x, 0, 1))
print(area)