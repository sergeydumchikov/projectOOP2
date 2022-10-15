

alph = 'abcdefghijklmnopqrstuvwxyz'
text = open('shifr.txt', 'w')
sym_list = []

for _ in range(3):
    sym = input()
    sym_list.append(sym)

sym_count = '\n'.join(sym_list)
text = open('text.txt', 'w')
text.write(sym_count)
text.close()
text = open('text.txt', 'r')
count = 0
shifr_str = []

for i_line in text:
    count += 1
    zero_str = ''
    for let in i_line:
        cou = 0
        for i_let in alph:
            cou += 1
            if i_let == let.lower():
                zero_str += alph[cou - 1 + count]
    shifr_str.append(zero_str.capitalize())

text.close()
shifr_count = '\n'.join(shifr_str)
new_text = open('shifr.txt', 'w')
new_text.write(shifr_count)
new_text.close()



