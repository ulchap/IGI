import random

def input_int():
    """Returns integer value."""
    while True:
        try:
            x = int(input("Enter the number:"))
            break
        except ValueError:
            print("Incorrect input! Try again.")
    return x

def generate_random_sequence():
    """Integer sequence generator."""
    while True:
        yield random.randint(0, 50)


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