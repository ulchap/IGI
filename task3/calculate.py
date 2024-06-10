import math
import statistics
import matplotlib.pyplot as plt

class TaylorSeries:
    def __init__(self, x, eps, y):
        self.x = x
        self.eps = eps
        self.y = y
        self.sum = 0
        self.component = 0
        self.n = 0
        self.series_values = []

    def get_function_value(self, x):
        return math.cos(x)

    def calculate_series_sum(self):
        while True:
            self.component = ((-1) ** self.n) * (self.x ** (2 * self.n) / math.factorial(2 * self.n))
            self.sum += self.component
            self.series_values.append(self.sum)
            self.n += 1
            if self.n == 501:
                print("500 iterations already done.")
                return self.sum, self.n
            if abs(self.sum - self.y) < self.eps:
                print("Accuracy is achieved.")
                return self.sum, self.n

    def additional_parameters(self):
        mean = statistics.mean(self.series_values)
        median = statistics.median(self.series_values)
        mode = statistics.mode(self.series_values)
        variance = statistics.variance(self.series_values)
        std_deviation = statistics.stdev(self.series_values)

        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)
        print("Variance:", variance)
        print("Standard Deviation:", std_deviation)
