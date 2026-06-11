def sum_numerals(n):
    """
    >>> sum_numerals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total