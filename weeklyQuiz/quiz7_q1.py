# matrix [[2, 3], [10, 8], [5, 3]]
# calculate population covariance between these two columns

import numpy as np

# Define the matrix
matrix = np.array([[2, 3], [10, 8], [5, 3]])

# Calculate the mean of each column
mean_col1 = np.mean(matrix[:, 0])
mean_col2 = np.mean(matrix[:, 1])

# Calculate the difference of each column from its mean
diff_col1 = matrix[:, 0] - mean_col1
diff_col2 = matrix[:, 1] - mean_col2

# Calculate the mean of the product of the differences
covariance = np.mean(diff_col1 * diff_col2)

print(f"Population covariance between the two columns: {covariance}")