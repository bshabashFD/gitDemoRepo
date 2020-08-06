import numpy as np
import pandas as pd


matrix_A = np.random.randn(2, 4)
matrix_C = np.random.randn(4, 8)


final_result = np.matmul(matrix_A, matrix_B)

assert(final_result.shape[0] == matrix_A.shape[0])
print(final_result.shape)

