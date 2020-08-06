import numpy as np
import pandas as pd
import matplotplib.pyplot as plt
# this is a python script, so no need for matplotlib inline


matrix_D = np.random.randn(2, 3)
matrix_C = np.random.randn(3, 8)


final_result = np.matmul(matrix_D, matrix_C)

assert(final_result.shape[0] == matrix_A.shape[0])
print("The shape of the final result is ",final_result.shape)
print("Something really experimental")

# This is a comment
# write another comment