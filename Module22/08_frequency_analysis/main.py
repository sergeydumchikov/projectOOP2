from collections import Counter
text_file = open('text.txt', 'w')
text = 'Mama myla ramu.'
text_file.write(text)
text_file.close()
text_file = open('text.txt', 'r')
string = ''
num_let = 0

for sym in text_file.read():
    if sym.isalpha():
        string += sym.lower()
        num_let += 1
cou = Counter(string).most_common()
text_file.close()

analys_file = open('analysis.txt', 'a')
analys_list = []
cou = sorted(cou, key=lambda point: (-point[1], point[0]))
for i in cou:
    pair = f'{i[0]} : {round(i[1]/num_let, 3)}'
    analys_list.append(pair)
analys_file.write('\n'.join(analys_list))
analys_file.close()