# implement here your fibonacci function as instructed.

def fibonacci(n):
    """
    Returns the n-th Fibonacci number using naive recursion.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
