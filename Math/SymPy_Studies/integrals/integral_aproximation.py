#Let's consider that my function is f(x) = x**2 + 4
def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0
    for i in range(1, n + 1):
        midpoint = 0.5*(2*a + delta_x * (2*i - 1))
        total_sum += f(midpoint)
    return total_sum * delta_x

def my_function(x):
    return x**2 + 4

area = approximate_integral(0,1,100,my_function)
print(f'Using 100 rectangles: {area}')

#If I put more rectangles, decreasing the width of each one, I get more precision:
#Instead of 100 rectangles, let's try using 100.000:
area = approximate_integral(0,1,100000,my_function)
print(f'Using 100.000 rectangles: {area}')
