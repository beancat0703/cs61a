def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    m = x 
    digit_number = 0
    while x > 0:
        digit_number += 1
        x //= 10
    while digit_number >=1:
        a1 = m % 10
        m = m // 10
        a2 = m % 10
        if a1 >= a2:
            return True
        else:
            return False
        