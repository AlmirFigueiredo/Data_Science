from sympy import *
# If a receive these two functions:
# y = x^3 + 8
# z = y^2 - 4
# I can figure out this: z = (x^3 + 8)^2 - 4
# So, it's possible to calculate the derivative of z with respect to x
x = symbols('x')
z = (x**3 + 8)**2 - 4

dz_dx = diff(z, x)
print(dz_dx)



