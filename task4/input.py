def input_int():
    """Returns integer value."""
    while True:
        try:
            x = int(input("Enter the number from 1 to 3:  "))
            if x!=1 and x!=2 and x!=3:
                raise ValueError("Choice doesn't meet the conditions")
            break
        except ValueError:
            print("Incorrect input! Try again.")
    return x

def continue_or_exit():
    """Provides a choice to the user to continue or exit the program."""
    while True:
        choice = input("Would you like to exit (e) or continue (c)? ").strip().lower()
        if choice == 'c':
            return True
        elif choice == 'e':
            return False
        else:
            print("Invalid choice. Please enter 'e' to exit or 'c' to continue.")
