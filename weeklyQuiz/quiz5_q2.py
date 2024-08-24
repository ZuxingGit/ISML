#  calculate SVM primal form parameters from dual form solution
import numpy as np

x = np.array([[1, 2], [-1, 2], [-1, 4], [3, 1]])
y = np.array([-1, -1, 1, 1])
α = np.array([5/16, 0.0, 1/16, 1/4])
C = 5/16
ξ = 6/8
# the rest of slack variables are zero.
w1 = 3/4
w2 = 1
w = np.array([w1, w2])

# Calculate b* from the dual solution using the above data
b = y - np.dot(w, x.T)
print(b)

# Calculate the margin value, which is 1/||w||_2
margin = 1 / np.linalg.norm(w)
print(margin)