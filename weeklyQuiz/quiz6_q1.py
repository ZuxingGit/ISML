# given function f(x) =x^{3}+6x^{2}
# In what range of x values of f(x) function is a convex downwards?

import sympy as sp

# Define the variable and function
x = sp.symbols('x')
f = x**3 + 6*x**2

# Compute the first and second derivatives
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)

# Solve for the range where the second derivative is negative
solution = sp.solve(f_double_prime < 0, x)

print(f"First derivative: {f_prime}")
print(f"Second derivative: {f_double_prime}")
print(f"The function is convex downwards for x in the range: {solution}")