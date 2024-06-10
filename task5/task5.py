import matrix

n = int(input("Enter n: "))
m = int(input("Enter m: "))

A = matrix.Matrix(n, m)
mean = A.middle_value()
count = A.count_elems_more_middle_value()
std_deviation_formula = A.calculate_standard_deviation()
std_deviation_builtin = A.sko_standart()

print("Матрица A:")
for element in A.A.flat:
    print(element)
print("Cреднее значение:", mean)
print("Количество элементов матрицы, превосходящих среднее значение:", count)
print("Стандартное отклонение (через встроенную функцию):", std_deviation_builtin)
print("Стандартное отклонение (через формулу):", std_deviation_formula)