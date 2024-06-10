 
def input_x(x):
    """Returns x value."""
    x = float(input("Enter the value of x:"))
    return x
        

def input_accuracy(eps):
    """Returns epsilon value."""
    while True:
        try:
            eps=float(input("Enter the accuracy:"))
            if(eps<=0):
                raise ValueError("Accuracy must be positive!")
            if(eps>=1):
                raise ValueError("Accuracy must be less than 1!")
            break
        except ValueError as err:
            print(err)
            print("Incorrect input! Try again.")
    return eps


def continue_or_exit():
    """Provides a choice to the user to continue or exit the program."""
    while True:
        choice = input("Would you like to exit (e) or continue (c)? ").strip().lower()
        if choice == 'c':
            return True
        elif choice == 'e':
            return False
        else:
            print("Incorrect input! Please enter 'e' to exit or 'c' to continue.")