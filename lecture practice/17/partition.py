def partition(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partition(n - m, m):
            yield p + ' + ' + str(m)
        yield from partition(n, m -1)