site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search(key, struct, dep=10):
    if key in struct:
        return struct[key]
    if dep > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = search(key, sub_struct, dep-1)
                if result:
                    break
        else:
            result = 'Такого ключа нет в словаре'
        return result



desired_key = input('Введите искомый ключ: ')
maximum_depth = input('Хотите ввести максимальную глубину? ')

if maximum_depth == 'yes':
    max_dep = int(input('Введите максимальную глубину: '))
    print('Искомый ключ: {key}'.format(key=search(desired_key, site, dep=max_dep)))
elif maximum_depth == 'no':
    print('Искомый ключ: {key}'.format(key=search(desired_key, site)))