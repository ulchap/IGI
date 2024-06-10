def decorate(func):
    """Decorates given function."""
    def new_func(x):
        print("Running function:",func.__name__)
        print("Arguments:",x)
        res=func(x)
        print("Result:",res)
        return res
    return new_func