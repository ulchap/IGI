 
def check_triangle_input():
    while True:
        try:
            a = float(input("Enter the sides of triangle: "))
            b = float(input())
            c = float(input())
            R = float(input("Enter the radius: "))
            if a <= 0 or b <= 0 or c <= 0 or R <= 0:
                raise ValueError("Data must be positive!")
            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError("Incorrect data for triangle")
            break
        except ValueError as err:
            print(err)
            print("Incorrect input! Try again.")
    return a, b, c, R