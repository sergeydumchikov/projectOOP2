import random

with open('out_file', 'a') as file:
    summ = 0
    num_list = []
    try:
        while True:
            number = int(input('Введите число: '))
            summ += number
            if summ >= 777:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                num_list.append(str(number))
                break
            ran_num = random.randint(1, 13)
            if ran_num == 7:
                print('Вас постигла неудача')
                break
            num_list.append(str(number))
        ap_list = '\n'.join(num_list)
        file.write(ap_list)
    except TypeError:
        print('Ошибка в типе данных')

print('Содержимое файла out_file: ')
with open('out_file', 'r') as file:
    for i in file:
        print(i, end='')