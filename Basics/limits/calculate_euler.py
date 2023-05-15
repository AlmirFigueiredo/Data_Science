from sympy import *

#Let's calculate euler's number
def f(n):
    return (1 + (1/n))**n

n = symbols('n')
result = limit(f(n), n, oo)
print(result.evalf()) #Because when you print the result without the evalf, it prints E (means euler's number)

