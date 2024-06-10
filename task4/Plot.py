import matplotlib.pyplot as plt
import numpy as np
import Triangle

def plot_triangle(triangle, title):
    # Вычисляем углы треугольника
    angle_a = 2 * np.arcsin(triangle.a / (2 * triangle.R))
    angle_b = 2 * np.arcsin(triangle.b / (2 * triangle.R))
    angle_c = 2 * np.arcsin(triangle.c / (2 * triangle.R))

    # Создаем массив углов
    angles = [0, angle_a, angle_a + angle_b]

    # Вычисляем координаты вершин треугольника на окружности
    x = triangle.R * np.cos(angles)
    y = triangle.R * np.sin(angles)

    # Замыкаем треугольник
    x = np.append(x, x[0])
    y = np.append(y, y[0])

    #Рисуем треугольник
    plt.fill(x, y, color=triangle.get_color())
    plt.axis('equal')
    plt.title(title)
    plt.savefig('triangle.png')
    plt.show()
