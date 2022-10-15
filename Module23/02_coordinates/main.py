import random

def f(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        return x / y
    except Exception:
        print('Ошибка, что-то не так с первой функцией')

def f2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        return y / x
    except Exception:
        print('Ошибка, что-то не так со второй функцией')


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        number = random.randint(0, 100)
        with open('result.txt', 'w') as file_2:
            my_list = sorted([res1, res2, number])
            file_2.write(' '.join(my_list))



