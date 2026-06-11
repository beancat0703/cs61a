def count(s, value):
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def sum_list(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + sum_list(s[1:])
    
def large(s, n):
    if s == []:
        return []
    elif s[0] > n:
        return large(s[1:], n)
    else:

        with_s0 = [s[0]] + large(s[1:], n - s[0])
        without_s0 = large(s[1:], n)
        if sum_list(with_s0) > sum_list(without_s0):
            return with_s0
        else:
            return without_s0