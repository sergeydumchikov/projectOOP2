sym_sum = 0
count = 0

try:
    with open('people.txt', 'r', encoding='utf-8') as people_file:
        for i_line in people_file:
            count += 1
            lengh = len(i_line)
            if i_line.endswith('\n'):
                lengh -= 1
            if lengh < 3:
                print('Ошибка: длина строки {} менее 3-х символов'.format(count))
            sym_sum += lengh

except FileNotFoundError:
    print('Файл не найден')

finally:
    print('Сумма символов: ', sym_sum)

