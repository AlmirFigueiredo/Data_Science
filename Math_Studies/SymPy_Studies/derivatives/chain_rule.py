from sympy import *
# If a receive these two functions:
# y = x^3 + 8
# z = y^2 - 4
# I can figure out this: z = (x^3 + 8)^2 - 4
# So, it's possible to calculate the derivative of z with respect to x
x,y = symbols('x y')
def z(x):
    return (x**3 + 8)**2 - 4

dz_dx = diff(z(x), x)
print(dz_dx)

#Application of chain rule, the chain rule says it: dz/dx = dz/dy x dy/dx
_y = x**3 + 8
dy_dx = diff(_y)

z = y**2 - 4
dz_dy = diff(z)
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
print(dz_dx_chain)


