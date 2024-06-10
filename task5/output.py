def print_list(lst):
    """Outputs the given list"""
    for word in lst: print(word)
    
def output_value(value,line):
    """Outputs task's results."""
    if value==None:
        print("There is nothing to output.")
    else:
        print(line,value)