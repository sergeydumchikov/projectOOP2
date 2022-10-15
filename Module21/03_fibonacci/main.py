def fibonuchi(position, list,  start = 0):
    if list.index(list[start]) == position - 1:
        return list[start]

    list.append(list[start] + list[start + 1])
    start += 1
    return fibonuchi(position, list, start)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
fibonuchi_list = [1, 1]

print('Число: {num}'.format(num=fibonuchi(num_pos, fibonuchi_list)))



