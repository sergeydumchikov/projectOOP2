def unzip(args, res):
    for arg in args:
        if isinstance(arg, list):
            unzip(arg, res)
        else:
            res.append(arg)
    return res


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
result = []
print(unzip(nice_list, result))
