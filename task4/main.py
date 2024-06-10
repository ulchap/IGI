import Triangle
import matplotlib.pyplot as plt
import Plot
import Input

while True:
    # Ввод параметров с клавиатуры
    a, b, c, R = Input.check_triangle_input()
    color = input("Enter the color of the triangle: ")
    title = input("Enter the plot title: ")

    # Создание объекта прямоугольника
    triangle = Triangle.Triangle(a, b, c, R, color)

    # Вывод информации о фигуре
    print(triangle.get_figure_info())
    Triangle.Triangle.print_type()

    # Построение фигуры
    # plt.gca().add_patch(plt.Rectangle((0, 0), width, height, color=color))
    # plt.text(width/2, height/2, "Rectangle", ha='center', va='center')
    Plot.plot_triangle(triangle, title)

    choice = input("Would you like to exit (e) or continue (c)? ").strip().lower()
    if choice == 'c':
        pass
    elif choice == 'e':
        break
    else:
        print("Incorrect input! Please enter 'e' to exit or 'c' to continue.")
        