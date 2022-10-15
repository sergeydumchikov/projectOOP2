from operator import itemgetter
def sort(argument, dict_sort):
    if argument[1] in dict_sort.keys() and int(argument[0]) > dict_sort[argument[1]]:
        dict_sort[argument[1]] = int(argument[0])
    elif argument[1] not in dict_sort.keys():
        dict_sort[argument[1]] = int(argument[0])


record = int(input('Введите кол-во записей: '))
print('Записи (результат и имя):')
dict_players = {}
list_players = []

for i_rec in range(record):
    print('{номер} запись: '.format(номер=i_rec+1), end='')
    player = input().split()
    sort(player, dict_players)

list_players = list((dict_players.items()))
list_players = sorted(list_players, key=itemgetter(1), reverse=True)

print('\nИтоги соревнований')
for i in range(3):
    print('{i} место: '.format(i=i+1), end='')
    print(list_players[i][0], list_players[i][1])











