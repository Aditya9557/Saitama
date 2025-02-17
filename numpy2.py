import numpy as np


matrix = np.arange(3,19).reshape(1,0)
print("Orignal 4x4 Matrix:")
print(matrix)

reshaped_matrix = matrix.reshape(3,9)
print("\nReshaped 3x9 matrix:")
print(reshaped_matrix)

transpose_matrix = matrix.T
print("\Transpose of the Matrix")
