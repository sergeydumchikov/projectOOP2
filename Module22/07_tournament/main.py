K = int(input('Введите число К: '))
first_file = open('first_tour.txt', 'a')
text = []
text.append(str(K))
for _ in range(4):
    text.append(input())

write_text = '\n'.join(text)
first_file.write(write_text)
first_file.close()

from operator import itemgetter
second_file = open('second_tour.txt', 'w')
sec_text = []
for i in text[1::]:
    i_line = i.split()
    if int(i_line[2]) > K:
        sec_text.append(i_line)

sec_text = sorted(sec_text, key=itemgetter(2))
count = 0
result = []
for elem in sec_text[::-1]:
    count += 1
    elem[0], elem[1] = elem[1], elem[0]
    elem[0] = '{cou}) {el}.'.format(cou=count, el=elem[0][0])
    result.append(' '.join(elem))
result.insert(0, str(len(result)))
second_file.write('\n'.join(result))
second_file.close()
