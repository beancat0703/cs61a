def fib(n):
    a1 = 0
    a2 = 1
    k = 1
    while k < n:
        a1, a2 = a2, a1 + a2
        k += 1
    return a2