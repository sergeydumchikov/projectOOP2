def tpl_sort(lis):
    lis = sorted(lis)
    for num in lis:
        if num % 1 != 0:
            return orig_tuple
    return (i for i in lis)


orig_tuple = (1, -1, -6, 10, -3, 2, 4, 7)
copy_list = list(orig_tuple)

print(tpl_sort(copy_list))
