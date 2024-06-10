import math
from decorators import decorate

@decorate
def get_function_value(x):
    """Calculates the function cos(x).
    
    Arguments:
    x -- float argument,|x|<=1
    """
    return math.cos(x)


def get_series_sum(x,eps,y):
    """Calculates the sum of given series.
    
    Arguments:
    x -- float argument
    eps -- specified accuracy
    y -- function's value
    
    Returns the sum and amount of iterations,
    alerts, if accuracy hasn't been achieved.
    """
    sum,component,n,prev_result=0,0,0,1000
    while True:
        component = ((-1)**n)*(x**(2*n)/math.factorial(2*n))
        sum+=component
        n+=1
        if n==501:
            print("500 iterations already done.")
            return sum,n
        if(abs(sum-y)<eps):
            print("Accuracy is achieved.")
            return sum,n
