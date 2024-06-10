import numpy as np
import math

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.A = np.random.randint(1, 100, (self.n, self.m))

    def array_as_list(self):
        array = []
        for element in self.A.flat:
            array.append(element)
        return array

    def middle_value(self):
        array = self.array_as_list()
        mean_value = np.mean(array)
        return mean_value

    #Посчитать количество элементов матрицы, превосходящих среднее арифметическое значение элементов матрицы.
    def count_elems_more_middle_value(self):
        array = self.array_as_list()
        mean_value = np.mean(array)
        count = np.sum(array > mean_value)
        return count

    # Вычисление стандартного отклонения с помощью встроенной функции std()
    def sko_standart(self):
        array = self.array_as_list()
        std_deviation_builtin = np.std(array)
        return round(std_deviation_builtin, 2)

    # Вычисление стандартного отклонения через программирование формулы
    def calculate_variance(self):
        array = self.array_as_list()
        mean_value = np.mean(array)
        return sum((x - mean_value) ** 2 for x in array) / len(array)

    def calculate_standard_deviation(self):
        variance = self.calculate_variance()
        return round(math.sqrt(variance), 2)