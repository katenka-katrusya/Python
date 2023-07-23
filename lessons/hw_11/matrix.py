from operations import Matrix

m1 = Matrix([[1, 1, 7, 2, 3],
       [0, 4, 9, 1, 5],
       [4, 0, 1, 5, 3],
       [5, 4, 5, 1, 1]])

m2 = Matrix([[0, 8, 1, 3, 3],
       [9, 4, 0, 1, 4],
       [4, 2, 2, 0, 3],
       [3, 0, 1, 5, 7]])

print("Первая матрица -->>")
m1.show_matrix()

print("Вторая матрица -->>")
m2.show_matrix()

print("Сложение матриц -->>")
plus = m1 + m2
plus.show_matrix()

print("Сравнение матриц -->>")
print(m1.comparison(m2))