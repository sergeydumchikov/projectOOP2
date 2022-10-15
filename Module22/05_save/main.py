import os


string = input('Введите строку: ')
text = input('Введите название файла, который хотите сохранить: ')
way = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
way_path = os.path.join('C:/', '/'.join(way))


if text not in os.listdir(way_path):
    file = open(os.path.join(way_path, text), 'w')
    file.write(string)
    print('Файл успешно сохранён!')
    file.close()
else:
    answer = input('Вы действительно хотите перезаписать файл? ').lower()
    if answer == 'да':
        file = open(os.path.join(way_path, text), 'w')
        file.write(string)
        print('Файл успешно перезаписан!')
        file.close()
    else:
        print('Файл не будет записан')
