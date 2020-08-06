import numpy as np
import pandas as pd


matrix_A = np.random.randn(5, 5)
matrix_B = np.random.randn(5, 8)
matrix_Z = np.random.randn(3, 3)


final_result = np.matmul(matrix_A, matrix_B)

assert(final_result.shape[0] == matrix_A.shape[0])
print(final_result.shape)

