# Создайте класс Матрица.
# Добавьте методы для:
# вывода на печать,
# проверку на равенство,
# сложения,
# *умножения матриц

class Matrix:
    
    """Создаём матрицу из списка с вложенными в него списками"""

    def __init__(self, numbers: list[list]) -> None:
        self.number_of_matrix = numbers

    def __str__(self) -> str:
        f_str = ''
        for i in self.number_of_matrix:
            f_str += str(i)[1:-1].replace(',', '') + "\n"
        return f_str

    def __eq__(self, other) -> bool:
        return self.number_of_matrix == other.number_of_matrix

    def __add__(self, other):
        if len(self.number_of_matrix) == len(other.number_of_matrix) \
                and len(self.number_of_matrix[0]) == len(other.number_of_matrix[0]):
            f_list = []
            for i in range(len(self.number_of_matrix)):
                list_sum = []
                for j in range(len(self.number_of_matrix[i])):
                    sum_pos = self.number_of_matrix[i][j] + \
                        other.number_of_matrix[i][j]
                    list_sum.append(sum_pos)
                f_list.append(list_sum)
            return Matrix(f_list)
        else:
            return "Сумма невозможна"

    def __mul__(self, other):
        if len(self.number_of_matrix[0]) == len(other.number_of_matrix):
            f_list = []
            for i in range(len(self.number_of_matrix)):
                sum_list = []
                for k in range(len(other.number_of_matrix[i])):
                    sum_pos = 0
                    for j in range(len(self.number_of_matrix[i])):
                        sum_pos += self.number_of_matrix[i][j] * \
                            other.number_of_matrix[j][k]
                    sum_list.append(sum_pos)
                f_list.append(sum_list)
            return Matrix(f_list)
        else:
            return "Умножение невозможно"


a = Matrix([[1, 2, 3, 4], [2, 1, 3, 4]])
b = Matrix([[5, 6], [7, 8], [6, 7], [8, 9]])
c = Matrix([[3, 4, 5, 6], [7, 8, 9, 1]])

print(a)
print(b)
print(a+b)
print(a+c)
print(a*b)
print(a*c)
