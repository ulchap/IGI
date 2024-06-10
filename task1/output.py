import math

def invitation():
    """Outputs the invitation to start the program at the beginning."""
    print("This program is designed to calculate the amount of iterations"
          " required for a numerical series to converge.")
    

def print_table(x, n, sum, y, eps):
    """Outputs the result of the program in a table."""
    amount_of_digits = int(abs(math.log10(eps)))
    print("{:^15} | {:^15} | {:^20} | {:^20} | {:^20}"
          .format("x", "n", "F(x)", "Math F(x)", "eps"))
    print("-" * 99)
    print("{:^15} | {:^15d} | {:^20.{}f} | {:^20.{}f} | {:.{}f}"
          .format(x, n, sum, amount_of_digits, y, amount_of_digits, eps, amount_of_digits))
