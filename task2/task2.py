# Program Purpose: Task 2.
# Lab Work Number: 3
# Program Name: 
# Version: 1.0
# Developer: Pobortseva Ulyana

import input as inp
import operation as op

print("This program expects an integer value seq and returns the sum of odd numbers."
      "The cycle breaks if entered value is 0.")
count=0
while True:
        print("Choose how do you want to input numbers' sequence:\n"
          "1. Manually.\n"
          "2. Generated automatically.\n")
    
        while True:
            print("Enter 1 or 2:")
            choice=inp.input_int()
            if choice!=1 and choice!=2:
                print("Incorrect input! Try again.")
            else:
                break
            
        if choice==1:
            while True:
                term=inp.input_int()   #Input an integer value
                res=op.perform_operation(term) #Get last digit of number
                count+=res
                print("Result:",res)
                if term==0:   #If entered number is 18 break the cycle
                    break
            
        elif choice==2:
            for num in inp.generate_random_sequence():
                print(num)
                res=op.perform_operation(num)
                count+=res
                print("Result:",res)
                if num==0:   #If entered number is 18 break the cycle
                    break
        
        print("Numbers: ",count)
        numbers_sum=0
      
        if not inp.continue_or_exit(): #Ask user if he wants to finish the program or continue.  
            break