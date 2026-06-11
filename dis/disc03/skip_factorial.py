def skip_factorial(n):
    if n <= 2:
        return n
    else:
        return n * skip_factorial(n - 2)