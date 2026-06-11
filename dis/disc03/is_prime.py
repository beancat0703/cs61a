def is_prime(n):
    def check_factor(k):
        """Returns True if n is not divisible by any integer from k up to n-1."""
        if k == n:
            return True
        elif n % k == 0:
            return False
        else:
            return check_factor(k + 1)
    return check_factor(2)