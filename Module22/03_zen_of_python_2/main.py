import os
def rare_letter(text, rare_dict):
    del_sings = [' ', '!', '\n', '?', '.', ',', "'", '#', '*']
    for i_let in text.lower():
        if i_let in rare_dict:
            rare_dict[i_let] += 1
            continue
        if i_let not in del_sings:
            rare_dict[i_let] = 1

    return rare_dict



search_zen = os.path.abspath(os.path.join('..', '02_zen_of_python'))
zen_file_txt = open(os.path.join(search_zen, 'zen.txt'), 'r')

count_letter = 0
count_words = 0
count_str = 0
my_rare_dict = {}

for i_line in zen_file_txt:
    i_line_list = i_line.split()
    count_str += 1
    count_letter += len(i_line) - len(i_line_list) - 2
    count_words += len(i_line_list)
    rare = rare_letter(i_line, my_rare_dict)

zen_file_txt.close()
max_let = min(rare, key=rare.get)


print(f'Кол-во букв в файле: {count_letter}')
print(f'Кол-во слов в файле: {count_words}')
print(f'Кол-во строк в файле: {count_str}')
print(f'Наиболее редкая буква: {max_let}')