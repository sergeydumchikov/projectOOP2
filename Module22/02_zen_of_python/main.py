
zen_list = []
zen_txt_file = open('zen.txt', 'r')
for i_line in zen_txt_file:
    zen_list.append(i_line)

result = zen_list[::-1]
zen_txt_str = ''.join(result)
zen_txt_file.close()
zen_txt_file = open('zen.txt', 'w')
zen_txt_file.write(zen_txt_str)
zen_txt_file.close()