import os

def num_subdir(directory):
    count = 0
    for i_elem in os.listdir(directory):
        path = os.path.join(directory, i_elem)
        if os.path.isdir(path):
            count += 1
    return count


def num_files(directory, dict):
    for i_elem in os.listdir(directory):
        path = os.path.join(directory, i_elem)
        if os.path.isfile(path):
            dict[path] = os.stat(path).st_size / 1024
        elif os.path.isdir(path):
           num_files(path, dict)
    return dict

dir_path = input('Введите путь до директории: ')
dict_files = {}
size_file = 0

for i_val in num_files(dir_path, dict_files).values():
    size_file += i_val

print(f'Размер каталога (в КБ): {size_file}')
print(f'Кол-во подкаталогов: {num_subdir(dir_path)}')
print(f'Кол-во файлов: {len(num_files(dir_path, dict_files))}')
