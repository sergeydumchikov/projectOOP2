def error_analise(text):
    text = text.split()
    try:
        if len(text[1]) > 1:
            raise IndexError
        if text[0].isalpha() or text[2].isalpha() or text[1].isalpha():
            raise TypeError
    except (IndexError, TypeError):
        print(f'Обнаружена ошибка в строке {text}', end=' ')
        question = input('Хотите исправить? ').lower()
        if question == 'да':
            text = input('Введите исправленную строку: ').split()
        else:
            return False
    return text


with open('calc.txt', 'r') as calc_file:
    summ = 0
    for line in calc_file:
        expres = error_analise(line)
        if expres:
            if expres[1] == '+':
                summ += int(expres[0]) + int(expres[2])
            elif expres[1] == '-':
                summ += int(expres[0]) - int(expres[2])
            elif expres[1] == '/':
                summ += int(expres[0]) / int(expres[2])
            elif expres[1] == '*':
                summ += int(expres[0]) * int(expres[2])


print(f'Сумма равна {summ}')