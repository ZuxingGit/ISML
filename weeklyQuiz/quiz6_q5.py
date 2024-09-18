# x = (x1,x2,x3); y=(y1,y2,y3)
# f(x) = (x1x1, x1x2, x1x3, x2x1, x2x2, x2x3, x3x1, x3x2, x3x3)
# kernal fucntion K(x,y)= (<x, y>)^2
# Calculate the inner product of x and y in the transformed 6 dimensional space using Kernel function K(x, y)

def kernel_function(x, y):
    # Compute the inner product in the original space
    inner_product = sum(x_i * y_i for x_i, y_i in zip(x, y))
    
    # Apply the kernel function
    return inner_product ** 2

x = (1, 2, 3)
y = (4, 5, 6)

# transform
f_x = (x[0]*x[0], x[0]*x[1], x[0]*x[2], x[1]*x[0], x[1]*x[1], x[1]*x[2], x[2]*x[0], x[2]*x[1], x[2]*x[2])
f_y = (y[0]*y[0], y[0]*y[1], y[0]*y[2], y[1]*y[0], y[1]*y[1], y[1]*y[2], y[2]*y[0], y[2]*y[1], y[2]*y[2])

result = kernel_function(x, y)
# result = kernel_function(f_x, f_y)
print(f"The inner product in the transformed space is: {result}")