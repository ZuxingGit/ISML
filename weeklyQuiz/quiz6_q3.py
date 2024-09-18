# w= (0.25,-0.4), x_i=(2, 1.5), b=1.1, y_i=1

w = (0.25, -0.4)
x = (2, 1.5)
b = 1.1
y = 1

value = y*(w[0]*x[0] + w[1]*x[1] + b)
print(value)
# check if the point is correctly classified
if y*(w[0]*x[0] + w[1]*x[1] + b) > 0:
    print('Correctly classified')
else:
    print('Incorrectly classified')