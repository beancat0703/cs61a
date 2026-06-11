def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return hailstone(n // 2) + 1

def odd(n):
    return hailstone(3 * n + 1) + 1