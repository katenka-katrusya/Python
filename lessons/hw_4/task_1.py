# Напишите функцию для транспонирования матрицы

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

def matrix_transpose(matrix):
    new_matrix = matrix.T
    return new_matrix

print(matrix_transpose(matrix))
