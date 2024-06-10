import input as inp
import output as out
import task as task

while True:
    length=inp.input_choice("Enter list's length:")
    
    print("Choose how do you want to input list's elements:\n"
          "1. Manually.\n"
          "2. Generated automatically.\n")
    
    while True:
        choice=inp.input_choice("Enter 1 or 2:")
        if choice!=1 and choice!=2:
            print("Incorrect input!Try again.")
        else:
            break
        
    lst=[]
    if choice==1:
        lst=inp.manual_input(length)
        print("You successfully entered the list:")
    elif choice==2:
        random_sequence = inp.generate_random_sequence(length)
        lst = list(random_sequence)
        print("List has been generated:")
    
    out.print_list(lst)
    
    product= task.calculate_product(lst)
    #lst = [0, 2, 3, 0, 4, 5, 6, 0, 0, 7, 8]
    sum = task.find_sum_between_nonzero(lst)
    out.output_value(product,"Product is: ")
    out.output_value(sum,"The sum of elements: ")

    if not inp.continue_or_exit():
        break
