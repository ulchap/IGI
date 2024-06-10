import geometric_figure
import Color

class Triangle(geometric_figure.GeometricFigure):
    __figure_name = "Triangle"

    def __init__(self, a, b, c, R, color):
        self.a = a
        self.b = b
        self.c = c
        self.R = R
        self.color = Color.Color(color)

    def calculate_area(self):
        return self.a * self.b * self.c / 4 / self.R
    
    def get_color(self):
        return self.color.color

    def get_figure_info(self):
        return "{0} {1} colored {2} with area {3}".format(self.__figure_name, self.color.color, (self.a, self.b, self.c, self.R), self.calculate_area())
    
    @staticmethod
    def print_type():
        print(Triangle.__figure_name)
