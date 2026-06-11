def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total = total + pow(k, 3)
        k = k + 1
    return total