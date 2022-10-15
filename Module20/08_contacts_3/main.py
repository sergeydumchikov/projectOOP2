def ap_people(dictinp):
    name_family = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    name_family = tuple(name_family)
    num_tel = int(input('Введите номер телефона: '))
    if name_family in dict_peop:
        print('Такой человек уже есть в контактах')
    else:
        dictinp[name_family] = num_tel

def find_people():
    family = input('Введите фамилию для поиска: ').capitalize()
    for nam, fam in dict_peop.keys():
        fam = fam.capitalize()
        if fam == family or fam == family + 'а' or fam == family[:-1]:
            print(nam, fam, dict_peop[(nam, fam)])
        else:
            print('Такого человека нет в контактах')

dict_peop = {}
while True:
    print('\n1. Добавить новый контакт \n2. Найти контакт')

    action = int(input('Введите действие: '))
    if action == 1:
        ap_people(dict_peop)
    elif action == 2:
        find_people()
    else:
        print('Ошибка ввода!')

    print('Текущий словарь контактов: ', dict_peop)
