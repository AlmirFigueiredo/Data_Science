from sympy import *

x, i, n = symbols('x i n')
def f(x):
    return x**2 + 4
lower, upper = 0, 1
delta_x = ((upper - lower)/n)
x_i = delta_x * i + lower
fx_i = f(x).subs(x, x_i)

rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()
#Approaching the number of rectangles to infinity
area = limit(rectangles, n, oo)
print(area)