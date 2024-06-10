def calculate_product(lst):
    product = 1
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 == 0:
            product *= abs(num)

    return product

def find_sum_between_nonzero(lst):
    # find indexes
    first_nonzero = next((i for i, x in enumerate(lst) if x != 0), None)
    last_nonzero = next((i for i, x in enumerate(lst[::-1]) if x != 0), None)
    if lst.count(0) == 0:
        return sum(lst)
    
    if first_nonzero is None or last_nonzero is None:
        return 0
    
    last_nonzero = len(lst) - last_nonzero
    
    # find sum
    sublist = lst[first_nonzero+1:last_nonzero]
    return sum(sublist)


# def calculate_sum(lst):
#     if lst.count(0) == 0:
#         return sum(lst)
#     elif lst.count(0) == 1:
#         ind = lst.index(0)
#         for i in lst
#     elif lst.count(0) > 1:
#         x1 = lst
