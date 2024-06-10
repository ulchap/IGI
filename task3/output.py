
def print_result(res1, res2):
    """Outputs the result of the program in a table."""
    print("{:^15} | {:^15}".format("Digits", "Letters"))
    print("-" * 30)
    print("{:^15d} | {:^15d}".format(res1,res2))