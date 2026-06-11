def cascate(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascate(n // 10)
        print(n)