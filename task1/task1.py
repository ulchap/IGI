# Program Purpose: Task 1.
# Lab Work Number: 3
# Program Name: Convergence of Numerical Series
# Version: 1.0
# Developer: Pobortseva Ulyana

import input as inpt
from output import invitation, print_table
import calc as calc


invitation()    #Print invitation at the beginning of the program.  

while True:
    x=inpt.input_x(None)        #Input argument x.  
    print("You entered x =",x)

    eps=inpt.input_accuracy(None)   #Input argument epsilon.  
    print("You entered epsilon =",eps)

    y=calc.get_function_value(x)    #Calculations.
    sum,n=calc.get_series_sum(x,eps,y)

    print_table(x,n,sum,y,eps)  #Output the result table.  
    
    if not inpt.continue_or_exit(): #Ask user if he wants to finish the program or continue.  
        break
        