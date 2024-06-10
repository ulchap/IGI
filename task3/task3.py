import calculate
import math
import matplotlib.pyplot as plt

# Создание экземпляра класса и вызов методов
x = 0.5
eps = 0.001
y = math.cos(x)

taylor_series = calculate.TaylorSeries(x, eps, y)
series_sum, iterations = taylor_series.calculate_series_sum()
print(series_sum, iterations)
taylor_series.additional_parameters()

# Построение графиков
x_values = []
y_taylor_series = []
y_math_function = []

for i in range(100):
    x_values.append(i / 10)
    y_taylor_series.append(taylor_series.get_function_value(x_values[-1]))
    y_math_function.append(math.cos(x_values[-1]))

plt.plot(x_values, y_taylor_series, label='Taylor Series')
plt.plot(x_values, y_math_function, label='math.cos(x)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True)
plt.savefig('chart.png')
plt.show()

