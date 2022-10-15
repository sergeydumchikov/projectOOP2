import os

numer_txt_file = open('numbers.txt', 'r')
asw_txt_file = open('answer.txt', 'w')
count = 0

for i_line in numer_txt_file:
    for i_elem in i_line:
        if i_elem.isdigit():
            count += int(i_elem)

asw_txt_file.write(str(count))
numer_txt_file.close()
asw_txt_file.close()
