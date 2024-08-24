#  calculate SVM primal form parameters from dual form solution
import numpy as np

x = np.array([[1, 2], [-1, 2], [-1, -2], [3, 1]])
y = np.array([-1, -1, 1, 1])
α = np.array([5/16, 0.0, 1/16, 1/4])
C = 5/16
ξ = 6/8
# the rest of slack variables are zero.

# Calculate weights w1 and w2 from dual solution from the above given data
w = np.dot(α*y, x)
print(w)