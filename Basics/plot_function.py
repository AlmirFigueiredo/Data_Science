from sympy import *

# If f(x) = 2x - 4.
def f(x):
    return 2*x - 4

x_values = [2, 5, 7, 10]
for x in x_values:
    x = symbols('x')
    y = f(x)
    plot(y)






