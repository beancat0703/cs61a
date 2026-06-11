def summation(n, term):
    """
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while(k <= n):
        total, k = total + term(k), k + 1
    return total

def sum_numerals(n):
    """
    >>> sum_numerals(5)
    15
    """
    return summation(n, identity)

def identity(k):
    return k

def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

def cube(k):
    return pow(k, 3)