# w=(X^T X)^−1 X^Ty to find the optimal weights
# with data points as parameters
import numpy as np

def linear_regression(X, y):
    # w=(X^T X)^−1 X^Ty
    w = np.linalg.inv(X.T @ X) @ X.T @ y
    return w

# data points:(3,13),(6,8),(7,11),(8,2),(11,6)
X = np.array([[1,3],[1,6],[1,7],[1,8],[1,11]])
y = np.array([13,8,11,2,6])
w = linear_regression(X, y)
print(w)