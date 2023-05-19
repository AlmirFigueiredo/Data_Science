from sympy import *
#Let's calculate the limit of the function 1/x
def f(x):
    return 1/x

x = symbols('x')
result = limit(f(x), x, oo)
print(result)
