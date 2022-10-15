def cycle(number, start=1):
    if number != start:
        print(start)
        start += 1
        return cycle(number, start)
    else:
        print(number)



my_number = int(input('Введите число: '))
cycle(my_number)