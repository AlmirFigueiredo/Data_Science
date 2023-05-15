from sympy import *
from sympy.plotting import plot3d
import matplotlib.pyplot as plt 
plt.switch_backend('TkAgg')
#If f(x) = 2x + 3y
def f(x, y):
    return 2*x + 3*y

x,y = symbols('x y')
plot3d(f(x, y))