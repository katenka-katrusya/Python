class Matrix:

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def show_matrix(self):
        for i in self.matrix:
            print(i)

    def comparison(self, other) -> str:
        result = ""
        if self.matrix < other.matrix:
            result = "Вторая матрица больше первой"
        elif self.matrix > other.matrix:
            result = "Первая матрица больше второй"
        else:
            result = "Матрицы равны"
        return result

    def __add__(self, other):
        result = []
        nums = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                nums.append(summa)
                if len(nums) == len(self.matrix[i]):
                    result.append(nums)
                    nums = []
        return Matrix(result)