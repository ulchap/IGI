# Program Purpose: Task 3.
# Lab Work Number: 3
# Program Name: Counter of digits and letters
# Version: 1.0
# Developer: Pobortseva Ulyana

from count import count_digits_and_letters
from output import print_result
import input as inp

while True:
    s=inp.input_string()

    res1,res2=count_digits_and_letters(s)    #Count symbols.      

    print_result(res1,res2)    #Output the result in a table. 
    
    if not inp.continue_or_exit():  #Ask user if he wants to finish the program or continue.  
        break