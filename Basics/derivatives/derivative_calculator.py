from sympy import *
x = symbols('x')
def f(x):
    return x**2
def dx_f(x):
    return diff(f(x), x)
value = float(input())
slope_at = dx_f(x).subs(x, value)
print(f'{slope_at:.4f}')
