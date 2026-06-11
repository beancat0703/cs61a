def count_down(n):
    if n > 0:
        yield n
        yield from count_down(n - 1)