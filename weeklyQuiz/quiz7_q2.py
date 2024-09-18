# calculate the eigenvalues for this matrix
# [[2, -12], [1, -5]]

import numpy as np

# Define the matrix
matrix = np.array([[2, -12], [1, -5]])

# Calculate the eigenvalues
eigenvalues = np.linalg.eigvals(matrix)

print(f"Eigenvalues for the matrix: {eigenvalues}")