
def input_string():
    """Returns line."""
    user_input=input("Enter the line: ")
    return user_input

def continue_or_exit():
    """Provides a choice to the user to continue or exit the program."""
    while True:
        choice = input("Would you like to continue (c) or exit (e)? ").strip().lower()
        if choice == 'c':
            return True
        elif choice == 'e':
            return False
        else:
            print("Invalid choice. Please enter 'C' to continue or 'E' to exit.")
            
