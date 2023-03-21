"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
 новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""


class Matrix:
    table = []

    def __init__(self, table):
        self.table = table

    def __add__(self, matrix):
        m_1 = self.table
        m_2 = matrix.table

        if len(m_1) > len(m_2):
            t = m_2
            m_2 = m_1
            m_1 = t
        m_3 = []
        for i in range(len(m_1)):
            line = []
            for j in range(len(m_1[i])):
                line.append(m_1[i][j] + m_2[i][j])
            m_3.append(line)

        for value in m_2[(len(m_1) - len(m_2)):len(m_2)]:
            m_3.append(value)
        return Matrix(m_3)

    def __str__(self):
        to_print_str = ''
        for line in self.table:
            for value in line:
                to_print_str = to_print_str + str(value) + ' '
            to_print_str = to_print_str + '\n'
        return to_print_str


# input
m_list_1 = [[1, 2, 3, 4], [1, 2, 3, 4]]
m_list_2 = [[2, 3, 4, 5], [6, 7, 8, 9], [6, 7, 8, 59], [1, 2, 1, 19]]
# create matrix
matrix_1 = Matrix(m_list_1)  # Create object matrix_1
matrix_2 = Matrix(m_list_2)  # Create object matrix_2
# add matrix
matrix_3 = matrix_1 + matrix_2  # matrix_1 object + matrix_2 object = new matrix_3 object
print(matrix_3)