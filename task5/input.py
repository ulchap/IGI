import random

def input_choice(line):
    """Returns positive integer value."""
    while True:
        try:
            x = int(input(line))
            if(x<=0):
                raise ValueError("Entered number is not positive!")
            break
        except ValueError as err:
            print(err)
            print("Incorrect input! Try again.")
    return x


def input_int():
    """Returns integer value."""
    while True:
        try:
            x = int(input("Enter the integer:"))
            break
        except ValueError:
            print("Incorrect input! Try again.")
    return x


def generate_random_sequence(length):
    """Integer sequence generator."""
    for _ in range(length):
        yield random.randint(-50, 50)
        

def manual_input(length):
    """Provides a manual input of list's elements."""
    lst=[]
    while length!=0:
        elem=input_int()
        lst.append(elem)
        length-=1
    return lst
    
        
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