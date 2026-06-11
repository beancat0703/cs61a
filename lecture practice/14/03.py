from tree import *

numbers = tree(3, [tree(4), tree(5, [tree(6)])])

def print_sum(t, so_far):
    so_far = so_far + lable(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sum(b, so_far)

t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])

def count_paths(t, total):
    if lable(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - lable(t)) for b in branches(t)])
