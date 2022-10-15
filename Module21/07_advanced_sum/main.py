def sum_(*args):
    return sum(sum_(*arg) if isinstance(arg, list) else arg for arg in args)


print(sum_([[1, 2, [3]], [1], 3]))

