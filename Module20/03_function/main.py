def slicer(tuple, sym):
    count = 0
    start = 0
    for i_index, i_sym in enumerate(tuple):
        if i_sym == sym:
            count += 1
        if count == 1 and start == 0:
            start = i_index
        elif count == 2:
            finish = i_index
            return tuple[start:finish+1]

    if count == 1:
        return tuple[start:]
    else:
        return ()





my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
symbol = int(input('Введите случайный элемент: '))
print(slicer(my_tuple, symbol))
