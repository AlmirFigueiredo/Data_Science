#Let's define the function as f(x) = 1/x
def f(x):
    return 1/x

def derivative_x(y, x, step_size):
    m = (f(x+step_size) - f(x)) / ((x + step_size) - x)
    return m

slope_at_2 = derivative_x(f, 2, .00001)
print(slope_at_2)


